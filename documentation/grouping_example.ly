\version "2.24.1"
\header {
    title = "Concert Bb"
    subtitle = "The Band In Unison"
    composer = ""
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
\new StaffGroup <<
\new Staff \with {
    instrumentName = "Flute "
    shortInstrumentName = "Fl. "
    midiInstrument = "flute"
} {
    \key bes \major
{ bes'1 }
\bar "|."
}
\new Staff \with {
    instrumentName = "Clarinet "
    shortInstrumentName = "Cl. "
    midiInstrument = "clarinet"
} {
    { c'1 }
}
\new Staff \with {
    instrumentName = "Alto Saxophone "
    shortInstrumentName = "A. S. "
    midiInstrument = "alto saxophone"
} {
    \key g \major
{ g'1 }
}
>>
\new StaffGroup <<
\new Staff \with {
    instrumentName = "Trumpet "
    shortInstrumentName = "Tpt. "
    midiInstrument = "trumpet"
} {
    { c'1 }
}
\new Staff \with {
    instrumentName = "Low Brass "
    shortInstrumentName = "L. B. "
    midiInstrument = "low brass"
} {
    \clef bass
\key bes \major
{ bes,1 }
}
>>

>>
