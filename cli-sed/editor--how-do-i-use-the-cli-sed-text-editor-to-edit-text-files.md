# editor

How do I use the CLI sed text editor to edit text files?
// plain

The `sed` text editor is a powerful command line tool for editing text files. It works by taking a script of commands as input and applying those commands to a text file. To use `sed`, you must first create a sed script that contains the commands you want to execute on the text file. For example, to replace all instances of the word “Hello” with “Goodbye” in a text file “example.txt”, you would use the following script:

```
sed 's/Hello/Goodbye/g' example.txt
```

This command will output the contents of the file with all instances of “Hello” replaced with “Goodbye”.

The script consists of several parts:

* `s/` - This is the command for substitution.
* `Hello` - This is the string to be replaced.
* `Goodbye` - This is the string that will replace “Hello”.
* `g` - This is the flag to indicate that all instances of “Hello” should be replaced.
* `example.txt` - This is the name of the text file to be edited.

You can also use `sed` to perform more complex edits, such as inserting or deleting lines from a text file. For more information on `sed`, you can refer to the [GNU sed Manual](https://www.gnu.org/software/sed/manual/sed.html).

onelinerhub: [editor

How do I use the CLI sed text editor to edit text files?](https://onelinerhub.com/cli-sed/editor--how-do-i-use-the-cli-sed-text-editor-to-edit-text-files)