\version "2.23.0"
\header {
    title = "My Title"
    subtitle = "My Subtitle"
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
    instrumentName = "Flute "
    shortInstrumentName = "Fl. "
} {
    \tempo "Allegro non troppo" 4 = 120
{ \clef treble \numericTimeSignature
\time 4/4 \key c \major \tweak direction #DOWN \mark \markup { \small \italic "dolce" } \stemUp c'4\staccato \tenuto \mf \stemNeutral \stemUp d'4\staccato \marcato \stemNeutral e'4 f'4 \defaultTimeSignature
\time 4/4 r4 r8 g'8[ r8] r8 r4 \tuplet 3/2 { r4 g'4 g'4 } c'4 c'4 \bar "|." \Segno \DScoda \GotoCoda \DCfine }
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
        { <c'g'>4 }
}
    \new Staff {
        { e4 }
}
>>

>>
