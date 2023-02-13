( title "My Title")
( subtitle "Jingle Bells")
(composer "Me")
(instruments flute clarinet)

(tempo "Allegro non troppo" /4 = 120 m50)

(part flute "Flute"
    (staff
        (notes (clef treble) (time common) (key C)
            E4[staccato stemDown pianoFinger1]/4 E4.^/4 (key Cbm) r/2 E4[phrasingSlurBegin]/4 D4[slurBegin]/4 C4_E4_G4[staccato marcato stemUp ff slurEnd]/2 E4[phrasingSlurEnd]/4 G4/4 C4/4. D4/8 E4/1)
        (voices
            (voice (notes F4/4 F4/4 F4/4. F4/8))
            (voice (notes C4/2 C4[crescendoBegin]/2)))
        (notes
            (tuplet 3/2 F4[dimTextBegin]/4 E4[dimTextEnd]/4 E4[tie]/4) E4/4 E4[crescEnd]/4
            E4[pedalBegin]/4 D4/4 D4[lift]/4 E4/4 D4[pedalEnd]/2 G4/2
            (clef bass) E4/4 E4/4 E4/2 E4/4 E4/4 E4/2)))

(part clarinet "Clarinet"
    (staff (notes (clef treble) (time common) (key D)
        C4/4 C4/4 D4/4 E4/4 (barline double) E4/4 D4/4 C4/4 B4/4)))