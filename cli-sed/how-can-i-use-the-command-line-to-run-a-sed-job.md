# How can I use the command line to run a sed job?
// plain

The command line can be used to run a sed job by using the `sed` command. The syntax of the `sed` command is `sed [options] script [input-file]`. The `script` argument specifies the sed commands to be applied to the input file.

For example, the following command will replace the word `dog` with the word `cat` in the file `input.txt` and print the output to the terminal:
```
sed 's/dog/cat/g' input.txt
```
The output of the above command will be:
```
I have a cat.
My cat is white.
```

The `sed` command has several options that can be used to control its behavior. The `-n` option suppresses automatic printing of pattern space, and the `-i` option allows in-place editing of files.

The `script` argument is composed of one or more sed commands. The `s` command is used to search and replace text, and the `d` command is used to delete lines.

For more information on the `sed` command, see the following links:
- [GNU Sed Manual](https://www.gnu.org/software/sed/manual/sed.html)
- [Sed Tutorial](https://www.grymoire.com/Unix/Sed.html)

onelinerhub: [How can I use the command line to run a sed job?](https://onelinerhub.com/cli-sed/how-can-i-use-the-command-line-to-run-a-sed-job)