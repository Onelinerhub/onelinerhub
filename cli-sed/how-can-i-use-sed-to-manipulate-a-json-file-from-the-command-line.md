# How can I use sed to manipulate a JSON file from the command line?
// plain

Sed is a powerful command line tool that can be used to manipulate a JSON file. To use sed to manipulate a JSON file, you must first specify the pattern that you want to match, then specify the replacement string. For example, if you wanted to replace the text "foo" with "bar" in a JSON file, you could use the following command:

```
sed -i 's/foo/bar/g' my_json_file.json
```

This command will replace all occurrences of "foo" with "bar" in the file `my_json_file.json`.

You can also use sed to add text to a JSON file. For example, if you wanted to add the text "baz" after the text "foo" in a JSON file, you could use the following command:

```
sed -i 's/foo/foo baz/g' my_json_file.json
```

This command will add the text "baz" after each occurrence of "foo" in the file `my_json_file.json`.

In addition, you can use sed to delete text from a JSON file. For example, if you wanted to delete the text "foo" from a JSON file, you could use the following command:

```
sed -i '/foo/d' my_json_file.json
```

This command will delete all occurrences of "foo" from the file `my_json_file.json`.

Parts of code and explanation:

1. `sed -i 's/foo/bar/g' my_json_file.json` - This command will replace all occurrences of "foo" with "bar" in the file `my_json_file.json`.
2. `sed -i 's/foo/foo baz/g' my_json_file.json` - This command will add the text "baz" after each occurrence of "foo" in the file `my_json_file.json`.
3. `sed -i '/foo/d' my_json_file.json` - This command will delete all occurrences of "foo" from the file `my_json_file.json`.

## Helpful links

- [Sed Tutorial](https://www.grymoire.com/Unix/Sed.html)
- [Sed Command Cheat Sheet](https://www.cheatography.com/davechild/cheat-sheets/sed/)

onelinerhub: [How can I use sed to manipulate a JSON file from the command line?](https://onelinerhub.com/cli-sed/how-can-i-use-sed-to-manipulate-a-json-file-from-the-command-line)