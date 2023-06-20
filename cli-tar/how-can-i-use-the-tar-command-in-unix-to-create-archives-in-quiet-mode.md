# How can I use the tar command in Unix to create archives in quiet mode?
// plain

The `tar` command in Unix can be used to create archives in quiet mode by using the `-q` or `--quiet` flag. This flag will suppress the output of the command, which is useful for redirecting and piping the output of the command.

## Example code

```
tar -cf archive.tar --quiet file1 file2 file3
```

## Code explanation

* `tar` - the command to create archives
* `-c` - the flag to create an archive
* `-f` - the flag to specify the name of the archive
* `--quiet` - the flag to suppress the output of the command
* `file1`, `file2`, `file3` - the files to be included in the archive

## Helpful links
* [GNU Tar Manual](https://www.gnu.org/software/tar/manual/tar.html)

onelinerhub: [How can I use the tar command in Unix to create archives in quiet mode?](https://onelinerhub.com/cli-tar/how-can-i-use-the-tar-command-in-unix-to-create-archives-in-quiet-mode)