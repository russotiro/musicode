( title "My Title")
( subtitle "Jingle Bells")
(composer "Me")
(instruments flute)

(clef treble m1 flute)
(time common m1)
(key Dbm m1 flute)
(tempo "Allegro non troppo" /4 = 120)
(tempo /4 = 122 m4)

(part flute "Flute"
    (notes
        E4[staccato stemDown]/4 E4.^/4 (clef bass) (key DbM) (notes r/2 \{E4/4 {D4/4 C4_E4_G4[staccato marcato stemUp ff]/2} E4/4\} G4/4 C4/4. D4/8 E4/1
        (voices
            (notes F4/4 F4/4 F4/4. F4/8)
            (notes C4/2 C4/2))
        (cresc (tuplet 3/2 (dimText F4/4 E4/4) E4[tie]/4) E4/4 E4/4)
        (pedal E4/4 D4/4 D4[lift]/4 E4/4 D4/2) G4/2
        (clef bass) E4/4 E4/4 E4/2 E4/4 E4/4 E4/2))
