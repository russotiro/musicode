#!/usr/bin/env python3

import mc_ast


def assert_equal(p1, p2):
    print('%r == %r...' % (p1, p2), end='')
    assert(p1 == p2)
    print("\t\tOK")


note1 = mc_ast.Note("G", "4", mc_ast.Modifiers([]), "4")
note2 = mc_ast.Note("C", "6", mc_ast.Modifiers([]), "2")
note3 = mc_ast.Note("A", "1", mc_ast.Modifiers([]), "16")
note4 = mc_ast.Note("G#", "4", mc_ast.Modifiers([]), "4")
note5 = mc_ast.Note("A", "4", mc_ast.Modifiers([]), "2")
note6 = mc_ast.Note("C", "5", mc_ast.Modifiers([]), "2")
note7 = mc_ast.Note("A", "4", mc_ast.Modifiers([]), "2.")
note8 = mc_ast.Note("C", "5", mc_ast.Modifiers([]), "2.")

def reset_notes():
    # Revert global notes back to original values in case they got 
    # modified (e.g. in the case of tremolo)
    global note1, note2, note3, note4, note5, note6, note7, note8
    note1 = mc_ast.Note("G", "4", mc_ast.Modifiers([]), "4")
    note2 = mc_ast.Note("C", "6", mc_ast.Modifiers([]), "2")
    note3 = mc_ast.Note("A", "1", mc_ast.Modifiers([]), "16")
    note4 = mc_ast.Note("G#", "4", mc_ast.Modifiers([]), "4")
    note5 = mc_ast.Note("A", "4", mc_ast.Modifiers([]), "2")
    note6 = mc_ast.Note("C", "5", mc_ast.Modifiers([]), "2")
    note7 = mc_ast.Note("A", "4", mc_ast.Modifiers([]), "2.")
    note8 = mc_ast.Note("C", "5", mc_ast.Modifiers([]), "2.")

metadata1 = {
    'title': 'Jingle Bells',
    'subtitle': '2000 version',
    'composer': 'John Doe'
}


def test_note():
    note = mc_ast.Note("G", "4", mc_ast.Modifiers([]), "4").render()
    assert_equal(note, "g'4")
    note = mc_ast.Note("C", "6", mc_ast.Modifiers([]), "2").render()
    assert_equal(note, "c'''2")
    note = mc_ast.Note("A", "1", mc_ast.Modifiers([]), "16").render()
    assert_equal(note, "a,,16")
    note = mc_ast.Note("A", "3", mc_ast.Modifiers([]), "32").render()
    assert_equal(note, "a32")
    note = mc_ast.Note("G#", "4", mc_ast.Modifiers([]), "4").render()
    assert_equal(note, "gis'4")
    note = mc_ast.Note("Bb", "4", mc_ast.Modifiers([]), "4").render()
    assert_equal(note, "bes'4")
    note = mc_ast.Note("C", "6", mc_ast.Modifiers([]), "2.").render()
    assert_equal(note, "c'''2.")

def test_modifiers_sort():
    modifiers = mc_ast.Modifiers(["beamStemLeftCount5", "beamStemRightCount5", "beamStemRightCount4", "stemUp", "staccato",
                                  "beamStemLeftCount3", "beamStemRightCount0", "beamStemLeftCount4", "beamStemLeftCount1",
                                  "beamStemLeftCount0", "beamStemRightCount1", "stemDown", "beamStemLeftCount2",
                                  "beamStemRightCount2", "beamStemRightCount3", "ppp"]).render_pre_event()
    assert_equal(modifiers, "\\stemUp \\stemDown \n\\set stemLeftBeamCount = #0\n \n\\set stemLeftBeamCount = #1\n "
                            "\n\\set stemLeftBeamCount = #2\n \n\\set stemLeftBeamCount = #3\n \n\\set stemLeftBeamCount = #4\n "
                            "\n\\set stemLeftBeamCount = #5\n \n\\set stemRightBeamCount = #0\n \n\\set stemRightBeamCount = #1\n "
                            "\n\\set stemRightBeamCount = #2\n \n\\set stemRightBeamCount = #3\n \n\\set stemRightBeamCount = #4\n "
                            "\n\\set stemRightBeamCount = #5\n ")
    
    modifiers = mc_ast.Modifiers(["fermata", "trill", "crescEnd", "gliss", "beamStemLeftCount3", "beamStemRightCount5", "pianoFinger3",
                                  "ppp", "crescBegin", "beamNone", "tie", "beamStemRightCount3", "slurEnd", "stemUp", "beamStemLeftCount4",
                                  "pianoFinger2", "pianoFinger4", "beamBegin", "tenuto", "pedalBegin", "tremolo8", "beamStemLeftCount2",
                                  "pianoFinger5", "pianoFinger1", "beamStemLeftCount0", "beamStemLeftCount1", "phrasingSlurBegin", "slurBegin",
                                  "marcato", "accent", "phrasingSlurEnd", "beamStemLeftCount5", "beamStemRightCount4", "staccato", 
                                  "beamStemRightCount0", "beamStemRightCount2", "beamStemRightCount1"]).render_post_event()
    assert_equal(modifiers, "\\noBeam [             \\staccato \\tenuto \\accent \\marcato \\fermata ~ \\glissando \) ) \( ( :8 \\trill "
                            "\\sustainOn -1 -2 -3 -4 -5 \\ppp \! \< \\stemNeutral")

