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


# again, using naive AST 
# key signature and time signature not implemented 
hcb_ast = {
    'title': 'Hot Cross Buns',
    'composer': 'Unknown',
    'notes': [
        {
            'pitch' : 'E',
            'octave': 4,
            'duration': 4
        },
        {
            'pitch': 'D',
            'octave': 4,
            'duration': 4
        },
        {
            'pitch': 'C',
            'octave': 4,
            'duration': 2
        },
        {
            'pitch' : 'E',
            'octave': 4,
            'duration': 4
        },
        {
            'pitch': 'D',
            'octave': 4,
            'duration': 4
        },
        {
            'pitch': 'C',
            'octave': 4,
            'duration': 2
        },
        {
            'pitch': 'C',
            'octave': 4,
            'duration': 8
        },
        {
            'pitch': 'C',
            'octave': 4,
            'duration': 8
        },
        {
            'pitch': 'C',
            'octave': 4,
            'duration': 8
        },
        {
            'pitch': 'C',
            'octave': 4,
            'duration': 8
        },
        {
            'pitch': 'D',
            'octave': 4,
            'duration': 8
        },
        {
            'pitch': 'D',
            'octave': 4,
            'duration': 8
        },
        {
            'pitch': 'D',
            'octave': 4,
            'duration': 8
        },
        {
            'pitch': 'D',
            'octave': 4,
            'duration': 8
        },
        {
            'pitch' : 'E',
            'octave': 4,
            'duration': 4
        },
        {
            'pitch': 'D',
            'octave': 4,
            'duration': 4
        },
        {
            'pitch': 'C',
            'octave': 4,
            'duration': 2
        }
    ]
}

print_score(hcb_ast)


