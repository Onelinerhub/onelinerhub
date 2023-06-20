# How do I delete a line using the CLI sed command?
// plain

The sed command can be used to delete a line from a text file. The syntax to delete a line using sed is `sed 'Nd'`. Here, N is the line number of the line to be deleted. For example, to delete the third line from a text file, the command would be:

```
$ sed '3d' file.txt
```

The output of the above command would be the contents of the text file, with the third line deleted.

The parts of the command are:

* `sed`: the sed command
* `'3d'`: the argument to the sed command, which specifies the line number to delete
* `file.txt`: the name of the text file to be edited

For more information about using the sed command to delete lines, see the following links:

* [Sed Command in Linux - Delete Lines From a File](https://www.geeksforgeeks.org/sed-command-in-linux-delete-lines-from-a-file/)
* [How to delete a line using sed command in Linux](https://www.cyberciti.biz/faq/how-to-delete-a-line-using-sed-command-in-linux/)

onelinerhub: [How do I delete a line using the CLI sed command?](https://onelinerhub.com/cli-sed/how-do-i-delete-a-line-using-the-cli-sed-command)