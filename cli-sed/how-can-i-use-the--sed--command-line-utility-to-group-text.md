# How can I use the 'sed' command line utility to group text?
// plain

The 'sed' command line utility is a powerful tool for manipulating text. It can be used to group text in several ways.

For example, to group lines of text by a specific character, you can use the `sed` command with the `-n` option and a regular expression. The following example code will group lines of text by the `|` character:

```
sed -n 's/^\(.*\)|\(.*\)$/\1\n\2/p'
```

This example code will take the following input:

```
this|that
these|those
```

And produce the following output:

```
this
that
these
those
```

You can also use `sed` to group text by words. This can be done by using the `-r` option and a regular expression. The following example code will group lines of text by the word `foo`:

```
sed -r 's/^(.*)foo(.*)$/\1\nfoo\n\2/g'
```

This example code will take the following input:

```
foo bar
foo baz
```

And produce the following output:

```
foo
bar
foo
baz
```

Parts of the code:
- `sed`: the command line utility
- `-n`: the option used to group lines of text by a specific character
- `-r`: the option used to group lines of text by words
- `s/^\(.*\)|\(.*\)$/\1\n\2/p`: the regular expression used to group lines of text by the `|` character
- `s/^(.*)foo(.*)$/\1\nfoo\n\2/g`: the regular expression used to group lines of text by the word `foo`

## Helpful links
- [sed Manual](https://www.gnu.org/software/sed/manual/sed.html)
- [How to Use sed to Find and Replace String in Files](https://www.tecmint.com/find-and-replace-text-using-sed-command-in-linux/)

onelinerhub: [How can I use the 'sed' command line utility to group text?](https://onelinerhub.com/cli-sed/how-can-i-use-the--sed--command-line-utility-to-group-text)