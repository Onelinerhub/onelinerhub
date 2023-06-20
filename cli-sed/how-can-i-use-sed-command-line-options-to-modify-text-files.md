# How can I use sed command line options to modify text files?
// plain

The `sed` command line tool can be used to modify text files. It works by reading a file line-by-line and applying a set of operations on each line that matches a given pattern.

For example, the following code will replace all occurrences of the word `hello` with `goodbye` in the file `hello.txt`:
```
sed 's/hello/goodbye/g' hello.txt
```

The code consists of the following parts:

* `sed`: The `sed` command line tool.
* `s/hello/goodbye/g`: The `s` stands for substitution, `hello` is the pattern to be replaced, `goodbye` is the replacement, and `g` stands for global, meaning all occurrences of the pattern should be replaced.
* `hello.txt`: The file to be modified.

For more information about the `sed` command line tool, see the following resources:

* [Sed Tutorial](https://www.grymoire.com/Unix/Sed.html)
* [Sed Command in Linux/Unix with Examples](https://www.geeksforgeeks.org/sed-command-in-linux-unix-with-examples/)

onelinerhub: [How can I use sed command line options to modify text files?](https://onelinerhub.com/cli-sed/how-can-i-use-sed-command-line-options-to-modify-text-files)