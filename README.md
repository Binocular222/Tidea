Tidea means Text Idea, or Idea presented as Text

Tidea is a way of writing, it's neither a source code nor a new data format
Tidea is useful to record knowledge

The below text
    presents each idea in 1 line and show relationship between ideas by indent.
    Thus, well demonstrate the spirit of Tidea.

Phylosophy
    Idea is the most valuable asset, the only thing matter
    Idea is a stream of plain text + image + sound inside human brain
    Idea has nothing to do with Format, grammar, writing style...
    Tidea records and link text + image + sound together in an succinct, informal, platform-independent ways

How Tidea do that?
    Ideas are written in plain text files
    No special character, no escape character, no markup tag → What you write is what you meant
    Only 3 rules:
        Child idea is indented below parent idea by 4 spaces
        Internal link is wrapped by quare brackets: [[...]]
            i.e: [[image.jpg]]  [[object\spreadsheet.xlsx]]  [[C:\test.tex]]  http://google.com/
            Ctrl+enter will fire up those links
            Internal link can have "Jumpto" section after sharp # sign,
                i.e: [[C:\test.txt#Section]]
                This open test.txt, then jumpto the first text "Section" (similar to common find feature)
        External link & Email has no special denotation
        Tidea support very minimal mark-up
            Use a few zero-space Unicode characters, i.e:
                a ‎Bold‎text ‏need‏s ‬no‬ ob​stru​sive ‭mark-up‭ ‪tag‪
                See table at the end
            → Any text editor with syntax highlighting capability can render these format
            → Even Notepad can view all the content correctly (only lose the format)
            → source code looks the same as final deliverable

A few good practice (non-mandatory):
    Use mark-up as little as possible
    Writing should be short, to the point, no need for lengthy/articulate sentences
    Very informal, grammar is not needed
    Have a root text files contain main ideas then have some internal links to
        Other text files
        Everything non-text (Image, sound, chart, formula, url...)
    To facilitate View on small-screen devices and Printing
        Lines should be as short as possible
        Each file should have no more than 4 indent level
    File Format: txt with Encoding = UTF-16 LE with BOM
    View with Fixed width font (i.e: Consolas)

Format
    Indent-level = 4-space
    Format text
        |   Format  |  Code  |     Name of character      |         Sample        |     Width     |      Sublime       |
        |-----------|--------|----------------------------|-----------------------|---------------|--------------------|
        | Green     |        | none                       | http://google.com/    |               | link.external      |
        | Green     |        | [[]]                       | [[Target.txt]]        |               | link.internal      |
        | Unused    | U+2009 | THIN SPACE                 | foo link bar          | 1/5 em        | link.internal      |
        | Green     |        | none                       | mr.khanhnam@gmail.com |               | link.email         |
        | Purple    |        | none                       | 091234567857          |               | constant.numeric   |
        | Orange    | U+202a | Bidirectional text control | foo‪Orange‪bar        | Zero          | variable.parameter |
        | Red       | U+200b | Zero-Width-Space           | foo​Red​bar           | Zero          | keyword.control    |
        | Gray      | U+202c | Bidirectional text control | foo‬Gray‬bar          | Zero          | comment.block      |
        | Bold      | U+200e | Bidirectional text control | foo​‎Bold‎bar         | Zero          | markup.bold        |
        | Italic    | U+200f | Bidirectional text control | foo​‏Italic‏bar       | Zero          | markup.italic      |
        | Highlight | U+202d | Bidirectional text control | foo‏‭Hightlight‭bar   | Zero          | markup.hightlight  |
        |-----------|--------|----------------------------|-----------------------|---------------|--------------------|
        | Unused    | U+202e | Bidirectional text control | foo‮‏Hightlight‮bar   | Zero          |                    |
        | Unused    | U+202b | Bidirectional text control | foo​‫Red‫bar          | Zero          |                    |
        | Unused    | U+FEFF | ZERO WIDTH NO-BREAK SPACE  | foo﻿bar               | Zero          |                    |
        | Unused    | U+200c | Zero-Width-Non-joiner      | fooXXbar              | Zero          |                    |
        | Unused    | U+200a | HAIR SPACE                 | foo bar               | <1/6 em       |                    |
        | Unused    | U+2006 | SIX-PER-EM SPACE           | foo bar               | 1/6 em        |                    |
        | Unused    | U+2005 | FOUR-PER-EM SPACE          | foo bar               | 1/4 em        |                    |
        | Unused    | U+2004 | THREE-PER-EM SPACE         | foo Italic bar        | 1/3 em        |                    |
        | Unused    | U+2000 | EN QUAD                    | foo Orange bar        | 1 en (1/2 em) |                    |
        | Unused    | U+2001 | EM QUAD                    | foo gray bar          | 1 em          |                    |
        | Unused    | U+2002 | EN SPACE                   | foo red bar           | 1 en (1/2 em) |                    |
        | Unused    | U+2003 | EM SPACE                   | foo Bold bar          | 1 em          |                    |
        http://www.cs.tut.fi/~jkorpela/chars/spaces.html
        http://en.wikipedia.org/wiki/Unicode_control_characters
        [[Tidea format in Microsoft Word.docx]]

File naming convention:
    SortInfo1.SortInfo2, Identity ~ Tag1, Tag2,.txt
    A large subject can be broken down like this:
        Tax.Procedure.txt
        Tax.Process.txt
        Tax.Regulation.txt
        Tax.Regulation.CIT.txt
        Tax.Regulation.PIT.txt
        Tax.Regulation.VAT.txt
    To visualize relationship between files
        FileName contain a recognizable Identity (fairly-unique, standard name)
        Relationship type
            Create/Modify/supporting info is denoted as +
            Terminate is denoted as -
        Upstream/Downstream: Relationship type (+-) is placed before or after target file's Identifier
        i.e: "13.2013.TT.BTC, VAT law, VN, +21.2012, 23.2013-.docx" => 13.2013 modify 21.2012  AND  being nullified by 23.2013
    Law:
        "210.2012.TT.BTC, Tomtatnoidung, EN, -SoVanBanBiHuy, +SoVabBanBiDieuChinh.docx"
        Appendix and PDF signed version should be attached inside main file
        EN version is separated
​​
Example:
    Comment
        ​(ftp:\/\/|https?:\/\/)?​‪(\w\.)?([\w-]+)\.[a-z]{2,6}‪​(\.|\/)[\/\w\.-:~]*​
        ​Optional ftp:// or http:// or https://​  ‪Domain en.wiki.com‪  ​Subpages /football#Rules​