# How do I use the command line to compress a file using SED and ZIP?
// plain

To compress a file using SED and ZIP from the command line, you can use the following code:

```
sed 's/^/prefix-/' <file-name> | zip <file-name>.zip -
```

This code uses the `sed` command to add a prefix to each line of the file, then pipes the output to `zip`, which compresses the file into the specified `<file-name>.zip`.

The code consists of the following parts:

1. `sed 's/^/prefix-/' <file-name>`: This uses `sed` to add a prefix to each line of the file specified by `<file-name>`.
2. `| zip <file-name>.zip -`: This pipes the output of `sed` to `zip`, which compresses the file into `<file-name>.zip`.

You can find more information about `sed` and `zip` commands on the following links:

- [sed](https://www.gnu.org/software/sed/manual/sed.html)
- [zip](https://linux.die.net/man/1/zip)

onelinerhub: [How do I use the command line to compress a file using SED and ZIP?](https://onelinerhub.com/cli-sed/how-do-i-use-the-command-line-to-compress-a-file-using-sed-and-zip)