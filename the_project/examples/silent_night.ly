\version "2.24.1"
\header {
    title = "Silent Night"
    subtitle = "A Christmas Song"
    composer = "Joseph Mohr"
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
  \mark \markup { \musicglyph #"scripts.coda" }
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
} {
    \key a \major
\clef treble
{ R2. R2. e'4. \tuplet 3/2 { cis''16[ cis''16 r16] } e'4 }
\volta 1 {  { \slashedGrace { d'8( } cis'2.) } }

\bar ":|."
\volta 2 {  { cis'2. } }

\break
\Segno
{ b'2 b'4\staccato gis'2.\trill a'2 a'4 e'2. }
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
                 \Coda { fis'2. fis'2. }
\bar "|."
}
\new StaffGroup <<
\new Staff \with {
    instrumentName = "Viola "
    shortInstrumentName = "Vla. "
} {
    \numericTimeSignature
\time 3/4
\tempo 4 = 90
\key a \major
\clef alto
{ <cis' e' >4. fis'8 e'4 <e cis' >2. R2. R2. R2. }
{ b'2 b'4\staccato gis'2. a'2 a'4 e'2. }
\cadenzaOn \stopStaff
                    \repeat unfold 1 {
                        s1
                        \bar ""
                    }
                    \startStaff \cadenzaOff
                    \break
                    \once \override Staff.KeySignature.break-visibility = #end-of-line-invisible
                    \once \override Staff.Clef.break-visibility = #end-of-line-invisible
                 \Coda { fis'2. fis'2. }
}
\new StaffGroup \with {
    instrumentName = "Violoncello "
    shortInstrumentName = "Vc. "
} { <<
\set StaffGroup.systemStartDelimiter = #'SystemStartSquare
    \new Staff {
        \key a \major
\clef bass
{ cis'4. d'8 cis'4 a2. cis'4. d'8 cis'4 a2. }
{ a2. }
{ gis'2 gis'4\staccato e'2. \slashedGrace { fis'8 } e'2 e'4 cis'2. }
\cadenzaOn \stopStaff
                    \repeat unfold 1 {
                        s1
                        \bar ""
                    }
                    \startStaff \cadenzaOff
                    \break
                    \once \override Staff.KeySignature.break-visibility = #end-of-line-invisible
                    \once \override Staff.Clef.break-visibility = #end-of-line-invisible
                 \Coda { fis2. fis2. }
}
    \new Staff {
        \key a \major
\clef bass
{ a,2. a,2. a,2. a,2. a,2. e2. e2. a,2. cis2. }
\cadenzaOn \stopStaff
                    \repeat unfold 1 {
                        s1
                        \bar ""
                    }
                    \startStaff \cadenzaOff
                    \break
                    \once \override Staff.KeySignature.break-visibility = #end-of-line-invisible
                    \once \override Staff.Clef.break-visibility = #end-of-line-invisible
                 \Coda { fis,2. fis,2. }
}
>> }

>>

>>