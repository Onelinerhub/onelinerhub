# How do I use the command line sed utility?
// plain

The `sed` utility is a powerful command line tool for editing text. It can be used to perform a variety of tasks, such as replacing text, removing lines, and transforming text.

For example, to replace all occurrences of the word "foo" with the word "bar", you can use the following command:
```
sed 's/foo/bar/g' filename
```
This will replace all occurrences of "foo" with "bar" in the file `filename`.

You can also use `sed` to remove lines from a file that contain a certain string. For example, to remove all lines containing the word "foo", you can use the following command:
```
sed '/foo/d' filename
```
This will remove all lines containing the word "foo" from the file `filename`.

You can also use `sed` to transform text. For example, to convert all occurrences of the word "foo" to uppercase, you can use the following command:
```
sed 's/foo/\U&/g' filename
```
This will convert all occurrences of the word "foo" to uppercase in the file `filename`.

For more information on using the `sed` utility, see the following links:
- [sed - An Introduction and Tutorial](https://www.grymoire.com/Unix/Sed.html)
- [sed Manual](https://www.gnu.org/software/sed/manual/sed.html)

onelinerhub: [How do I use the command line sed utility?](https://onelinerhub.com/cli-sed/how-do-i-use-the-command-line-sed-utility)