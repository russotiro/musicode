\version "2.24.1"
\header {
    title = "whats up"
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
    instrumentName = "Piano "
    shortInstrumentName = "Pno. "
} {
    \tweak direction #DOWN \mark \markup { \small \italic "dolce" }
\tempo 4 = 120
{ \slashedGrace { g16 a16 b16 } \repeat tremolo 2 { c'16 d'16 } e'4 f'4 g'4 }
\Segno
{ c'4 d'4 e'4 f'4 }
\set Score.repeatCommands = #'((volta "1"))
 { g'4\trill a'4:8 b'4 c''4 }
\set Score.repeatCommands = #'((volta #f))

\bar ":|."
\set Score.repeatCommands = #'((volta "2"))
 { \slashedGrace { e'8 } f'4 e'4 d'4 c'4 }
\set Score.repeatCommands = #'((volta #f))

{ c'4 d'4 e'4 f'4 }
\bar "|."
\once \override Score.RehearsalMark.self-alignment-X = #LEFT
\mark \markup \small "straight mute"
{ c'4 d'4 e'4 f'4 }
{ c'8 d'8] e'8 f'8 g'8 a'8] b'8 c''8 }
\DSfine
}

>>