(title "Silent Night")
(subtitle "A Christmas Song")
(composer "Joseph Mohr")

(part "Trumpet"
    (staff (key A) (clef treble)
        (notes r/2. r/2. E4/4. (tuplet 3/2 F#4[stemDown]/16 F#4[stemDown]/16 F#4[stemDown]/16) E4/4)
        (notes (grace (notes D4/8) C#4/2.))
        (notes B4/2 B4./4 G#4[trill]/2. A4/2 A4/4 E4/2.)
        (barline final)))

(group begin)
(part "Viola"
    (staff (time 3/4) (tempo /4 = 90) (key A) (clef alto)
        (notes C#4_E4/4. F#4/8 E4/4 E3_C#4/2. r/2. r/2.)
        (notes B4/2 B4./4 G#4/2. A4/2 A4/4 E4/2.)))

(part "Violoncello"
    (staff (key A) (clef bass)
        (notes C#4/4. D4/8 C#4/4 A3/2. C#4/4. D4/8 C#4/4 A3/2.)
        (notes G#4/2 G#4./4 E4/2. E4/2 E4/4 C#4/2.))
    (staff (key A) (clef bass)
        (notes A2/2. A2/2. A2/2. A2/2. E3/2. E3/2. A2/2. C#3/2.)))
(group end)