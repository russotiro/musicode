\version "2.24.1"
\header {
    title = "My Title"
    subtitle = "My Subtitle"
    composer = "Me"
}

DSfine = {
  \once \override Score.RehearsalMark #'break-visibility = #'#(#t #t #f)
  \once \override Score.RehearsalMark.self-alignment-X = #RIGHT
  \mark \markup { \small "D.S. al fine" }
}

DCfine = {
  \once \override Score.RehearsalMark #'break-visibility = #'#(#t #t #f)
  \once \override Score.RehearsalMark.self-alignment-X = #RIGHT
  \mark \markup { \small "D.C. al fine" }
}

DCcoda = {
  \once \override Score.RehearsalMark #'break-visibility = #'#(#t #t #f)
  \once \override Score.RehearsalMark.self-alignment-X = #RIGHT
  \mark \markup { \small "D.C. al coda" }
}

DScoda = {
  \once \override Score.RehearsalMark #'break-visibility = #'#(#t #t #f)
  \once \override Score.RehearsalMark.self-alignment-X = #RIGHT
  \mark \markup { \small "D.S. al coda" }
}

Fine = {
  \once \override Score.RehearsalMark #'break-visibility = #'#(#t #t #f)
  \mark \markup { \small \italic "fine" }
}

GotoCoda = {
  \once \override Score.RehearsalMark #'break-visibility = #'#(#t #t #f)
  \once \override Score.RehearsalMark.self-alignment-X = #RIGHT
  \mark \markup { \small "To Coda" \raise #0.5 \smaller \musicglyph #"scripts.coda" }
}

Coda = {
  \once \override Score.RehearsalMark #'break-visibility = #'#(#f #t #t)
  \mark \markup { " " \musicglyph #"scripts.coda" \lower #0.9 "Coda" }
}

Segno = {
  \once \override Score.RehearsalMark #'break-visibility = #'#(#f #t #t)
  \mark \markup { \small \musicglyph #"scripts.segno" }
}

\paper { left-margin = 0.75\in }

<<
\new Staff \with {
    instrumentName = "Flute "
    shortInstrumentName = "Fl. "
} {
    \tempo "Allegro non troppo" 4 = 120
{ \clef treble \numericTimeSignature
\time 4/4 \key c \major \tweak direction #DOWN \mark \markup { \small \italic "dolce" } \stemUp c'4\staccato \tenuto \mf \stemNeutral \stemUp d'4\staccato \marcato \stemNeutral e'4 f'4 \defaultTimeSignature
\time 4/4 r4 R8 g'8[ R8] r8 r4 \tuplet 3/2 { r4 g'4 g'4 } c'4 c'4 \bar "|." \Segno \DScoda \GotoCoda \DCfine }
}
\new Staff \with {
    instrumentName = "Clarinet "
    shortInstrumentName = "Cl. "
} {
    { g'4 }
}
\new PianoStaff \with {
    instrumentName = "Piano "
    shortInstrumentName = "Pno. "
} <<
    \new Staff {
        { <c' g' >4 }
}
    \new Staff {
        { e4 }
}
>>


>>