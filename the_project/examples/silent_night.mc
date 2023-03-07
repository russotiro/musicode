(title "Silent Night")
(subtitle "A Christmas Song")
(composer "Joseph Mohr")

(part "Trumpet"
    (staff (key A) (clef treble)
        (notes E4/4. F#4/8 E4/4 C#4/2. E4/4. F#4/8 E4/4) (ending 1 (notes C#4/2.))
        (ending 2 (notes F#4/2.))
        (notes B4/2 B4/4 G#4/2. A4/2 A4/4 E4/2.)))

(group begin)
(part "Viola"
    (staff (time 3/4) (tempo /4 = 90) (key A) (clef alto)
        (notes E4/4. F#4/8 E4/4 C#4/2. E4/4. F#4/8 E4/4) (ending 1 (notes C#4/2.))
        (barline repeatEnd)
        (ending 2 (notes D#4/2.))
        (notes B4/2 B4/4 G#4/2. A4/2 A4/4 E4/2.)))

(part "Violoncello"
    (staff (key A) (clef bass)
        (notes C#4/4. D4/8 C#4/4 A3/2. C#4/4. D4/8 C#4/4) (ending 1 (notes A3/2.))
        (ending 2 (notes B3/2.))
        (notes G#4/2 G#4/4 E4/2. E4/2 E4/4 C#4/2.))
    (staff (key A) (clef bass)
        (notes A2/2. A2/2. A2/2.) (ending 1 (notes A2/2.)) (ending 2 (notes A2/2.))
        (notes E3/2. E3/2. A2/2. C#3/2.)))
(group end)