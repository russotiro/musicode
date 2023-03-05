(title "Modifiers Galooza")
(subtitle "Lots of Modifiers")
(composer "Me")

(part "Soprano"
    (staff
        (notes (clef treble) (time 4/4) (key G)
            D5[stemUp phrasingSlurBegin slurBegin beamBegin pedalBegin dimBegin]/8
            E5[stemUp gliss slurBegin slurEnd phrasingSlurBegin phrasingSlurEnd tremolo16 
               trill pedalLift pianoFinger1 pianoFinger2 pianoFinger3 pianoFinger4 
               pianoFinger5 fff dimEnd crescTextBegin beamStemLeftCount2 beamStemRightCount3].^_>~/8
            E5[stemUp slurEnd pedalEnd phrasingSlurEnd crescTextEnd beamEnd]/8
            F#5[beamNone]/8
            G5/2
            (barline final)
        )
    )
)