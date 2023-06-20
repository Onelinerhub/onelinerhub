# How to use the CLI to modify the head of a file using sed?
// plain

Using the `sed` command line utility, you can modify the head of a file. `sed` stands for "stream editor" and can be used to perform editing operations on text streams and files. Here is an example of how to use `sed` to modify the head of a file:

```
sed -i '1s/.*/This is the new head of the file/' <file_name>
```

This command replaces the first line of the file with the text `This is the new head of the file`.

## Code explanation


- `sed`: The command line utility used for editing streams and files.
- `-i`: This flag tells `sed` to edit the file in-place, meaning that it will modify the original file instead of creating a new one.
- `1s/.*/This is the new head of the file/`: This is the edit command. The `1` tells `sed` to edit the first line of the file, the `s` tells `sed` to substitute the line, the `.*` tells `sed` to match any characters, and the `This is the new head of the file` is the text that will replace the first line.
- `<file_name>`: This is the name of the file that will be edited.

## Helpful links

- [GNU sed manual](https://www.gnu.org/software/sed/manual/sed.html)
- [An Introduction to sed](https://www.grymoire.com/Unix/Sed.html)

onelinerhub: [How to use the CLI to modify the head of a file using sed?](https://onelinerhub.com/cli-sed/how-to-use-the-cli-to-modify-the-head-of-a-file-using-sed)