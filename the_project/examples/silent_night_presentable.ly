\version "2.24.1"
\header {
    title = "Silent Night"
    subtitle = "A Christmas Song"
    composer = "Joseph Mohr"
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
    instrumentName = "Trumpet "
    shortInstrumentName = "Tpt. "
    midiInstrument = "trumpet"
} {
    \key a \major
\clef treble
{ R2. R2. e'4. \tuplet 3/2 { fis'16 fis'16 fis'16 } e'4 }
\set Score.repeatCommands = #'((volta "1, 2, 3"))
 { \slashedGrace { d'8( } cis'2.) }
\set Score.repeatCommands = #'((volta #f))

\bar ":|."
\set Score.repeatCommands = #'((volta "4"))
 { cis'2. }
\set Score.repeatCommands = #'((volta #f))

\break
\Segno
{ b'2 b'4\staccato gis'2.\trill a'2 a'4 \GotoCoda e'2.~ e'2. }
\DScoda
\bar "||"
\cadenzaOn \stopStaff
                    \repeat unfold 1 {
                        s1
                        \bar ""
                    }
                    \startStaff \cadenzaOff
                    \break
                    \once \override Staff.KeySignature.break-visibility = #end-of-line-invisible
                    \once \override Staff.Clef.break-visibility = #end-of-line-invisible
                 \Coda { e'2. fis'2 fis'4 a'4. gis'8 fis'4 e'4. fis'8 e'4 cis'2. }
\bar "|."
}
\new StaffGroup <<
\new Staff \with {
    instrumentName = "Viola "
    shortInstrumentName = "Vla. "
    midiInstrument = "viola"
} {
    \numericTimeSignature
\time 3/4
\tempo 4 = 90
\key a \major
\clef alto
{ <cis' e' >4. fis'8 e'4 <e cis' >2. R2. R2. R2. }
{ b'2 b'4\staccato gis'2. a'2 a'4 e'2.~ e'2. }
\cadenzaOn \stopStaff
                    \repeat unfold 1 {
                        s1
                        \bar ""
                    }
                    \startStaff \cadenzaOff
                    \break
                    \once \override Staff.KeySignature.break-visibility = #end-of-line-invisible
                    \once \override Staff.Clef.break-visibility = #end-of-line-invisible
                 \Coda { e2. R2. R2. R2. R2. }
}
\new StaffGroup \with {
    instrumentName = "Violoncello "
    shortInstrumentName = "Vc. "
    midiInstrument = "cello"
} { <<
\set StaffGroup.systemStartDelimiter = #'SystemStartSquare
    \new Staff {
        \key a \major
\clef bass
{ cis'4. d'8 cis'4 a2. cis'4. d'8 cis'4 a2. }
{ a2. }
{ gis'2 gis'4\staccato e'2. e'2 e'4 cis'2.( c'2.) }
\cadenzaOn \stopStaff
                    \repeat unfold 1 {
                        s1
                        \bar ""
                    }
                    \startStaff \cadenzaOff
                    \break
                    \once \override Staff.KeySignature.break-visibility = #end-of-line-invisible
                    \once \override Staff.Clef.break-visibility = #end-of-line-invisible
                 \Coda { cis2. R2. R2. R2. R2. }
}
    \new Staff {
        \key a \major
\clef bass
{ a,2. a,2. a,2. a,2. a,2. e2. e2. a,2. cis2.( g,2.) }
\cadenzaOn \stopStaff
                    \repeat unfold 1 {
                        s1
                        \bar ""
                    }
                    \startStaff \cadenzaOff
                    \break
                    \once \override Staff.KeySignature.break-visibility = #end-of-line-invisible
                    \once \override Staff.Clef.break-visibility = #end-of-line-invisible
                 \Coda { e,2. R2. R2. R2. R2. }
}
>> }

>>

>>
