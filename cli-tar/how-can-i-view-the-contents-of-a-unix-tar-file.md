# How can I view the contents of a Unix tar file?
// plain

To view the contents of a Unix tar file, you can use the `tar` command with the `tvf` option. This command will list the contents of the tar file without extracting it. The general syntax is as follows:
```
tar tvf <filename>.tar
```
The output of the command will be a list of the contents of the tar file, including the file name, permissions, owner, size, and timestamp.

The following example code shows the output of the command for a tar file named `example.tar`:
```
$ tar tvf example.tar
-rw-r--r-- me/users   0 2019-10-20 15:20 file1.txt
-rw-r--r-- me/users   0 2019-10-20 15:20 file2.txt
-rw-r--r-- me/users   0 2019-10-20 15:20 file3.txt
```

The parts of the command are as follows:
- `tar`: The tar command is used to create, modify, and extract files from a tar archive.
- `tvf`: This option is used to view the contents of a tar file.
- `<filename>.tar`: This is the name of the tar file.

## Helpful links
- [tar command](https://www.computerhope.com/unix/utar.htm)
- [tar command examples](https://www.cyberciti.biz/faq/linux-unix-bsd-tar-command-examples/)

onelinerhub: [How can I view the contents of a Unix tar file?](https://onelinerhub.com/cli-tar/how-can-i-view-the-contents-of-a-unix-tar-file)