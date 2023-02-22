#!/usr/bin/env python3

import mc_ast

def test_note():
    note = mc_ast.Note("G", "4", mc_ast.Modifiers([]), "4").render()
    assert(note == "g'4")
    note = mc_ast.Note("C", "6", mc_ast.Modifiers([]), "2").render()
    assert(note == "c'''2")
    note = mc_ast.Note("A", "1", mc_ast.Modifiers([]), "16").render()
    assert(note == "a,,16")
    note = mc_ast.Note("A", "3", mc_ast.Modifiers([]), "32").render()
    assert(note == "a32")
    note = mc_ast.Note("G#", "4", mc_ast.Modifiers([]), "4").render()
    assert(note == "gis'4")
    note = mc_ast.Note("Bb", "4", mc_ast.Modifiers([]), "4").render()
    assert(note == "bes'4")
    note = mc_ast.Note("C", "6", mc_ast.Modifiers([]), "2.").render()
    assert(note == "c'''2.")


def test_modifiers():
    note = mc_ast.Note("G", "4", mc_ast.Modifiers(["stemUp", "accent", "beamNone"]), "4").render()
    assert(note == "g'4\\stemUp \\accent \\noBeam")
    note = mc_ast.Note("C", "6", mc_ast.Modifiers(["beamBeginUp", "ff"]), "2").render()
    assert(note == "c'''2^[ \\ff")
    note = mc_ast.Note("A", "1", mc_ast.Modifiers(["tremolo16", "crescTextBegin"]), "16").render()
    assert(note == "a,,16:16 \\cresc")
    note = mc_ast.Note("A", "3", mc_ast.Modifiers(["beamEnd", "crescendoTextEnd"]), "32").render()
    assert(note == "a32] \\!")
    note = mc_ast.Note("G", "4", mc_ast.Modifiers(["beamStemLeftCount4"]), "4").render()
    assert(note == "g'4\n\\set stemLeftBeamCount = #4\n")
    note = mc_ast.Note("C", "6", mc_ast.Modifiers(["pedalBegin"]), "2").render()
    assert(note == "c'''2\\sustainOn")
    note = mc_ast.Note("A", "1", mc_ast.Modifiers(["pedalLift"]), "16").render()
    assert(note == "a,,16\\sustainOff\\sustainOn")
    note = mc_ast.Note("A", "3", mc_ast.Modifiers(["pedalEnd"]), "32").render()
    assert(note == "a32\\sustainOff")

def test_rest():
    rest = mc_ast.Rest([], "4").render()
    assert(rest == "r4")
    rest = mc_ast.Rest(["beamBegin"], "8").render()
    assert(rest == "r8[")
    rest = mc_ast.Rest(["beamEnd"], "8").render() 
    assert(rest == "r8]")
    rest = mc_ast.Rest(["beamBeginUp"], "8").render() 
    assert(rest == "r8^[")
    rest = mc_ast.Rest(["beamEnd"], "8").render() 
    assert(rest == "r8]")
    rest = mc_ast.Rest([], "4").render()
    assert(rest == "r4")

def test_chord():
    chord = mc_ast.Chord([mc_ast.Note("C", "4"), mc_ast.Note("E", "4"), mc_ast.Note("G", "4")], mc_ast.Modifiers([]), "4").render()
    assert(chord == "<c'e'g'>4")
    chord = mc_ast.Chord([mc_ast.Note("D", "4"), mc_ast.Note("F#", "4"), mc_ast.Note("A", "4")], mc_ast.Modifiers(["staccato", "ff", "marcato", "tremolo32", "beamNone"]), "4.").render()
    assert(chord == "<d'fis'a'>4.\\staccato \\ff \\marcato :32 \\noBeam")

def test_symbol():
    segno = mc_ast.Symbol('segno').render()
    assert(segno == '\\Segno')

def test_text():
    # Test road map cases 
    text = mc_ast.Text('road_map', 'd.c. al fine').render()
    assert(text == '\\DCfine')
    text = mc_ast.Text('road_map', 'd.s. al fine').render()
    assert(text == '\\DSfine')
    text = mc_ast.Text('road_map', 'd.c. al coda').render()
    assert(text == '\\DCcoda')
    text = mc_ast.Text('road_map', 'd.s. al coda').render()
    assert(text == '\\DScoda')
    text = mc_ast.Text('road_map', 'toCoda').render()
    assert(text == '\\GotoCoda')

    # Test expression text 
    text = mc_ast.Text('expression', 'dolce').render()
    assert(text == '\\tweak direction #DOWN \\mark \\markup { \\small \\italic "dolce" }')

    # Test technique text 
    text = mc_ast.Text('technique', 'straight mute').render() 
    assert(text == '\\mark "straight mute"')

test_note()
test_modifiers()
test_rest()
test_chord()
test_symbol()
test_text()
