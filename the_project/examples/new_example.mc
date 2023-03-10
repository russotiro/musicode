(title "whats up")

(part "Piano"
    (staff
        (expression "dolce") (tempo /4 = 120)
        (notes (grace slash (notes G3/16 A3/16 B3/16) (tremolo 2 C4/4 D4/4)) E4/4 F4/4 G4/4)
        (symbol segno)
        (notes C4/4 D4/4 E4/4 F4/4)
        (ending 1 (notes G4[trill]/4 A4[tremolo8]/4 B4/4 C5/4))
        (barline repeatEnd)
        (ending 2 (notes (grace (notes E4/8) F4/4) E4/4 D4/4 C4/4))
        (notes C4/4 D4/4 E4/4 F4/4)
        (barline final)
        (technique "straight mute")
        (notes C4/4 D4/4 E4/4 F4/4)
        (notes C4/8 D4[beamEnd]/8 E4/8 F4/8 G4/8 A4[beamEnd]/8 B4/8 C5/8)
        (D.S. al fine)
))
