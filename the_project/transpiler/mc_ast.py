'''
An intermediate representation of MusiCode code.
'''

class Node:
    name = 'node'

    def __repr__(self):
        return ("@%s%r" % (self.name, self.__dict__))
    


class Start(Node):
    name = 'start'
    
    def __init__(self, metadata, note_events=list()):
        self.metadata = metadata
        self.note_events = note_events

class Tempo(Node):
    name = 'tempo'

    def __init__(self, tempo_text=None, tempo_number=None, measure='1'):
        self.tempo_text = tempo_text
        self.tempo_number = tempo_number
        self.measure = measure

class Note(Node):
    name = 'note'

    def __init__(self, pitch, octave):
        self.pitch = pitch 
        self.octave = octave 
    
    def set_modifiers(self, modifiers):
        self.modifiers = modifiers 
    
    def set_duration(self, duration):
        self.duration = duration 

class Rest(Node):
    name = 'rest'

    def set_beaming(self, beaming):
        self.beaming = beaming 
    
    def set_duration(self, duration):
        self.duration = duration


class Chord(Node):
    name = 'chord'

    def __init__(self, notes):
        self.notes = notes

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
    
