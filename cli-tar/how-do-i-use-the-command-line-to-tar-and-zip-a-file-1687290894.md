# How do I use the command line to tar and zip a file?
// plain

To tar and zip a file using the command line, use the `tar` command followed by the `gzip` command. This will create a `.tar.gz` file.

The syntax for this command is:
```
tar -cvzf <name_of_file>.tar.gz <name_of_file>
```

For example, to tar and zip a file called `example.txt`, the command would be:
```
tar -cvzf example.tar.gz example.txt
```

The output of this command should be:
```
example.txt
```

The parts of the command are as follows:
- `tar`: the command to create an archive
- `-cvzf`: the flags used to indicate the type of archive to create and the options to use
- `<name_of_file>.tar.gz`: the name of the archive file to create
- `<name_of_file>`: the name of the file to be archived

For more information on the `tar` command, see the following links:
- [GNU tar Manual](https://www.gnu.org/software/tar/manual/tar.html)
- [Linux tar Command Tutorial](https://linuxize.com/post/linux-tar-command/)

onelinerhub: [How do I use the command line to tar and zip a file?](https://onelinerhub.com/cli-tar/how-do-i-use-the-command-line-to-tar-and-zip-a-file-1687290894)