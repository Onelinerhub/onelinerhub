# How do I unzip a tar file in the terminal?
// plain

To unzip a tar file in the terminal, start by navigating to the directory containing the file. This can be done with the `cd` command.

For example, if the file is in the `Downloads` directory:
```
cd Downloads
```

Next, use the `tar` command to unzip the file. The syntax for this is `tar -xvf <filename>`.

For example, if the file is called `example.tar`:
```
tar -xvf example.tar
```

This command will extract the contents of the tar file into the current directory.

The parts of the command are as follows:
- `tar`: the tar command
- `-x`: the option to extract files
- `-v`: the option to display the progress of the extraction
- `-f`: the option to specify the filename
- `example.tar`: the filename of the tar file

If you need more information about the `tar` command, you can find it in the [GNU tar manual](https://www.gnu.org/software/tar/manual/tar.html).

onelinerhub: [How do I unzip a tar file in the terminal?](https://onelinerhub.com/cli-tar/how-do-i-unzip-a-tar-file-in-the-terminal)