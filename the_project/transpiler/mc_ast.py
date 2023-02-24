'''
An intermediate representation of MusiCode code.
'''

import modifier_dictionary
import sys

mc_to_lily_modifiers = modifier_dictionary.mc_to_lily_modifiers


class Node:
    name = 'node'

    def __repr__(self):
        return ("@%s%r" % (self.name, self.__dict__))
    


class Start(Node):
    name = 'start'
    
    def __init__(self, metadata, part_list=list()):
        self.metadata = metadata
        self.part_list = part_list

class Tempo(Node):
    name = 'tempo'

    def __init__(self, tempo_text, tempo_number):
        self.tempo_text = tempo_text
        self.tempo_number = tempo_number

    def render(self):
        return ("\\tempo \"%s\" %s" % (self.tempo_text, self.tempo_number))


class Barline(Node):
    name = 'barline'

    def __init__(self, type):
        self.type = type

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

    def render(self):
        return "\\clef " + self.value


class Key(Node):
    name = 'key'

    def __init__(self, value=""):
        self.mode = "major"
        if 'm' in value:
            self.mode = "minor"
        self.pitch = Pitch(value.replace('m','').replace('M',''))

    def render(self):
        return "\\key " + self.pitch.render() + " \\" + self.mode


class Time(Node):
    name = 'time'

    def __init__(self, time=None):
        self.time = time

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
        return lily + self.modifiers.render()

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

    def __init__(self, beaming=None, duration=None):
        self.beaming = beaming 
        self.duration = duration 

    def set_beaming(self, beaming):
        self.beaming = beaming 
    
    def set_duration(self, duration):
        self.duration = duration
    
    def render(self):
        lily = "r" + self.duration 
        return lily + Modifiers(self.beaming).render()


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
            lily += note.render_pitch_octave()
        lily += ">"
        lily += self.duration 
        return lily + self.modifiers.render()


class Modifiers(Node):
    name = 'modifiers'
    # TODO: Decide if it makes more sense to group modifiers 
    # (i.e. put articulation modifiers together, dynamic modifiers together, etc.)
    def __init__(self, modifiers):
        self.modifiers = modifiers

    def render(self):
        lily_modifier_list = list()
        for modifier in self.modifiers:
            if modifier in mc_to_lily_modifiers:
                lily_modifier_list.append(mc_to_lily_modifiers[modifier])
            else:
                # Assume modifier is just prepended by a backslash if not in dictionary 
                lily_modifier_list.append("\\" + modifier)
        
        return ' '.join(lily_modifier_list)

class Symbol(Node):
    name = 'symbol'

    def __init__(self, s_type):
        self.type = s_type 
    
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
    
    def __set_road_map_converter(self):
        self.road_map_converter = {
            'd.c. al fine': '\\DCfine',
            'd.c. al coda': '\\DCcoda',
            'd.s. al fine': '\\DSfine',
            'd.s. al coda': '\\DScoda',
            'toCoda': '\\GotoCoda'
        }
    
    def render(self):
        if self.type == 'road_map':
            self.__set_road_map_converter()
            return self.road_map_converter[self.contents]
        elif self.type == 'expression':
            return f'\\tweak direction #DOWN \\mark \\markup {{ \\small \\italic "{self.contents}" }}'
        elif self.type == 'technique':
            return f'\\mark "{self.contents}"'
        else:
            sys.stderr.write('Tried to render Text of invalid type.\n')


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

    def render(self):
        result = ""
        if self.grace_type == "slash":
            result += "\\slashedGrace"
        elif self.grace_type == "noSlash":
            result += "\\grace"
        else:
            sys.stderr.write("Grace type must be slash or noSlash.\n")
        result += " { " + ' '.join([arg.render() for arg in self.notes]) + " } "

        return result + self.final_note.render()


class Tremolo(Node):
    name = 'tremolo'

    def __init__(self, num_bars, note1, note2):
        self.num_bars = int(num_bars)
        self.note1 = note1
        self.note2 = note2
        
        if note1.duration != note2.duration:
            sys.stderr.write("Invalid tremolo: differing note durations\n")

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


class Ending(Node):
    name = 'ending'

    def __init__(self, numbers, content):
        self.numbers = numbers
        self.content = content


class Part(Node):
    name = 'part'

    def __init__(self, instr, instr_name, content):
        self.instrument = instr
        self.instrument_name = instr_name
        self.content = content
