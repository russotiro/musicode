#!/usr/bin/env python3

'''
This version of the transpiler can only handle treble-clef music in 4/4
with one part. It currently only supports a score title, composer, and 
pitches and rhythms (no additional markings).
'''

import lark
import sys 

from lark import Lark, Transformer

import math 

import mc_ast




# Converter functions converting between values in naive AST and the integer 
# representation that would be passed into the ly library function. 
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
    def __init__(self):
        self.metadata = dict()

    def __concatenate_words(self, words):
        return ' '.join([word.value for word in words])

    def start(self, args):
        print(args)
        return mc_ast.Start(self.metadata)

    def statement(self, args):
        return args

    def title(self, args):
        title = self.__concatenate_words(args)
        self.metadata['title'] = title
        return ('title', title)

    def subtitle(self, args):
        subtitle = self.__concatenate_words(args)
        self.metadata['subtitle'] = subtitle
        return ('subtitle', subtitle)

    def composer(self, args):
        composer = self.__concatenate_words(args)
        self.metadata['composer'] = composer
        return ('composer', composer)

    def instruments(self, args):
        self.metadata['instruments'] = args
        return ('instruments', args)

    def instrument(self, args):
        return args[0].value





def main():
    if len(sys.argv) < 2:
        print("Usage: python3 transpiler.py musicodeFile")
        exit(1)

    grammar_file = open("../grammar/grammar.lark", "r")
    parser = lark.Lark(grammar_file.read())
    
    musicode_file = open(sys.argv[1], "r")
    tree = parser.parse(musicode_file.read())
    result = MyTransformer().transform(tree)

    print(result.metadata)


if __name__ == '__main__':
    main()


# 'system' function in 'os' package runs something as if it's running from the command line
# also 'popen' and 'call' functions
# module called 'subprocess'
