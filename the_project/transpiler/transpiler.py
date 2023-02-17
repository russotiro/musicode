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
        self.note_events = list() # Temporary list of note_events. TODO: Delete
        self.articulation_converter = {
            '.': 'staccato',
            '^': 'marcato',
            '_': 'tenuto',
            '>': 'accent',
            '~': 'tie'
        }

    def __concatenate_words(self, words):
        return ' '.join([word.value for word in words])
    
    def __symbol_to_word(self, symbol):
        return self.articulation_converter[symbol]

    def __determine_tempo_info(self, args):
        tempo_text = None
        tempo_number = None
        measure = '1'

        if len(args) == 1:
            if type(args[0]) == str:
                tempo_text = args[0]
            else:
                tempo_number = args[0]
        elif len(args) == 2:
            if type(args[0]) == str:
                tempo_text = args[0]
                if type(args[1]) == str:
                    measure = args[1]
                else:
                    tempo_number = args[1]
            else:
                tempo_number = args[0]
                measure = args[1]
        else:
            tempo_text = args[0]
            tempo_number = args[1]
            measure = args[2]

        return tempo_text, tempo_number, measure

    def start(self, args):
        print(args)
        return mc_ast.Start(self.metadata, self.note_events)

    def statement(self, args):
        return args[0]

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

    def tempo(self, args):
        tempo_text, tempo_number, measure = self.__determine_tempo_info(args)
        tempo = mc_ast.Tempo(tempo_text, tempo_number, measure)

        return ('tempo', tempo)

    def tempo_text(self, args):
        return self.__concatenate_words(args[1:-1])

    def tempo_number(self, args):
        # format = list of two numbers. first is note value, second is bpm
        args[1] = args[1].value
        return args
    
    def measure(self, args):
        return args[0].value[1:]
    
    def instrument_name(self, args):
        return self.__concatenate_words(args)

    def part(self, args):
        return ('part', args)

    def note_event(self, args):
        event = args[0]
        if isinstance(event, mc_ast.Note): # Augment Note with modifiers & duration if note
            modifiers = None
            duration = args[-1]
            if isinstance(args[1], mc_ast.Modifiers):
                modifiers = args[1]
            else:
                modifiers = mc_ast.Modifiers([])
            event.set_modifiers(modifiers)
            event.set_duration(duration)
        elif isinstance(event, mc_ast.Rest): # Augment Rest with duration if rest 
            duration = args[-1]
            event.set_duration(duration)
        else:
            mods = args[1] if len(args) == 3 else mc_ast.Modifiers([])
            duration = args[-1]
            event.set_duration(duration)
            event.set_modifiers(mods)

        self.note_events.append(event)
        return event

    def chord(self, args):
        return mc_ast.Chord(args)

    def note(self, args):
        # Initialize note instance with pitch and octave
        return mc_ast.Note(args[0], args[1])
    
    def pitch(self, args):
        return args[0].value
    
    def octave(self, args):
        return args[0].value
    
    def rest(self, args):
        rest = mc_ast.Rest()
        if args: # Check if beaming list is nonempty
            rest.set_beaming([arg.value for arg in args])
        else:
            rest.set_beaming(None)
        
        return rest
    
    def duration(self, args):
        return args[0].value
    
    def modifier_keyword(self, args):
        return args
    
    def articulation_keyword(self, args):
        return args[0]
    
    def piano_keyword(self, args):
        return args[0]
    
    def dynamics_keyword(self, args):
        return args[0]
    
    def beaming(self, args):
        return args[0]
    
    def modifier_list(self, args):
        modifiers = list()
        for arg in args:
            if type(arg) == list:
                modifiers.append(arg[0].value)
            elif type(arg) == str:
                modifiers.append(self.__symbol_to_word(arg))
            else:
                print('Something\'s gone horribly wrong in modifier_list')
        
        print("Modifiers: ")
        print(modifiers)
        return mc_ast.Modifiers(modifiers)
    
    def articulation_symbol(self, args):
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

    print("\n\nOriginal tree:\n\n")
    print(tree)
    print(result.metadata)
    print(result.note_events)


if __name__ == '__main__':
    main()


# 'system' function in 'os' package runs something as if it's running from the command line
# also 'popen' and 'call' functions
# module called 'subprocess'
