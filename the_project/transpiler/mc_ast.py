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


class Grace(Node):
    name = 'grace'

    def __init__(self, grace_type, notes, final_note):
        self.grace_type = grace_type
        self.notes = notes
        self.final_note = final_note

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
