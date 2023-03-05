\version "2.23.0"
\header {
    title = "My Title"
    subtitle = "Jingle Bells"
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
    { \clef treble \defaultTimeSignature
\time 4/4 \key c \major \tempo "Allegro non troppo" 4 = 120 \stemDown e'4\staccato -1 \stemNeutral e'4\staccato \marcato \key ces \minor r2 e'4\( d'4( \stemUp <c'e'g'>2\staccato \marcato ) \ff \stemNeutral e'4\) g'4 c'4. d'8 e'1 }
<<
\new Voice { \voiceOne f'4 f'4 f'4. f'8 }
\new Voice { \voiceTwo c'2\< c'2\! }
>> \oneVoice

{ \tuplet 3/2 { f'4\decresc e'4\! e'4~ } e'4 e'4\! e'4\sustainOn d'4 d'4\sustainOff\sustainOn e'4 d'2\sustainOff g'2 \clef bass e'4 e'4 e'2 e'4 e'4 e'2 }
<<
\new Voice { \voiceOne c'4 d'4 e'4 f'4 }
\new Voice { \voiceTwo g1 }
>> \oneVoice

\volta 1,2 {  { f'4 f'4 } \clef alto { f'4. f'8 f'4 f'4 f'4 f'4 } { f'2 f'2 f'2. f'4 } }

{ f'4 f'4 }
\clef alto
{ f'4. f'8 f'4 f'4 f'4 f'4 }
{ f'2 f'2 f'2. f'4 }
}
\new Staff \with {
    instrumentName = "Clarinet "
    shortInstrumentName = "Cl. "
} {
    { \clef treble \defaultTimeSignature
\time 4/4 \key d \major c'4 c'4 d'4 e'4 \bar "||" e'4 d'4 c'4 b'4 }
\Coda { g'4 }
}
>>
