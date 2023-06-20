# How do I use a CLI sed query?
// plain

The `sed` command is a powerful utility for editing text files from the command line. It can be used to perform complex search and replace operations.

To use `sed`, you must provide a query string that describes the search and replace operations you want to perform. Here is an example of a `sed` query:

```
sed -i 's/old_word/new_word/g' file.txt
```

This query will search for all instances of `old_word` in `file.txt` and replace them with `new_word`. The `-i` flag tells `sed` to edit the file in-place.

Here is a breakdown of the command parts:
- `sed`: the command itself
- `-i`: the flag that tells `sed` to edit the file in-place
- `s/old_word/new_word/g`: the search and replace query, which consists of:
  - `s`: the search and replace operation
  - `old_word`: the word to search for
  - `new_word`: the word to replace with
  - `g`: the global flag, which tells `sed` to replace all occurrences of `old_word`
- `file.txt`: the file to edit

For more information on `sed`, see the [GNU sed Manual](https://www.gnu.org/software/sed/manual/sed.html).

onelinerhub: [How do I use a CLI sed query?](https://onelinerhub.com/cli-sed/how-do-i-use-a-cli-sed-query)