'''
An intermediate representation of MusiCode code.
'''

import databases
import sys

MC_TO_LILY_MODIFIERS_PRE = databases.mc_to_lily_pre_note_modifiers 
MC_TO_LILY_MODIFIERS_POST = databases.mc_to_lily_post_note_modifiers
PRE_MODIFIER_ORDER = databases.pre_modifier_order 
POST_MODIFIER_ORDER = databases.post_modifier_order 
INSTR_TO_SHORT_INSTR = databases.instr_to_short_instr
MIDI_NAMES = databases.normal_to_midi


class Node:
    name = 'node'

    def validate(self):
        return []

    def __repr__(self):
        return ("@%s%r" % (self.name, self.__dict__))
    


class Start(Node):
    name = 'start'
    
    def __init__(self, metadata, raw_list=list()):
        self.metadata = metadata
        self.raw_list = raw_list

    def validate(self):
        errors = []

        for item in self.raw_list:
            if type(item) == Part:
                errors += item.validate()
                
        return errors

    
    def render_header(self):
        metadata = self.metadata 
        header = f'''\\header {{
    title = "{metadata['title'] if 'title' in metadata else ""}"
    subtitle = "{metadata['subtitle'] if 'subtitle' in metadata else ""}"
    composer = "{metadata['composer'] if 'composer' in metadata else ""}"
}}
'''
        return header

    def render_library(self):
        return '''
DSfine = {
  \\once \\override Score.RehearsalMark #'break-visibility = #'#(#t #t #f)
  \\once \\override Score.RehearsalMark.self-alignment-X = #RIGHT
  \\mark \\markup { \\small "D.S. al fine" }
}

DCfine = {
  \\once \\override Score.RehearsalMark #'break-visibility = #'#(#t #t #f)
  \\once \\override Score.RehearsalMark.self-alignment-X = #RIGHT
  \\mark \\markup { \\small "D.C. al fine" }
}

DCcoda = {
  \\once \\override Score.RehearsalMark #'break-visibility = #'#(#t #t #f)
  \\once \\override Score.RehearsalMark.self-alignment-X = #RIGHT
  \\mark \\markup { \\small "D.C. al coda" }
}

DScoda = {
  \\once \\override Score.RehearsalMark #'break-visibility = #'#(#t #t #f)
  \\once \\override Score.RehearsalMark.self-alignment-X = #RIGHT
  \\mark \\markup { \\small "D.S. al coda" }
}

Fine = {
  \\once \\override Score.RehearsalMark #'break-visibility = #'#(#t #t #f)
  \\mark \\markup { \\small \\italic "fine" }
}

GotoCoda = {
  \\once \\override Score.RehearsalMark #'break-visibility = #'#(#t #t #f)
  \\once \\override Score.RehearsalMark.self-alignment-X = #RIGHT
  \\mark \\markup { \\small "To Coda" \\raise #0.5 \\smaller \\musicglyph #"scripts.coda" }
}

Coda = {
  \\once \\override Score.RehearsalMark #'break-visibility = #'#(#f #t #t)
  \\mark \\markup { " " \\musicglyph #"scripts.coda" \\lower #0.9 "Coda" }
}

Segno = {
  \\once \\override Score.RehearsalMark #'break-visibility = #'#(#f #t #t)
  \\mark \\markup { \\small \\musicglyph #"scripts.segno" }
}

\paper { left-margin = 0.75\in }

'''
    
    def render_parts(self):
        result = '<<\n'
        for item in self.raw_list:
            if type(item) == tuple and item[0] == 'group':
                if item[1] == 'begin':
                    result += "\\new StaffGroup <<\n"
                elif item[1] == 'end':
                    result += ">>\n"
            elif type(item) == Part:
                result += item.render() + '\n'
        return result + '\n>>\n'
    
    def render(self, midi: bool = False):
        result = '\\version "2.24.1"\n' + self.render_header() + self.render_library()

        if midi:
            result += "\\score {\n"
        result += self.render_parts()

        if midi:
            result += "\\midi { }\n}\n"
        return result