def test_modifiers():
    note = mc_ast.Note("G", "4", mc_ast.Modifiers(["stemUp", "accent", "beamNone"]), "4").render()
    assert_equal(note, "\\stemUp g'4\\noBeam \\accent \\stemNeutral")
    note = mc_ast.Note("C", "6", mc_ast.Modifiers(["beamBeginUp", "ff"]), "2").render()
    assert_equal(note, "c'''2^[ \\ff")
    note = mc_ast.Note("A", "1", mc_ast.Modifiers(["tremolo16", "crescTextBegin"]), "16").render()
    assert_equal(note, "a,,16:16 \\cresc")
    note = mc_ast.Note("A", "3", mc_ast.Modifiers(["beamEnd", "crescendoTextEnd"]), "32").render()
    assert_equal(note, "a32] \\!")
    note = mc_ast.Note("G", "4", mc_ast.Modifiers(["beamStemLeftCount4"]), "4").render()
    assert_equal(note, "\n\\set stemLeftBeamCount = #4\n g'4")
    note = mc_ast.Note("C", "6", mc_ast.Modifiers(["pedalBegin"]), "2").render()
    assert_equal(note, "c'''2\\sustainOn")
    note = mc_ast.Note("A", "1", mc_ast.Modifiers(["pedalLift"]), "16").render()
    assert_equal(note, "a,,16\\sustainOff\\sustainOn")
    note = mc_ast.Note("A", "3", mc_ast.Modifiers(["pedalEnd"]), "32").render()
    assert_equal(note, "a32\\sustainOff")

def test_rest():
    rest = mc_ast.Rest([], "4").render()
    assert_equal(rest, "r4")
    rest = mc_ast.Rest(["beamBegin"], "8").render()
    assert_equal(rest, "r8[")
    rest = mc_ast.Rest(["beamEnd"], "8").render() 
    assert_equal(rest, "r8]")
    rest = mc_ast.Rest(["beamBeginUp"], "8").render() 
    assert_equal(rest, "r8^[")
    rest = mc_ast.Rest(["beamEnd"], "8").render() 
    assert_equal(rest, "r8]")
    rest = mc_ast.Rest([], "4").render()
    assert_equal(rest, "r4")

def test_chord():
    chord = mc_ast.Chord([mc_ast.Note("C", "4"), mc_ast.Note("E", "4"), mc_ast.Note("G", "4")], mc_ast.Modifiers([]), "4").render()
    assert_equal(chord, "<c'e'g'>4")
    chord = mc_ast.Chord([mc_ast.Note("D", "4"), mc_ast.Note("F#", "4"), mc_ast.Note("A", "4")], mc_ast.Modifiers(["staccato", "ff", "marcato", "tremolo32", "beamNone"]), "4.").render()
    assert_equal(chord, "<d'fis'a'>4.\\noBeam \\staccato \\marcato :32 \\ff")

def test_symbol():
    segno = mc_ast.Symbol('segno').render()
    assert_equal(segno, '\\Segno')

