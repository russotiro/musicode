'''
An intermediate representation of MusiCode code.
'''

import ly.dom as dom
import ly.pitch as pitch



class Node:
    name = "node"

    def __repr__(self):
        return ("@" + self.name + str(self.__dict__) + "")


class Rest(Node):
    name = "rest"

    def __init__(self, duration):
        self.duration = duration


class Chord(Node):
    name = "chord"

    def __init__(self, notes, duration, mods=[]):
        # note!!! notes is a list of (pitch, octave) tuples
        self.notes = notes
        self.duration = duration
        self.mods = mods



class Note(Node):
    name = "note"

    def __init__(self, pitch, octave, duration, mods=[]):
        self.pitch = pitch
        self.octave = octave
        self.duration = duration
        self.mods = mods

    def render(self, p):
        pitch = dom.Pitch(parent=p, octave=self.octave, note=self.pitch)
        duration = dom.Duration(self.duration, parent=p)
        return pitch, duration



class Tempo(Node):
    name = "tempo"

    def __init__(self, desc=None, duration=None, bpm=None, measure=None):
        self.desc = desc
        self.duration = duration
        self.bpm = bpm
        self.measure = measure



class Part(Node):
    name = "part"

    def __init__(self, instr, instr_name, notes):
        self.instrument = instr
        self.instrument_name = instr_name
        self.notes = notes

    def render(self, p):
        s = dom.Seq(parent=p)
        notes = [n.render(s) for n in self.notes]
        return s


class Metadata(Node):
    name = "meta"

    def __init__(self, **kwargs):    # make more specific later
        self.metadata = kwargs


class Score(Node):
    name = "score"
    
    def __init__(self, metadata, parts):
        self.metadata = metadata
        self.parts = parts

    def render(self):
        hdr = dom.Header()
        hdr['title'] = self.metadata['title']
        hdr['composer'] = self.metadata['composer']

        score = dom.Score()
        notes = self.parts.render(score)

        return hdr, score
