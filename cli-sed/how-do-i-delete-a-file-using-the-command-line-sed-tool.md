# How do I delete a file using the command line sed tool?
// plain

To delete a file using the command line sed tool, you can use the following command:

```
sed -i '' '/<pattern>/d' <filename>
```

This command will delete all lines from the file that match the given `<pattern>`.

The command consists of the following parts:

1. `sed` - the command line sed tool
2. `-i ''` - an option that specifies that the given file should be edited in place
3. `/<pattern>/d` - a regular expression that specifies what lines should be deleted
4. `<filename>` - the name of the file to be edited

For example, if you want to delete all lines containing the word "hello" from the file `example.txt`, you can use the following command:

```
sed -i '' '/hello/d' example.txt
```

This command will delete all lines containing the word "hello" from the file `example.txt`.

## Helpful links

- [Sed Tutorial](https://www.grymoire.com/Unix/Sed.html)
- [Sed Command Examples](https://www.cyberciti.biz/faq/sed-command-examples/)

onelinerhub: [How do I delete a file using the command line sed tool?](https://onelinerhub.com/cli-sed/how-do-i-delete-a-file-using-the-command-line-sed-tool)