def test_text():
    # Test road map cases 
    text = mc_ast.Text('road_map', 'd.c. al fine').render()
    assert_equal(text, '\\DCfine')
    text = mc_ast.Text('road_map', 'd.s. al fine').render()
    assert_equal(text, '\\DSfine')
    text = mc_ast.Text('road_map', 'd.c. al coda').render()
    assert_equal(text, '\\DCcoda')
    text = mc_ast.Text('road_map', 'd.s. al coda').render()
    assert_equal(text, '\\DScoda')
    text = mc_ast.Text('road_map', 'tocoda').render()
    assert_equal(text, '\\GotoCoda')

    # Test expression text 
    text = mc_ast.Text('expression', 'dolce').render()
    assert_equal(text, '\\tweak direction #DOWN \\mark \\markup { \\small \\italic "dolce" }')

    # Test technique text 
    text = mc_ast.Text('technique', 'straight mute').render() 
    assert_equal(text, '\\mark \\markup \\small "straight mute"')


def test_barline():
    text = mc_ast.Barline('single').render()
    assert_equal(text, '\\bar "|"')
    text = mc_ast.Barline('double').render()
    assert_equal(text, '\\bar "||"')
    text = mc_ast.Barline('repeatBegin').render()
    assert_equal(text, '\\bar ".|:"')
    text = mc_ast.Barline('repeatEnd').render()
    assert_equal(text, '\\bar ":|."')
    text = mc_ast.Barline('final').render()
    assert_equal(text, '\\bar "|."')
    text = mc_ast.Barline('dotted').render()
    assert_equal(text, '\\bar ";"')


def test_tempo():
    text = mc_ast.Tempo('asiago', ['4', '120']).render()
    assert_equal(text, '\\tempo "asiago" 4 = 120')
    text = mc_ast.Tempo('', ['4', '120']).render()
    assert_equal(text, '\\tempo 4 = 120')
    text = mc_ast.Tempo('asiago', []).render()
    assert_equal(text, '\\tempo "asiago"')

clef1 = mc_ast.Clef('bass')

def test_clef():
    assert_equal(clef1.render(), "\\clef bass")
    clef = mc_ast.Clef('alto').render()
    assert_equal(clef, "\\clef alto")


def test_key():
    key = mc_ast.Key("Cbm").render()
    assert_equal(key, "\\key ces \\minor")
    key = mc_ast.Key("f#M").render()
    assert_equal(key, "\\key fis \\major")
    key = mc_ast.Key("g").render()
    assert_equal(key, "\\key g \\major")


def test_time():
    time = mc_ast.Time("common").render()
    assert_equal(time, "\\defaultTimeSignature\n\\time 4/4")
    time = mc_ast.Time("cut").render()
    assert_equal(time, "\\defaultTimeSignature\n\\time 2/2")
    time = mc_ast.Time(['7','8']).render()
    assert_equal(time, "\\numericTimeSignature\n\\time 7/8")


def test_tuplet_basic():
    tup = mc_ast.Tuplet("3/2", [note1, note2, note3]).render()
    assert_equal(tup, "\\tuplet 3/2 { g'4 c'''2 a,,16 }")


def test_grace_basic():
    grace = mc_ast.Grace("noSlash", mc_ast.Notes([note1, note2]), note3).render()
    assert_equal(grace, "\\grace { g'4 c'''2 } a,,16")
    grace = mc_ast.Grace("slash", mc_ast.Notes([note1, note2]), note3).render()
    assert_equal(grace, "\\slashedGrace { g'4 c'''2 } a,,16")


def test_tremolo():
    trem = mc_ast.Tremolo("1", note1, note4).render()
    assert_equal(trem, "\\repeat tremolo 1 { g'8 gis'8 }")
    trem = mc_ast.Tremolo("3", note5, note6).render()
    assert_equal(trem, "\\repeat tremolo 8 { a'32 c''32 }")
    trem = mc_ast.Tremolo("2", note7, note8).render()
    assert_equal(trem, "\\repeat tremolo 6 { a'16 c''16 }")
    reset_notes() # Reset globals since tremolo modifies them

def test_header():
    start = mc_ast.Start(metadata1).render_header()
    assert_equal(start, "\\header {\n    title = \"Jingle Bells\"\n    subtitle = \"2000 version\"\n    composer = \"John Doe\"\n}\n")

