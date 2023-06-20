# How do I use a shell script to tar a directory?
// plain

A shell script can be used to tar a directory by using the `tar` command. The syntax of the command is as follows: `tar -cvf <archive-name>.tar <directory-name>`.

For example, to create a tar archive of the directory `my_directory`, the command would be:

```
tar -cvf my_directory.tar my_directory
```

This command will create an archive file `my_directory.tar` in the current working directory.

## Code explanation

- `tar`: The `tar` command is used to create, view, extract, and modify tar archives.
- `-cvf`: The `-cvf` option is used to create an archive with the `tar` command. `-c` stands for create, `-v` stands for verbose, and `-f` stands for file.
- `<archive-name>.tar`: This is the name of the archive file that will be created.
- `<directory-name>`: This is the name of the directory that will be archived.

For more information, see the following links:
- [tar command](https://www.computerhope.com/unix/utar.htm)
- [tar options](https://www.gnu.org/software/tar/manual/html_node/tar_112.html)

onelinerhub: [How do I use a shell script to tar a directory?](https://onelinerhub.com/cli-tar/how-do-i-use-a-shell-script-to-tar-a-directory)