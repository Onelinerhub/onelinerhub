# duplicates

How can I use the command line sed tool to remove duplicates?
// plain

The `sed` command line tool can be used to remove duplicates from a file. To do this, the `sed` command can be used with the `-i` flag, which will modify the file in place. The command will look something like this:

```
sed -i '$!N; /^\(.*\)
\1$/!P; D' <filename>
```

This command will search for duplicate lines and remove them. The parts of the command are as follows:

* `-i`: This flag tells `sed` to modify the file in place.
* `$!N`: This tells `sed` to read the next line into the pattern space.
* `/^\(.*\)
\1$/!P; D`: This part of the command searches for duplicate lines and removes them. The `^` character anchors the search to the beginning of the line, `\(.*\)` captures the line, `\1` refers to the captured line, and `$` anchors the search to the end of the line. The `!P` and `D` commands tell `sed` to delete the line if it is a duplicate.

This command should remove any duplicates from the given file.

## Helpful links

* [sed - An Introduction and Tutorial](https://www.grymoire.com/Unix/Sed.html)
* [Using sed to Remove Duplicate Lines from a File](https://stackoverflow.com/questions/17773376/using-sed-to-remove-duplicate-lines-from-a-file)

onelinerhub: [duplicates

How can I use the command line sed tool to remove duplicates?](https://onelinerhub.com/cli-sed/duplicates--how-can-i-use-the-command-line-sed-tool-to-remove-duplicates)