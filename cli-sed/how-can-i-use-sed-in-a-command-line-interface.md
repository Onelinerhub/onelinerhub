# How can I use sed in a command line interface?
// plain

Sed is a stream editor that can be used in a command line interface (CLI) to modify text. It reads an input file, makes changes according to a set of commands, and prints the result to the standard output.

For example, to replace all occurrences of the word “foo” with the word “bar” in a file, you can use the following command:

```
sed 's/foo/bar/g' input.txt
```

This command will print the modified version of `input.txt` to the standard output. To save the output to a file, you can use the following command:

```
sed 's/foo/bar/g' input.txt > output.txt
```

The command consists of the following parts:

* `s/foo/bar/g` – this is the sed command that replaces all occurrences of “foo” with “bar”;
* `input.txt` – this is the name of the input file;
* `> output.txt` – this is the redirection operator that saves the output of the command to the file `output.txt`.

For more information about using sed, see the following links:

* [Sed Tutorial](https://www.grymoire.com/Unix/Sed.html)
* [Sed Man Page](https://www.gnu.org/software/sed/manual/sed.html)

onelinerhub: [How can I use sed in a command line interface?](https://onelinerhub.com/cli-sed/how-can-i-use-sed-in-a-command-line-interface)