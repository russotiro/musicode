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
ast = {'pitch': {'note': 0, 'octave': 0, 'duration': 0}}

def build_pitch(ast, parent):
    dom.Pitch(octave=ast['octave'], note=ast['note'], parent=parent)
    dom.Duration(ast['duration'], parent=parent)


seq = dom.Seq()
build_pitch(ast['pitch'], seq)
root = seq

print(root.ly(dom.Printer()))

# how to use:
# python3 mc.py > test.ly
# lilypond --pdf test.ly
# $PDF_VIEWER test.pdf
