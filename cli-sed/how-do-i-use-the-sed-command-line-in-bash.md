# How do I use the sed command line in bash?
// plain

The `sed` command line is a powerful tool for text manipulation in bash. It allows users to search, find, and replace text in files. To use `sed`, the syntax is `sed [options] 'command' file(s)`.

For example, to replace all occurrences of the word "dog" with "cat" in the file `animals.txt`, the following command can be used:

```
sed 's/dog/cat/g' animals.txt
```

This command will output the contents of `animals.txt` with all occurrences of "dog" replaced with "cat".

The command consists of the following parts:

* `sed`: the command itself
* `s/dog/cat/g`: the search and replace command, where `s` stands for substitute, `dog` is the search pattern, `cat` is the replacement string, and `g` stands for global, meaning to replace all occurrences
* `animals.txt`: the file to be modified

For more information on `sed` and its options, see the [GNU sed Manual](https://www.gnu.org/software/sed/manual/sed.html).

onelinerhub: [How do I use the sed command line in bash?](https://onelinerhub.com/cli-sed/how-do-i-use-the-sed-command-line-in-bash)