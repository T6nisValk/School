# Regular expressions - REGEX

REGEX is used to match patterns with strings of text. It provides means to efficiently replace,
parse, search or extract data defined by a specific pattern.

## Patterns

- `.` - Matches any character except newline.
    - `.read` will match Bread, Dread.
- `b.t` - Matches bit, bot, but, bat.
- `?` - Matches 0 or 1 repetitions, 0 or 1 of the preceeding characters. `olk?a` will match
  `ola` and `olka`.
- `+` - Matches 1 or more repetitions. `bre+d` will match `bred`, `breed`, `breeeeeed`.
- `*` - Matches 0 or more repetitions. `*ala` will match `ala`, `aaaaaaaaaaala`.
- `$` - End of the string. `f$` will match `golf`, `fhsfkf`. Means that the string ends with `f`.
- `^` - Caret at the beginning of a pattern signifies the start of the string. `^[a-z]`
  will match `bread`, `fred` but not `Bread`, `Frederic`.
  Caret inside a square bracket `[]` means negation. `[^a-z]` means not a-z.
- `[]` - Indicates a set of characters. `[Ww]ood` will match `Woodstock`, `wood`, `Woody`,
  `woodland`.
- `{n}` - Exactly n repetitions. `e{3}` will give any `e` 3 times. `{n,}` means n or more times.
  `{,n}` Means less than or equal to n times. `{m, n}` means between m and n times.
- `\` - Escape special characters.
- `|` - Means OR.
- `()` - Group sub patterns.
- `\d` - Any digit `[0-9]`.
- `\D` - Any non digit character.
- `\s` - Matches any whitespace character.
- `\S` - Non whitespace character.
- `\w` - Matches any word/alphanumeric. This is equivalent to `[A-Za-z0-9_]`.
- `\W` - Matches any non alphanumeric character.

## REGEX in Python

To use REGEX, you have to first import it - `import re`.

- `re.match` will try to match the REGEX pattern to the string. This only checks if the pattern
  matches the beginning of the string.
- `re.search` does not limit the match to the beginning. It can locate a match anywhere in the
  string. It looks for the first location where the pattern produces a match.
- `re.findall` returns all occurances / non overlapping matches.
- `re.split` splits the string by the occurance of the pattern.
- `re.sub` replaces all the occurance in your main string unless the max is provided.
- `re.subn` similar to re.sub, but it returns a tuple of the new string and the number of
  substitutions made.