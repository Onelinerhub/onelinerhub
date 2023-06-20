# How do I use a regex with the CLI sed command?
// plain

Using a regex with the CLI sed command is a powerful way to search for and replace text in files. The syntax for using a regex with sed is `sed -r 's/regex/replacement/g' filename`.

For example, if you wanted to replace all occurrences of the word 'hello' with 'goodbye' in a file called 'example.txt', you could run the following command:
```
sed -r 's/hello/goodbye/g' example.txt
```
This command will replace all occurrences of 'hello' with 'goodbye' in the file 'example.txt'.

## Code explanation

- `sed` - The sed command used to perform the search and replace.
- `-r` - The flag used to enable extended regular expressions.
- `s/regex/replacement/g` - The search and replace pattern. The 's' indicates that this is a search and replace pattern, the 'regex' is the pattern to search for, the 'replacement' is the text to replace the pattern with, and the 'g' indicates that the search and replace should be done globally (i.e. all occurrences).
- `example.txt` - The name of the file to perform the search and replace on.

## Helpful links
- [Sed Command Tutorial](https://www.tutorialspoint.com/unix_commands/sed.htm)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/)

onelinerhub: [How do I use a regex with the CLI sed command?](https://onelinerhub.com/cli-sed/how-do-i-use-a-regex-with-the-cli-sed-command)