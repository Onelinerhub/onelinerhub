# How do I use sed to insert a new line in a command line interface?
// plain

Sed (stream editor) is a command line utility used to perform text transformations. It can be used to insert a new line in a command line interface (CLI).

For example, to insert a new line after the string "Hello World" in a text file called "test.txt", the following command can be used:

```
sed -i 's/Hello World/Hello World\n/' test.txt
```

The command above will produce the following output:

```
Hello World
```

The command consists of the following parts:

- `sed`: The command to invoke the sed utility
- `-i`: The option to edit the file in place
- `s/Hello World/Hello World\n/`: The substitution command to replace the string "Hello World" with the string "Hello World" followed by a new line character (`\n`)
- `test.txt`: The file to edit

For more information, see the [GNU Sed Manual](https://www.gnu.org/software/sed/manual/sed.html).

onelinerhub: [How do I use sed to insert a new line in a command line interface?](https://onelinerhub.com/cli-sed/how-do-i-use-sed-to-insert-a-new-line-in-a-command-line-interface)