class Tempo(Node):
    name = 'tempo'

    def __init__(self, tempo_text, tempo_number):
        self.tempo_text = tempo_text
        self.tempo_number = tempo_number

    def validate(self):
        return []

    def extract_tempo_number(self):
        if self.tempo_number == []:
            return ""
        else:
            return f'{self.tempo_number[0]} = {self.tempo_number[1]}'

    def render(self):
        result = "\\tempo "
        lily_tempo_text = f'"{self.tempo_text}"'
        lily_tempo_number = self.extract_tempo_number()

        if self.tempo_number == []:
            result += lily_tempo_text
        elif self.tempo_text == "":
            result += lily_tempo_number
        else:
            result += lily_tempo_text + " " + lily_tempo_number

        return result


class Barline(Node):
    name = 'barline'

    def __init__(self, type):
        self.type = type

    def validate(self):
        return []

    def render(self):
        line = {
            'single': '|',
            'double': '||',
            'repeatBegin': '.|:',
            'repeatEnd': ':|.',
            'final': '|.',
            'dotted': ';'
        }[self.type]

        return ('\\bar "%s"' % line)


class Clef(Node):
    name = 'clef'

    def __init__(self, value=""):
        self.value = value

    def validate(self):
        return []

    def render(self):
        return "\\clef " + self.value


class Key(Node):
    name = 'key'

    def __init__(self, value=""):
        self.mode = "major"
        if 'm' in value:
            self.mode = "minor"
        self.pitch = Pitch(value.replace('m','').replace('M',''))

    def validate(self):
        return []

    def render(self):
        return "\\key " + self.pitch.render() + " \\" + self.mode


class Time(Node):
    name = 'time'

    def __init__(self, time=None):
        self.time = time

    def validate(self):
        return []

    def render(self):
        if self.time == 'common':
            return "\\defaultTimeSignature\n\\time 4/4"
        elif self.time == 'cut':
            return "\\defaultTimeSignature\n\\time 2/2"
        else:
            string = "\\numericTimeSignature\n\\time "
            string += self.time[0] + "/" + self.time[1]
            return string


class Note(Node):
    name = 'note'

    def __init__(self, pitch=None, octave=None, modifiers=None, duration=None):
        self.pitch = Pitch(pitch)
        self.octave = octave 
        self.modifiers = modifiers 
        self.duration = duration 
    
    def set_modifiers(self, modifiers):
        self.modifiers = modifiers 
    
    def set_duration(self, duration):
        self.duration = duration 

    def render_pitch_octave(self):
        return self.pitch.render() + self.lily_octave(self.octave)

    def render(self):
        lily = self.render_pitch_octave() + self.duration
        return self.modifiers.render_pre_event() + lily + self.modifiers.render_post_event()

    def lily_octave(self, octave):
        octave = int(octave)
        if octave >= 3:
            return "'" * (octave - 3)
        else:
            return "," * (3 - octave)


class Pitch(Node):
    name = 'pitch'

    def __init__(self, pitch=""):
        self.pitch = pitch

    def render(self):
        return self.lily_pitch(self.pitch)

    def lily_pitch(self, pitch):
        if len(pitch) == 1:
            return pitch.lower()
        elif len(pitch) == 2 and pitch[1] == "#":
            return pitch[0].lower() + "is"
        elif len(pitch) == 2 and pitch[1] == "b":
            return pitch[0].lower() + "es"
        else:
            sys.stderr.write("ERROR: Invalid pitch.\n")


class Rest(Node):
    name = 'rest'

    def __init__(self, rest_type=None, beaming=None, duration=None):
        self.rest_type = rest_type
        self.beaming = beaming 
        self.duration = duration 

    def set_beaming(self, beaming):
        self.beaming = beaming 
    
    def set_duration(self, duration):
        self.duration = duration
    
    def render(self):
        lily = self.rest_type + self.duration 
        modifiers = Modifiers(self.beaming)
        return modifiers.render_pre_event() + lily + modifiers.render_post_event()


class Chord(Node):
    name = 'chord'

    def __init__(self, notes, modifiers=None, duration=None):
        self.notes = notes
        self.modifiers = modifiers 
        self.duration = duration 

    def set_modifiers(self, modifiers):
        self.modifiers = modifiers

    def set_duration(self, duration):
        self.duration = duration
    
    def render(self):
        lily = "<"
        for note in self.notes:
            lily += note.render_pitch_octave() + ' '
        lily += ">"
        lily += self.duration 
        return self.modifiers.render_pre_event() + lily + self.modifiers.render_post_event()


