# How do I use the command line to edit text using sed?
// plain

The `sed` command is a powerful tool for editing text in the command line. It works by applying a set of instructions, called a script, to a text file or stream. The following example shows how to use `sed` to replace all instances of the word "cat" with the word "dog" in a text file called `example.txt`:

```
sed 's/cat/dog/g' example.txt
```

This command will output the contents of `example.txt`, with all instances of "cat" replaced by "dog".

The `sed` command is made up of several parts:

- `s`: This is the command to substitute a string for another.
- `/cat/`: This is the string to be replaced.
- `/dog/`: This is the string to replace it with.
- `g`: This is an optional flag that tells `sed` to replace all instances of the string, rather than just the first one.

In addition to substitution, `sed` can be used to delete lines, insert text, and perform other types of text manipulation. For more information, see the following links:

- [GNU Sed Manual](https://www.gnu.org/software/sed/manual/sed.html)
- [Sed Tutorial](https://www.grymoire.com/Unix/Sed.html)
- [Sed One-Liners Explained](https://www.thegeekstuff.com/2009/11/unix-sed-tutorial-append-insert-replace-and-count-file-lines/)

onelinerhub: [How do I use the command line to edit text using sed?](https://onelinerhub.com/cli-sed/how-do-i-use-the-command-line-to-edit-text-using-sed)