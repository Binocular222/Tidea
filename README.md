Tidea
=====

Tidea means Text Idea, or Idea presented as Text

Tidea is useful to record knowledge

The below text
     presented each idea in 1 line and show relationship between ideas by indent.
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
          Child idea is indented below parent idea by 5 spaces
          Internal link is wrapped by quare brackets: [[...]]  (no need for external link)
               i.e: [[image.jpg]]  [[object\spreadsheet.xlsx]]  [[C:\test.tex]]  http://google.com/
               Ctrl+enter will fire up those links
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
     Indent-level = 5-space
     Format text
          |   Format  |  Code  |     Name of character      |         Sample        |     Width     |      Sublime       |
          |-----------|--------|----------------------------|-----------------------|---------------|--------------------|
          | Green     |        | external link              | http://google.com/    |               | link.external      |
          | Green     |        | internal link              | [[Target.txt]]        |               | link.internal      |
          | Green     |        | Email                      | mr.khanhnam@gmail.com |               | link.email         |
          | Purple    |        | Phone number               | 091234567857          |               | constant.numeric   |
          | Orange    | U+202a | Bidirectional text control | foo‪Orange‪bar        | Zero          | variable.parameter |
          | Red       | U+200b | Zero-Width-Space           | foo​Red​bar           | Zero          | keyword.control    |
          | Gray      | U+202c | Bidirectional text control | foo‬Gray‬bar          | Zero          | comment.block      |
          | Bold      | U+200e | Bidirectional text control | foo​‎Bold‎bar         | Zero          | markup.bold        |
          | Italic    | U+200f | Bidirectional text control | foo​‏Italic‏bar       | Zero          | markup.italic      |
          | Highlight | U+202d | Bidirectional text control | foo‏‭Hightlight‭bar   | Zero          | markup.hightlight  |
