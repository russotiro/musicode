(title "Jingle Bells")
(composer "James Pierpont")

(part "Piano"
    (staff (clef treble) (key Db) (time cut)
        (notes F4[f]/4 F4/4 F4/2)
        (voices
            (voice (notes Db5/2))
            (voice (notes F4/4 F4/4)))
        (notes Db5[beamBeginDown]/8 c5/8 Bb4[beamEnd]/8 Ab4[accent]/8)
        (notes F4[p crescBegin]/4 Ab4/4 Db4/4. Eb4/8 F4[mf]/1 (barline final)))
    (staff (clef bass) (key Db)
        (notes Db3[f]/2. Ab2[marcato]/4 Db2/1
               Db3[p crescBegin]/2 Gb2/4 Ab2/4 Db3[mf]/1)))

(part "Violin"
    (staff (clef treble) (key Db)
        (notes Db5[f]/2 Db5./4 Ab4./4 Db5/2 Db5./4 Ab4./4
               Bb4[p crescBegin]/4 Gb4/4 C5/4 Ab4/4 Ab4[mf tremolo32]/1)))