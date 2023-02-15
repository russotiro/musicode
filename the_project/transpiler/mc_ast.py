'''
An intermediate representation of MusiCode code.
'''


class Start:
    def __init__(self, metadata, note_events=list()):
        self.metadata = metadata
        self.note_events = note_events

class Note:
    def __init__(self, pitch, octave):
        self.pitch = pitch 
        self.octave = octave 
    
    def set_modifiers(self, modifiers):
        self.modifiers = modifiers 
    
    def set_duration(self, duration):
        self.duration = duration 

class Rest:
    def set_beaming(self, beaming):
        self.beaming = beaming 
    
    def set_duration(self, duration):
        self.duration = duration

class Modifiers:
    # TODO: Decide if it makes more sense to group modifiers 
    # (i.e. put articulation modifiers together, dynamic modifiers together, etc.)
    def __init__(self, modifiers):
        self.modifiers = modifiers 
    
