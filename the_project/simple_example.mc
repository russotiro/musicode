(title "My Title")
(subtitle "My Subtitle")
(composer "Me")

(part "Flute"
    (staff (tempo "Allegro non troppo" /4 = 120)
        (notes (clef treble) (time 4/4) (key C) (expression "dolce")
            C4[staccato tenuto mf stemUp]/4 D4.^[stemUp]/4 E4/4 F4/4
            (time common)
            r/4 R/8 G4[beamBegin]/8 R[beamEnd]/8 r/8 r/4
            (tuplet 3/2 r/4 G4/4 G4/4) C4/4 C4/4
            (barline final)
            (symbol segno)
            (D.S. al Coda)
            (toCoda)
            (D.C. al fine)
        )
    )
)

(part "Clarinet"
    (staff (notes G4/4)))

(part "Piano"
    (staff (notes C4_G4/4))
    (staff (notes E3/4)))