\version "2.24.1"
\header {
    title = ""
    subtitle = ""
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
\new Staff \with {
    instrumentName = "Alto "
    shortInstrumentName = "Alto "
    midiInstrument = "alto"
} {
    { c'4 d'4 e'4 f'4 }
\set Score.repeatCommands = #'((volta "1, 3"))
 { g'4 f'4 e'4 d'4 }
\set Score.repeatCommands = #'((volta #f))

\bar ":|."
\set Score.repeatCommands = #'((volta "2, 4"))
 <<
\new Voice { \voiceOne g'4 f'4 e'4 d'4 }
\new Voice { \voiceTwo g2 a4 b4 }
>> \oneVoice

\set Score.repeatCommands = #'((volta #f))

\bar ":|."
\set Score.repeatCommands = #'((volta "5"))
 { c'1 }
\set Score.repeatCommands = #'((volta #f))

\bar "|."
}

>>
