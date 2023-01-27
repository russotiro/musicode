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

# Extracts value from node 'node' in the lark tree 
def extract_node_value(node):
    values = node.pretty().split()[1:]
    return ' '.join(values)

# Extracts information from lark tree and returns dictionary containing stored info 
def extract_score_info(tree):
    result = dict() 

    # Get score metadata (title, composer)
    # TODO: Ensure that only one title and one composer is provided 
    for title in tree.find_data("title"):
        result['title'] = extract_node_value(title)
    for composer in tree.find_data('composer'):
        result['composer'] = extract_node_value(composer)

    # Get all notes. TODO: Handle more than one part 
    notes_list = list()
    all_part_nodes = tree.find_data("part") # Extract iterable of all parts 
    for part_node in all_part_nodes:
        note_nodes = part_node.find_data("note") # Extract iterable of all notes within current part 
        for note_node in note_nodes:
            note_map = dict()
            # Each 'for' loop below goes through a one-element iterable
            for pitch_node in note_node.find_data("pitch"):
                pitch = extract_node_value(pitch_node)
                note_map['pitch'] = pitch 
            for octave_node in note_node.find_data("octave"):
                octave = int(extract_node_value(octave_node))
                note_map['octave'] = octave 
            for duration_node in note_node.find_data("duration"):
                duration = int(extract_node_value(duration_node))
                note_map['duration'] = duration 
            notes_list.append(note_map)
    result['notes'] = notes_list 

    return result 


# Converter functions converting between values in naive AST and the integer 
# representation that would be passed into the ly library function. 
def pitch2int(p):
    return PITCH2INT[p]

def octave2int(o):
    return o - 4

def duration2int(d):
    return int(math.log(d, 2))

# Add note 'note' to the sequence 'parent'
def add_note(note, parent):
    pitch = dom.Pitch(octave=octave2int(note['octave']),
                      note=pitch2int(note['pitch']),
                      parent=parent)
    duration = dom.Duration(duration2int(note['duration']), parent=parent)

# Add double bar line to the sequence 'parent' 
def add_double_barline(parent):
    barline_cmd = dom.Command("bar", parent=parent)
    barline_txt = dom.Text("\"|.\"", parent=barline_cmd)

# Print lilypond code for score with info contained in 'ast' 
def print_score(ast):
    header = dom.Header();
    header['title'] = ast['title']
    header['composer'] = ast['composer']

    score = dom.Score()
    notes = dom.Seq(parent=score)
    for note in ast['notes']:
        add_note(note, notes)
    add_double_barline(notes)
    
    print(header.ly(dom.Printer()))
    print(score.ly(dom.Printer()))


# class MyTransformer(Transformer):
#     def duration(self, args):
#         n = int(args[0].value)
#         return ('<duration>', duration2int(n))
    
#     def title(self, args):
#         t = ' '.join([word.value for word in args])
#         return ('<title>', t)

#     def pitch(self, args):
#         # note: need to handle accidentals
#         n = pitch2int(args[0].value[0])
#         return ('<pitch>', n)

#     def octave(self, args):
#         n = int(args[0].value)
#         return ('<octave>', octave2int(n))

#     def note(self, args):
#         return ('<note>', *args)
        



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 transpiler.py musicodeFile")
        exit(1)

    grammar_file = open("grammar.lark", "r")
    parser = lark.Lark(grammar_file.read())
    
    musicode_file = open(sys.argv[1], "r")
    tree = parser.parse(musicode_file.read())
    # print(MyTransformer().transform(tree))
    # return

    score_info = extract_score_info(tree)

    print_score(score_info)

if __name__ == '__main__':
    main()


# 'system' function in 'os' package runs something as if it's running from the command line
# also 'popen' and 'call' functions
# module called 'subprocess'