class Modifiers(Node):
    name = 'modifiers'

    def __init__(self, modifiers):
        self.modifiers = modifiers
    
    def __check_no_duplicate_numbers(self, modifiers, modifier_order):
        # Assumes that 'modifiers' has ALREADY been sorted using 'modifier_order'
        for i in range(len(modifiers) - 1):
            curr_modifier = modifiers[i]
            next_modifier = modifiers[i + 1]
            if modifier_order[curr_modifier] == modifier_order[next_modifier]:
                sys.stderr.write(f'ERROR: Cannot apply both "{curr_modifier}" and "{next_modifier}" to '
                                  'the same note, rest, or chord.\n')
    
    def __sort_pre_modifiers(self):
        # Extract only modifiers that should appear before the event 
        pre_modifiers = filter(lambda modifier : modifier in MC_TO_LILY_MODIFIERS_PRE, self.modifiers)
        pre_modifiers = list(pre_modifiers)

        pre_modifiers.sort(key=lambda modifier : PRE_MODIFIER_ORDER[modifier])

        # Check that event does not contain modifiers that would result in an error thrown in LilyPond, 
        # e.g. no beamBegin and beamEnd on the same note 
        self.__check_no_duplicate_numbers(pre_modifiers, PRE_MODIFIER_ORDER)

        return pre_modifiers 
    
    def __sort_post_modifiers(self):
        post_modifiers = self.modifiers.copy() 

        post_modifiers.sort(key=lambda modifier : POST_MODIFIER_ORDER[modifier])

        # Check that event does not contain modifiers that would result in an error thrown in LilyPond, 
        # e.g. no beamBegin and beamEnd on the same note 
        self.__check_no_duplicate_numbers(post_modifiers, POST_MODIFIER_ORDER)

        return post_modifiers 
    
    def render_pre_event(self):
        lily_modifier_list = list()

        sorted_modifiers = self.__sort_pre_modifiers()

        for modifier in sorted_modifiers:
            lily_modifier_list.append(MC_TO_LILY_MODIFIERS_PRE[modifier])
         
        if lily_modifier_list == []:
            return ''
        return ' '.join(lily_modifier_list) + ' '

    def render_post_event(self):
        lily_modifier_list = list()

        sorted_modifiers = self.__sort_post_modifiers()

        for modifier in sorted_modifiers:
            if modifier in MC_TO_LILY_MODIFIERS_POST:
                lily_modifier_list.append(MC_TO_LILY_MODIFIERS_POST[modifier])
            else:
                # Assume modifier is just prepended by a backslash if not in dictionary 
                lily_modifier_list.append("\\" + modifier)
        
        return ' '.join(lily_modifier_list)

class Symbol(Node):
    name = 'symbol'

    def __init__(self, s_type):
        self.type = s_type 
    
    def validate(self):
        return []

    def render(self):
        if self.type == 'segno':
            return '\\Segno'
        else:
            sys.stderr.write('Something\'s gone horribly wrong in Symbol rendering!\n')

class Text(Node):
    name = 'text'

    def __init__(self, t_type, contents):
        self.type = t_type 
        self.contents = contents 

    def validate(self):
        return []
    
    def __set_road_map_converter(self):
        self.road_map_converter = {
            'd.c. al fine': '\\DCfine',
            'd.c. al coda': '\\DCcoda',
            'd.s. al fine': '\\DSfine',
            'd.s. al coda': '\\DScoda',
            'tocoda': '\\GotoCoda'
        }
    
    def render(self):
        if self.type == 'road_map':
            self.__set_road_map_converter()
            return self.road_map_converter[self.contents]
        elif self.type == 'expression':
            return f'\\tweak direction #DOWN \\mark \\markup {{ \\small \\italic "{self.contents}" }}'
        elif self.type == 'technique':
            result = '\\once \\override Score.RehearsalMark.self-alignment-X = #LEFT\n'
            return result + f'\\mark \\markup \\small "{self.contents}"'
        else:
            sys.stderr.write('Tried to render Text of invalid type.\n')


