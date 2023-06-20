# replace text

How do I use CLI sed to replace text?
// plain

The `sed` command line utility can be used to replace text. It is a powerful tool that can be used to manipulate text in a variety of ways.

To use `sed` to replace text, you need to provide a search pattern and a replacement string. The following example shows how to replace the word 'foo' with 'bar':

```
sed 's/foo/bar/g' input.txt
```

This command will replace all occurrences of 'foo' with 'bar' in the file `input.txt`.

The structure of the command is as follows:

* `s`: stands for 'substitute'
* `/foo/`: the search pattern
* `/bar/`: the replacement string
* `g`: stands for 'global', meaning that all occurrences of the search pattern should be replaced

You can also use `sed` to replace text in multiple files. To do this, you can use the `-i` flag, which stands for 'in-place':

```
sed -i 's/foo/bar/g' *.txt
```

This command will replace all occurrences of 'foo' with 'bar' in all `.txt` files in the current directory.

For more information on using `sed`, please see the following links:

* [GNU sed Manual](https://www.gnu.org/software/sed/manual/sed.html)
* [Sed Tutorial](https://www.grymoire.com/Unix/Sed.html)
* [Sed Commands](https://www.thegeekstuff.com/2009/11/unix-sed-tutorial-append-insert-replace-and-count-file-lines/)

onelinerhub: [replace text

How do I use CLI sed to replace text?](https://onelinerhub.com/cli-sed/replace-text--how-do-i-use-cli-sed-to-replace-text)