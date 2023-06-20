# How do I use the sed command in the command line interface?
// plain

The `sed` command is a powerful tool in the command line interface (CLI) that can be used to search, find, and replace strings in text files. It is a stream editor, meaning that it reads input from files or from the standard input, and writes output to the standard output.

For example, to replace the word `dog` with the word `cat` in the file `animals.txt`, the command would be:
```
sed 's/dog/cat/' animals.txt
```
The output of the command would be the file `animals.txt` with all instances of the word `dog` replaced with the word `cat`.

The command is composed of several parts:

* `sed`: The command to invoke the stream editor
* `s/dog/cat/`: The search and replace pattern, where `s` indicates search and replace, `dog` is the string to search for, and `cat` is the string to replace with
* `animals.txt`: The file to be edited

For more information on `sed` and how to use it, please see the following links:

* [GNU Sed Manual](https://www.gnu.org/software/sed/manual/sed.html)
* [Sed Tutorial](https://www.grymoire.com/Unix/Sed.html)

onelinerhub: [How do I use the sed command in the command line interface?](https://onelinerhub.com/cli-sed/how-do-i-use-the-sed-command-in-the-command-line-interface)