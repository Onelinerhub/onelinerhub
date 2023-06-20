# How do I use sed to add quotes around a string in a command line interface?
// plain

Sed (stream editor) is a powerful command line tool used to perform basic text transformations on an input stream (a file or input from a pipeline). It can be used to add quotes around a string in a command line interface.

The following example shows how to use sed to add double quotes around a string:

```
echo "Hello World" | sed 's/\(.*\)/"\1"/'
```

The output of the above command will be:
```
"Hello World"
```

The command works by using the `s` command to substitute the pattern `\(.*\)` with the string `"\1"`. The `\(.*\)` pattern matches any character (`.`) zero or more times (`*`) and stores the match in a memory buffer denoted by `\1`. The `\1` is then replaced with the string `"\1"` which adds double quotes around the matched string.

The following list explains the parts of the command:
- `echo "Hello World"`: Prints the string "Hello World" to the standard output.
- `|`: A pipe symbol which passes the output of the previous command to the next command.
- `sed 's/\(.*\)/"\1"/'`: The sed command which performs the substitution.
- `\(.*\)`: A pattern which matches any character (`.`) zero or more times (`*`).
- `\1`: A memory buffer which stores the match of the pattern.
- `"\1"`: The string which is substituted for the match of the pattern.

For more information about using sed to add quotes around a string, please refer to the following links:
- [Sed - An Introduction and Tutorial](http://www.grymoire.com/Unix/Sed.html)
- [Sed Tutorial – Advanced Sed Substitution Examples](https://www.cyberciti.biz/faq/sed-tutorial-advanced-sed-substitution-examples/)

onelinerhub: [How do I use sed to add quotes around a string in a command line interface?](https://onelinerhub.com/cli-sed/how-do-i-use-sed-to-add-quotes-around-a-string-in-a-command-line-interface)