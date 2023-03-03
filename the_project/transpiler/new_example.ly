\version "2.23.0"
\header {
    title = "whats up"
    subtitle = ""
    composer = ""
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
    instrumentName = "Piano "
    shortInstrumentName = "Pno. "
} {
    \tweak direction #DOWN \mark \markup { \small \italic "dolce" }
\tempo 4 = 120
{ \slashedGrace { g16 a16 b16 } \repeat tremolo 2 { c'16 d'16 } e'4 f'4 g'4 }
\Segno
{ c'4 d'4 e'4 f'4 }
\volta 1 {  { g'4\trill a'4:8 b'4 c''4 } }

\bar ":|."
\volta 2 {  { \slashedGrace { e'8 } f'4 e'4 d'4 c'4 } }

{ c'4 d'4 e'4 f'4 }
\bar "|."
\mark \markup \small "straight mute"
{ c'4 d'4 e'4 f'4 }
{ c'8 d'8] e'8 f'8 g'8 a'8] b'8 c''8 }
\DSfine
}
>>