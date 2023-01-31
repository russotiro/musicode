'''
An intermediate representation of MusiCode code.
'''

class Note:
    def __init__(self, pitch, octave, duration):
        self.pitch = pitch
        self.octave = octave
        self.duration = duration

    def __str__(self):
        return ("(note %d %d %d)" % (self.pitch, self.octave, self.duration))

    def __repr__(self):
        return self.__str__()

class Part:
    def __init__(self, instr, instr_name, notes):
        self.instrument = instr
        self.instrument_name = instr_name
        self.notes = notes


class Metadata:
    def __init__(self, **kwargs):    # make more specific later
        self.metadata = kwargs


class Score:
    def __init__(self, metadata, parts):
        self.metadata = metadata
        self.parts = parts
