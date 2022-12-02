from lark import Lark, Transformer
# import ly.music.items as items
import ly.dom as dom
import ly.pitch as pitch

# notes:
#
# * lark lets you define a translator to immediatety turn a lark parse
#   tree into a custom-formatted one
# * ly.music is a work in progress, designed for building a lilypond AST
# * ly.dom lets you do something similar, but is also pretty-printable
# * ly.dom is deprecated and will be removed when ly.music is finished
#


# grammar = r"""
# pitch: "c"
# octave: "4"
# length: "whole"
# note: pitch octave ":" length
# """

# parser = Lark(grammar, start='note', parser='lalr')
# tree = parser.parse("c4:whole")


# naïve musicode AST, using dictionaries
ast = {'note': {'pitch': 3, 'octave': 4, 'length': 1}}

# def build_note(ast):
#     note = items.Note()
#     p = pitch.Pitch(note=ast['pitch'], octave=ast['octave'])
#     note.pitch = p
#     note.duration = ast['length']
#     return note

def build_note(ast):
    d = dom.Duration(ast['length'])
    p = dom.Pitch(octave=ast['octave'], note=ast['pitch'], parent=d)
    return p

n = build_note(ast['note'])
p = dom.Printer()
s = n.ly(p)
print(s)
