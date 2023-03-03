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
        self.part_list = list()
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

    def __parse_ending_numbers(self, s):
        return [int(n) for n in s.split(',')]
    
    def __determine_tempo_info(self, args):
        tempo_text = ""
        tempo_number = []

        if len(args) == 1:
            if type(args[0]) == str:
                tempo_text = args[0]
            else:
                tempo_number = args[0]
        elif len(args) == 2:
            tempo_text = args[0]
            tempo_number = args[1]
        else:
            sys.stderr.write("something went wrong in __determine_tempo_info\n")

        return tempo_text, tempo_number

    def start(self, args):
        return mc_ast.Start(self.metadata, self.part_list)

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

    def tempo(self, args):
        tempo_text, tempo_number = self.__determine_tempo_info(args)
        tempo = mc_ast.Tempo(tempo_text, tempo_number)

        return tempo

    def tempo_text(self, args):
        return self.__concatenate_words(args[1:-1])

    def tempo_number(self, args):
        # format = list of two numbers. first is note value, second is bpm
        args[1] = args[1].value
        return args
    
    def instrument_name(self, args):
        return self.__concatenate_words(args)

    def part(self, args):
        part = mc_ast.Part(args[0], args[1:])
        self.part_list.append(part)
        return part

    def note_event(self, args):
        event = args[0]
        if isinstance(event, mc_ast.Note): # Augment Note with modifiers & duration if note
            modifiers = None
            duration = args[-1]
            if isinstance(args[1], mc_ast.Modifiers):
                modifiers = args[1]
            else:
                modifiers = mc_ast.Modifiers([])
            event.modifiers = modifiers
            event.duration = duration
        elif isinstance(event, mc_ast.Rest): # Augment Rest with duration if rest 
            duration = args[-1]
            event.duration = duration
        elif isinstance(event, mc_ast.Chord):
            mods = args[1] if len(args) == 3 else mc_ast.Modifiers([])
            duration = args[-1]
            event.duration = duration
            event.modifiers = mods
        else:
            sys.stderr.write("ERROR: note_event must be note, rest, or chord.\n")

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
            rest.set_beaming([])
        
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
                sys.stderr.write('Something\'s gone horribly wrong in modifier_list\n')
        
        return mc_ast.Modifiers(modifiers)
    
    def articulation_symbol(self, args):
        return args[0].value

    # staff events

    def clef(self, args):
        return mc_ast.Clef(args[0].value)

    def key(self, args):
        return mc_ast.Key(args[0].value)

    def time(self, args):
        if len(args) == 1:
            return mc_ast.Time(args[0].value)
        elif len(args) == 2:
            return mc_ast.Time([args[0].value, args[1]])
        else:
            sys.stderr.write("something went wrong in time\n")

    def barline(self, args):
        barline_database = ['single', 'double', 'repeatBegin', 'repeatEnd', 'final', 'dotted']

        if args[0].value in barline_database:
            return mc_ast.Barline(args[0].value)
        else:
            sys.stderr.write("You tried to set an invalid barline type: " + args[0].value + "\n")

    def symbol(self, args):
        symbol_database = ['segno']

        if args[0].value in symbol_database:
            return mc_ast.Symbol(args[0].value)
        else:
            sys.stderr.write("You tried to set an invalid symbol type: " + args[0].value + "\n")

    def road_map_text(self, args):
        return mc_ast.Text('road_map', args[0].value.lower())

    def expression_text(self, args):
        return mc_ast.Text('expression', self.__concatenate_words(args))

    def technique_text(self, args):
        return mc_ast.Text('technique', self.__concatenate_words(args))

    def text(self, args):
        return args[0]

    def staff_event(self, args):
        return args[0]

    # note environments

    def notes_argument(self, args):
        return args[0]

    def tuplet(self, args):
        return mc_ast.Tuplet(args[0].value, args[1:])

    def grace_type(self, args):
        return args[0].value

    def notes(self, args):
        return mc_ast.Notes(args)

    def voice(self, args):
        # args[0] is a notes instance
        return mc_ast.Voice(args[0])

    def voices(self, args):
        # args[0] is a list of voice instances
        return mc_ast.Voices(args)

    def note_environment(self, args):
        return args[0]

    def staff_environment(self, args):
        return args[0]

    def grace(self, args):
        grace_type = 'slash'

        if type(args[0]) == 'str':
            grace_type = args[0]
        
        notes = args[-2]
        final_note = args[-1]

        return mc_ast.Grace(grace_type, notes, final_note)

    def tremolo(self, args):
        return mc_ast.Tremolo(*args)

    def coda(self, args):
        return mc_ast.Coda(args)

    def ending(self, args):
        numbers = args[0].value
        return mc_ast.Ending(self.__parse_ending_numbers(numbers), args[1:])

    def staff(self, args):
        return mc_ast.Staff(args)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 transpiler.py musicodeFile")
        exit(1)

    grammar_file = open("../grammar/grammar.lark", "r")
    parser = lark.Lark(grammar_file.read())
    
    musicode_file = open(sys.argv[1], "r")
    tree = parser.parse(musicode_file.read())
    result = MyTransformer().transform(tree)

    print(result)
    # print(result.render())



if __name__ == '__main__':
    main()


# 'system' function in 'os' package runs something as if it's running from the command line
# also 'popen' and 'call' functions
# module called 'subprocess'
