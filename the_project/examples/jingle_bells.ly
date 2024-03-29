\version "2.24.1"
\header {
    title = "Jingle Bells"
    subtitle = ""
    composer = "James Pierpont"
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

\score {
<<
\new PianoStaff \with {
    instrumentName = "Piano "
    shortInstrumentName = "Pno. "
    midiInstrument = "acoustic grand"
} <<
    \new Staff {
        \clef treble
\key des \major
\defaultTimeSignature
\time 2/2
{ f'4\f f'4 f'2 }
<<
\new Voice { \voiceOne des''2 }
\new Voice { \voiceTwo f'4 f'4 }
>> \oneVoice

{ des''8_[ c''8 bes'8] aes'8\accent }
{ f'4\p \< aes'4 des'4. ees'8 f'1\mf \bar "|." }
}
    \new Staff {
        \clef bass
\key des \major
{ des2.\f aes,4\marcato des,1 des2\p \< ges,4 aes,4 des1\mf }
}
>>

\new Staff \with {
    instrumentName = "Violin "
    shortInstrumentName = "Vln. "
    midiInstrument = "violin"
} {
    \clef treble
\key des \major
{ des''2\f des''4\staccato aes'4\staccato des''2 des''4\staccato aes'4\staccato bes'4\p \< ges'4 c''4 aes'4 aes'1:32 \mf }
}

>>
\midi { }
}
