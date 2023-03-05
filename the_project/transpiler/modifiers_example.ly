\version "2.23.0"
\header {
    title = "Modifiers Galooza"
    subtitle = "Lots of Modifiers"
    composer = "Me"
}

DSfine = {
  \once \override Score.RehearsalMark #'break-visibility = #'#(#t #t #f)
  \mark \markup { \small "D.S. al fine" }
}

DS = {
  \once \override Score.RehearsalMark #'break-visibility = #'#(#t #t #f)
  \mark \markup { \small "D.S." }
}

DCfine = {
  \once \override Score.RehearsalMark #'break-visibility = #'#(#t #t #f)
  \mark \markup { \small "D.C. al fine" }
}

DCcoda = {
  \once \override Score.RehearsalMark #'break-visibility = #'#(#t #t #f)
  \mark \markup { \small "D.C. al coda" }
}

DScoda = {
  \once \override Score.RehearsalMark #'break-visibility = #'#(#t #t #f)
  \mark \markup { \small "D.S. al coda" }
}

Fine = {
  \once \override Score.RehearsalMark #'break-visibility = #'#(#t #t #f)
  \mark \markup { \small \italic "fine" }
}

GotoCoda = {
  \once \override Score.RehearsalMark #'break-visibility = #'#(#t #t #f)
  \mark \markup { \small "to Coda" \small \musicglyph #"scripts.coda" }
}

Coda = {
  \once \override Score.RehearsalMark #'break-visibility = #'#(#f #t #t)
  \mark \markup { \small \musicglyph #"scripts.coda" }
}

Segno = {
  \once \override Score.RehearsalMark #'break-visibility = #'#(#f #t #t)
  \mark \markup { \small \musicglyph #"scripts.segno" }
}

<<
\new Staff \with {
    instrumentName = "Soprano "
    shortInstrumentName = "Sop. "
} {
    { \clef treble \numericTimeSignature
\time 4/4 \key g \major \stemUp d''8[ \( ( \sustainOn \> \stemNeutral \stemUp 
\set stemLeftBeamCount = #2
 
\set stemRightBeamCount = #3
 e''8  \staccato \tenuto \accent \marcato ~ \glissando \) ) \( ( :16 \trill \sustainOff\sustainOn -1 -2 -3 -4 -5 \fff \! \cresc \stemNeutral \stemUp e''8] \) ) \sustainOff \! \stemNeutral fis''8\noBeam g''2 \bar "|." }
}
>>