def test_notes():
    notes = mc_ast.Notes([note1, note2, note3, note4]).render()
    assert_equal(notes, "{ g'4 c'''2 a,,16 gis'4 }")
    notes = mc_ast.Notes([mc_ast.Clef("bass"), mc_ast.Time("common"), mc_ast.Note("C", "4", mc_ast.Modifiers(["staccato"]), "1")]).render()
    assert_equal(notes, """{ \\clef bass \\defaultTimeSignature
\\time 4/4 c'1\\staccato }""")

def test_voice():
    voice = mc_ast.Voice(mc_ast.Notes([note1, note2, note3, note4])).render(0)
    assert_equal(voice, "\\new Voice { \\voiceOne g'4 c'''2 a,,16 gis'4 }")
    voice = mc_ast.Voice(mc_ast.Notes([note1, note2, note3, note4])).render(3)
    assert_equal(voice, "\\new Voice { \\voiceFour g'4 c'''2 a,,16 gis'4 }")

def test_voices():
    voices = mc_ast.Voices([mc_ast.Voice(mc_ast.Notes([note1, note2, note3, note4])), \
                            mc_ast.Voice(mc_ast.Notes([note5, note6, note7, note8]))]).render()
    assert_equal(voices, """<<
\\new Voice { \\voiceOne g'4 c'''2 a,,16 gis'4 }
\\new Voice { \\voiceTwo a'2 c''2 a'2. c''2. }
>> \\oneVoice
""")


def test_coda():
    notes1 = mc_ast.Notes([note1, note2, note3, note4])
    notes2 = mc_ast.Notes([note1, note2, note3, note3])
    coda   = mc_ast.Coda([notes1, notes2])
    assert_equal(coda.render(), "\\Coda { g'4 c'''2 a,,16 gis'4 } { g'4 c'''2 a,,16 a,,16 }")
    

def test_endings():
    notes1 = mc_ast.Notes([note1, note2, note3, note4])
    notes2 = mc_ast.Notes([note1, note2, note3, note3])
    ending = mc_ast.Ending([6, 7, 9], [notes1, notes2])
    assert_equal(ending.render(), "\\volta 6,7,9 {  { g'4 c'''2 a,,16 gis'4 } { g'4 c'''2 a,,16 a,,16 } }\n")


def test_staffs():
    staff = mc_ast.Staff([mc_ast.Notes([note1, note2, clef1, note3]), mc_ast.Coda([mc_ast.Notes([note1])])])
    assert_equal(staff.render(), "{ g'4 c'''2 \\clef bass a,,16 }\n\\Coda { g'4 }")


def test_parts():
    staff = mc_ast.Staff([mc_ast.Notes([note1, note2, clef1, note3]), mc_ast.Coda([mc_ast.Notes([note1])])])
    flute = mc_ast.Part("Flute", [staff]).render()
    assert_equal(flute, '\\new Staff \\with {\n    instrumentName = "Flute "\n    shortInstrumentName = "Fl. "\n} {\n    ' + staff.render() + '\n}')

    piano = mc_ast.Part("Piano", [staff, staff]).render()
    assert_equal(piano, '\\new PianoStaff \\with {\n    instrumentName = "Piano "\n    shortInstrumentName = "Pno. "\n} <<\n    \\new Staff {\n        ' + staff.render() + '\n}\n    \\new Staff {\n        ' + staff.render() + '\n}\n>>\n')

    cello = mc_ast.Part("Cello", [staff, staff]).render()
    the_string = '\\new StaffGroup \\with {\n    instrumentName = "Cello "\n    shortInstrumentName = "Vc. "\n} { <<\n\\set StaffGroup.systemStartDelimiter = #\'SystemStartSquare\n    \\new Staff {\n        ' + staff.render() + '\n}\n    \\new Staff {\n        ' + staff.render() + '\n}\n>> }\n'
    assert_equal(cello, the_string)


test_note()
test_modifiers_sort()
test_modifiers()
test_rest()
test_chord()
test_symbol()
test_text()
test_barline()
test_tempo()
test_clef()
test_key()
test_time()
test_tuplet_basic()
test_grace_basic()
test_tremolo()
test_header()
test_notes()
test_voice()
test_voices()
test_coda()
test_endings()
test_staffs()
test_parts()
