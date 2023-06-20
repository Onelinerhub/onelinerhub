# How do I tar a directory using a terminal?
// plain

Using the terminal, you can tar (or compress) a directory and its contents in one step. To do this, you need to use the `tar` command.

For example, to tar the directory `my_directory`, you would use the following command:

```
tar -cvzf my_directory.tar.gz my_directory
```

This command will create a compressed archive called `my_directory.tar.gz` containing the contents of `my_directory`.

The parts of the command are:
- `tar`: the command to create an archive
- `-cvzf`: the flags used to specify the desired behavior of the command
  - `-c`: create an archive
  - `-v`: verbose - display the files being added to the archive
  - `-z`: compress the archive using gzip
  - `-f`: specify the filename of the archive
- `my_directory.tar.gz`: the filename of the archive
- `my_directory`: the directory to be archived

For more information, see the [GNU tar manual](https://www.gnu.org/software/tar/manual/html_node/tar_5.html).

onelinerhub: [How do I tar a directory using a terminal?](https://onelinerhub.com/cli-tar/how-do-i-tar-a-directory-using-a-terminal)