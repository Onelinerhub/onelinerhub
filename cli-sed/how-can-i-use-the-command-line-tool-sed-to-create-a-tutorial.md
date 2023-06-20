# How can I use the command line tool sed to create a tutorial?
// plain

Using the command line tool `sed`, you can create a tutorial by manipulating text files. For example, to replace the word "example" with "tutorial" in a text file:

```
sed -i 's/example/tutorial/g' textfile.txt
```

This command will replace all occurrences of "example" with "tutorial" in the file `textfile.txt`.

## Code explanation


- `sed`: Invokes the sed command line tool
- `-i`: Modifies the file in-place
- `s/example/tutorial/g`: Substitutes all occurrences of "example" with "tutorial"
- `textfile.txt`: The text file to be modified

For more information, please refer to the following links:

- [GNU sed Manual](https://www.gnu.org/software/sed/manual/sed.html)
- [Linux Sed Command Tutorial with Examples](https://linuxize.com/post/sed-command-tutorial-examples/)

onelinerhub: [How can I use the command line tool sed to create a tutorial?](https://onelinerhub.com/cli-sed/how-can-i-use-the-command-line-tool-sed-to-create-a-tutorial)