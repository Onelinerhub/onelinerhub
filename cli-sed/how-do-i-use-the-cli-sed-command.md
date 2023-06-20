# How do I use the CLI sed command?
// plain

The `sed` command is a powerful command-line tool for manipulating text. It can be used to perform a variety of operations, such as searching and replacing, transforming, and transforming text.

To use the `sed` command, you need to specify the input file, the command, and the output file. Here's an example of how to use the `sed` command to replace all occurrences of the word "cat" with "dog" in a text file:

```
sed 's/cat/dog/g' input.txt > output.txt
```

The `sed` command has three parts:

1. `s` - This is the command that tells `sed` to perform a substitution.
2. `cat` - This is the pattern that `sed` will search for.
3. `dog` - This is the replacement string that `sed` will use to replace the pattern.

The `g` flag at the end of the command tells `sed` to replace all occurrences of the pattern.

For more information on the `sed` command and its usage, see the [GNU sed manual](https://www.gnu.org/software/sed/manual/sed.html).

onelinerhub: [How do I use the CLI sed command?](https://onelinerhub.com/cli-sed/how-do-i-use-the-cli-sed-command)