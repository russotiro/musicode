(title "My Title")
(subtitle "My Subtitle")
(composer "Me")
(instruments flute clarinet)

(tempo "Allegro non troppo")
(tempo /4 = 6400)
(tempo "Allegro non troppo" /4 = 180)
(tempo "Allegro non troppo" m19)
(tempo /1 = 6400 m19)
(tempo "Allegro non troppo" /1 = 6400 m19)

(part flute "Flute"
    (staff
        (notes (clef treble) (time 4/4) (key C)
            C4[staccato tenuto mf beamEnd stemUp]/4 D4.^/4 E4/4 F4/4
            r/4 R/4 R[beamEnd]/4 r/4
        )
    )
)