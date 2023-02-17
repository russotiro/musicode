'''
An intermediate representation of MusiCode code.
'''

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

class Note(Node):
    name = 'note'

    def __init__(self, pitch=None, octave=None, modifiers=None, duration=None):
        self.pitch = pitch 
        self.octave = octave 
        self.modifiers = modifiers 
        self.duration = duration 
    
    def set_modifiers(self, modifiers):
        self.modifiers = modifiers 
    
    def set_duration(self, duration):
        self.duration = duration 

class Rest(Node):
    name = 'rest'

    def __init__(self, beaming=None, duration=None):
        self.beaming = beaming 
        self.duration = duration 

    def set_beaming(self, beaming):
        self.beaming = beaming 
    
    def set_duration(self, duration):
        self.duration = duration


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


class Modifiers(Node):
    name = 'modifiers'
    # TODO: Decide if it makes more sense to group modifiers 
    # (i.e. put articulation modifiers together, dynamic modifiers together, etc.)
    def __init__(self, modifiers):
        self.modifiers = modifiers 
    

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
