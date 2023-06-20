# How can I use CLI sed to edit a file?
// plain

The `sed` command line utility can be used to edit files. It is a powerful tool for performing text transformations. To use `sed`, you must provide a command line argument with the desired transformation.

For example, to replace all occurrences of the word "foo" with "bar", you could use the following command:
```
sed 's/foo/bar/g' myfile.txt
```
This command would replace all occurrences of "foo" with "bar" in the file `myfile.txt`.

You can also use `sed` to delete lines from a file. For example, to delete all lines containing the word "foo", you could use the following command:
```
sed '/foo/d' myfile.txt
```
This command would delete all lines containing the word "foo" from the file `myfile.txt`.

You can also use `sed` to insert lines into a file. For example, to insert a line containing the word "foo" after the line containing the word "bar", you could use the following command:
```
sed '/bar/a\foo' myfile.txt
```
This command would insert the line "foo" after the line containing the word "bar" in the file `myfile.txt`.

The `sed` utility is very powerful and can be used to perform a variety of text transformations. For more information, see the following links:

* [GNU sed Manual](https://www.gnu.org/software/sed/manual/sed.html)
* [sed Tutorial](https://www.grymoire.com/Unix/Sed.html)
* [sed - An Introduction and Tutorial](https://www.panix.com/~elflord/unix/sed.html)

onelinerhub: [How can I use CLI sed to edit a file?](https://onelinerhub.com/cli-sed/how-can-i-use-cli-sed-to-edit-a-file)