class Break(Node):
    name = 'break'

    def __init__(self, type):
        self.type = type

    def render(self):
        if self.type == 'line':
            return '\\break'
        elif self.type == 'page':
            return '\\pageBreak'
        else:
            sys.stderr.write('Invalid break type.\n')


class Tuplet(Node):
    name = 'tuplet'

    def __init__(self, fraction, notes_argument_list):
        self.fraction = fraction
        self.notes_argument_list = notes_argument_list

    def render(self):
        string = "\\tuplet " + self.fraction + " { "
        return string + ' '.join([arg.render() for arg in self.notes_argument_list]) + " }"


class Grace(Node):
    name = 'grace'

    def __init__(self, grace_type, notes, final_note):
        self.grace_type = grace_type
        self.notes = notes
        self.final_note = final_note

    def validate(self):
        errors = []
        errors += self.notes.validate()
        errors += self.final_note.validate()
        return errors

    def render(self):
        result = ""
        if self.grace_type == "slash":
            result += "\\slashedGrace "
        elif self.grace_type == "noSlash":
            result += "\\grace "
        else:
            sys.stderr.write("Grace type must be slash or noSlash.\n")
        result += self.notes.render() + ' '

        return result + self.final_note.render()


class Tremolo(Node):
    name = 'tremolo'

    def __init__(self, num_bars, note1, note2):
        self.num_bars = int(num_bars)
        self.note1 = note1
        self.note2 = note2

    def validate(self):
        errors = []
        if self.note1.duration != self.note2.duration:
            e = "Invalid tremolo: differing note durations in %r and %r"
            # TODO: it would be nice to pretty-print these notes in
            # musicode syntax
            e %= self.note1, self.note2
            errors.append(e)
        return errors

    def render(self):
        # Get the Lilypond duration of each note in tremolo (2^(2+num_bars))
        # 1 bar = 8th note, 2 bars = 16th note, 3 bars = 32nd note
        ly_duration = 2 ** (2 + self.num_bars)

        # Find index of first dot in duration (parsing numerical value from dots)
        first_dot_index = self.note1.duration.find('.')

        num_dots = 0
        mc_duration_no_dots = 0
        if first_dot_index == -1: # Case 1: No dots in duration 
            num_dots = 0
            mc_duration_no_dots = int(self.note1.duration)
        else: # Case 2: At least one dot in duration 
            num_dots = len(self.note1.duration[first_dot_index:])
            mc_duration_no_dots = int(self.note1.duration[:first_dot_index])

        # Get the Lilypond number of repeats without accounting for dotted rhythms:
        # num_repeats = ly_duration / (2 * mc_duration_without_dots)
        # This is the number of times that the tremolo pattern is repeated
        # The 2 accounts for two notes per repetition 
        reps = ly_duration / (2 * mc_duration_no_dots)

        # Account for dotted rhythms, increasing length by 1-(1/2)^num_dots percent 
        reps += (1 - 0.5**num_dots) * reps

        # Edit Note durations from MusiCode duration to LilyPond duration 
        self.note1.duration = str(ly_duration)
        self.note2.duration = str(ly_duration)

        # Produce and return output string 
        result = "\\repeat tremolo " + str(int(reps)) + " { " + self.note1.render()
        return result + " " + self.note2.render() + " }"

class Notes(Node):
    name = 'notes'

    def __init__(self, notes_args):
        self.notes_args = notes_args
    
    def validate(self):
        errors = []
        for arg in self.notes_args:
            errors += arg.validate()
        return errors

    def render_notes(self):
        return ' '.join([arg.render() for arg in self.notes_args])
    
    def render(self):
        return '{ ' + self.render_notes() + ' }'

class Voice(Node):
    name = 'voice'

    def __init__(self, notes):
        self.notes = notes 
        self.voiceNumKeywords = ['voiceOne', 'voiceTwo', 'voiceThree', 'voiceFour']
    
    def render(self, voiceNum):
        # voiceNum is voice number MINUS ONE (e.g. 0 should be inputted for voiceOne)
        if voiceNum < 0 or voiceNum > 3:
            sys.stderr.write(f'ERROR: Invalid voiceNum {voiceNum}; must be between 0 and 3\n')
        return f'\\new Voice {{ \\{self.voiceNumKeywords[voiceNum]} {self.notes.render_notes()} }}'

