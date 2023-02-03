#!/usr/bin/env python3

'''
This version of the transpiler can only handle treble-clef music in 4/4
with one part. It currently only supports a score title, composer, and 
pitches and rhythms (no additional markings).
'''

import lark
import sys 

from lark import Lark, Transformer
# import ly.music.items as items
import ly.dom as dom
import ly.pitch as pitch

import math 

import mc_ast



# GLOBAL CONVERTER
PITCH2INT = {
    'C': 0,
    'D': 1,
    'E': 2,
    'F': 3,
    'G': 4,
    'A': 5,
    'B': 6
}


# Converter functions converting between values in naive AST and the integer 
# representation that would be passed into the ly library function. 
def pitch2int(p):
    return PITCH2INT[p]

def octave2int(o):
    return o - 4

def duration2int(d):
    return int(math.log(d, 2))

# Add double bar line to the sequence 'parent' 
# def add_double_barline(parent):
#     barline_cmd = dom.Command("bar", parent=parent)
#     barline_txt = dom.Text("\"|.\"", parent=barline_cmd)



def flatten(xs):
    result = []

    for x in xs:
        if type(x) == list:
            f = flatten(x)
            result += x
        else:
            result.append(x)

    return result



class MyTransformer(Transformer):
    def duration(self, args):
        n = int(args[0].value)
        return ('duration', duration2int(n))
    
    def title(self, args):
        t = ' '.join([word.value for word in args])
        return ('title', t)

    def composer(self, args):
        name = ' '.join([word.value for word in args])
        return ('composer', name)
    
    def statement(self, args):
        return args

    def pitch(self, args):
        # note: need to handle accidentals
        n = pitch2int(args[0].value[0])
        return ('pitch', n)

    def octave(self, args):
        n = int(args[0].value)
        return ('octave', octave2int(n))

    def notes(self, args):
        return ('notes', args)

    def instruments(self, args):
        return ('instruments', args)

    def instrument(self, args):
        return ('instrument', args)

    def instrument_name(self, args):
        return ('instrument_name', args)

    def clef(self, args):
        return ('clef', args)

    def time(self, args):
        return ('time', args)

    def key(self, args):
        return ('key', args)
    
    def part(self, args):
        args = dict(args)
        return ('part', mc_ast.Part(args['instrument'], args['instrument_name'],
                                    args['notes']))

    def start(self, args):
        flat_args = flatten(args)
        # print(flat_args)
        dict_args = dict(flat_args)
        return mc_ast.Score(dict_args, dict_args['part'])
        
    
    def note(self, args):
        args = dict(args)
        return mc_ast.Note(args['pitch'], args['octave'],
                           args['duration'])        



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 transpiler.py musicodeFile")
        exit(1)

    grammar_file = open("grammar.lark", "r")
    parser = lark.Lark(grammar_file.read())
    
    musicode_file = open(sys.argv[1], "r")
    tree = parser.parse(musicode_file.read())
    hdr, score = MyTransformer().transform(tree).render()

    p = dom.Printer()
    print(hdr.ly(p))
    print(score.ly(p))

    
if __name__ == '__main__':
    main()


# 'system' function in 'os' package runs something as if it's running from the command line
# also 'popen' and 'call' functions
# module called 'subprocess'
