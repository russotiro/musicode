(title "My Title")
(subtitle "My Subtitle")
(composer "Me")
(instruments flute clarinet)

(tempo "Allegro non troppo" /1 = 6400 m19)

(part flute "Flute"
    (staff
        (notes (clef treble) (time 4/4) (key C) (expression "dolce")
            C4[staccato tenuto mf beamEnd stemUp]/4 D4.[stemUp]^/4 E4/4 F4/4
            (time common)
            r/4 R/4 R[beamEnd]/4 r/4
            (tuplet 3/2 r/4 G4/4 G4/4) C4/4 C4/4
            (barline final)
            (symbol segno)
            (D.S. al Coda)
            (toCoda)
            (D.C. al fine)
        )
    )
)