class Voices(Node):
    name = 'voices'

    def __init__(self, voices):
        self.voices = voices 
    
    def validate(self):
        return []

    def render(self):
        if len(self.voices) > 4:
            sys.stderr.write(f'ERROR: Cannot transpile. There are {len(self.voices)} voices in a '
                              'voices block. The maximum number of voices supported is 4.\n')
        
        result = '<<\n'
        for i in range(len(self.voices)):
            result += self.voices[i].render(i) + '\n'
        result += '>> \\oneVoice\n'
        return result 

class Ending(Node):
    name = 'ending'

    def __init__(self, numbers, content):
        self.numbers = numbers
        self.content = content

    def validate(self):
        if len(set(self.numbers)) != len(self.numbers):
            return ["Invalid ending: repeated numbers in %r" % self.numbers]
        else:
            return []

    def render(self):
        result = "\\set Score.repeatCommands = #'((volta \""
        result += ', '.join([str(n) for n in self.numbers]) + "\"))\n"
        for env in self.content:
            result += " " + env.render()
        result += "\n\\set Score.repeatCommands = #'((volta #f))\n"
        return result


class Part(Node):
    name = 'part'

    def __init__(self, instr_name, staffs):
        self.instrument_name = instr_name
        self.staffs = staffs

    def validate(self):
        errors = []
        for staff in self.staffs:
            errors += staff.validate()
        return errors

    def short_instr(self):
        if self.instrument_name in INSTR_TO_SHORT_INSTR:
            return INSTR_TO_SHORT_INSTR[self.instrument_name]
        elif len(self.instrument_name) <= 4:
            return self.instrument_name
        elif ' ' in self.instrument_name:
            words = self.instrument_name.split()
            result = ""
            for word in words:
                result += word[0] + ". "
            return result[:-1]
        else:
            return self.instrument_name[0:3] + '.'

    def render_instr_names(self):
        midi_name = self.instrument_name.lower()
        if midi_name in MIDI_NAMES:
            midi_name = MIDI_NAMES[midi_name]

        result  = '    instrumentName = "' + self.instrument_name + ' "\n'
        result += '    shortInstrumentName = "' + self.short_instr() + ' "\n'
        result += '    midiInstrument = "' + midi_name + '"\n'
        return result

    def render_staffs(self):
        result = ""
        for staff in self.staffs:
            result += '    \\new Staff {\n        ' + staff.render() + '\n}\n'
        return result

    def render(self):
        if len(self.staffs) == 1:
            result =  '\\new Staff \\with {\n'
            result += self.render_instr_names()
            result += '} {\n    '
            result += self.staffs[0].render()
            result += '\n}'
            return result

        elif self.instrument_name in databases.grand_staffs:
            result =  '\\new PianoStaff \\with {\n'
            result += self.render_instr_names()
            result += '} <<\n'
            result += self.render_staffs()
            result += '>>\n'
            return result

        else: # non-grand-staff multi-staff parts
            result  = '\\new StaffGroup \\with {\n'
            result += self.render_instr_names()
            result += '} { <<\n\\set StaffGroup.systemStartDelimiter = #\'SystemStartSquare\n'
            result += self.render_staffs()
            result += '>> }\n'
            return result


class Staff(Node):
    name = 'staff'

    def __init__(self, staff_environments):
        self.staff_environments = staff_environments

    def validate(self):
        errors = []
        for env in self.staff_environments:
            errors += env.validate()
        return errors

    def render(self):
        return '\n'.join(staff_env.render() for staff_env in self.staff_environments)

    
class Coda(Node):
    name = 'coda'

    def __init__(self, envs):
        self.staff_environments = envs

    def validate(self):
        return []

    def render(self):
        result = '''\\cadenzaOn \\stopStaff
                    \\repeat unfold 1 {
                        s1
                        \\bar ""
                    }
                    \\startStaff \\cadenzaOff
                    \\break
                    \\once \\override Staff.KeySignature.break-visibility = #end-of-line-invisible
                    \\once \\override Staff.Clef.break-visibility = #end-of-line-invisible
                 '''
        result += "\\Coda"
        for env in self.staff_environments:
            result += " " + env.render()
        return result
