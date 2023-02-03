'''
An intermediate representation of MusiCode code.
'''

import ly.dom as dom
import ly.pitch as pitch




class Note:
    def __init__(self, pitch, octave, duration):
        self.pitch = pitch
        self.octave = octave
        self.duration = duration

    def render(self, p):
        pitch = dom.Pitch(parent=p, octave=self.octave, note=self.pitch)
        duration = dom.Duration(self.duration, parent=p)
        return pitch, duration

    def __repr__(self):
        return ("(note %d %d %d)" % (self.pitch, self.octave, self.duration))


class Part:
    def __init__(self, instr, instr_name, notes):
        self.instrument = instr
        self.instrument_name = instr_name
        self.notes = notes

    def render(self, p):
        s = dom.Seq(parent=p)
        notes = [n.render(s) for n in self.notes]
        return s


class Metadata:
    def __init__(self, **kwargs):    # make more specific later
        self.metadata = kwargs


class Score:
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
