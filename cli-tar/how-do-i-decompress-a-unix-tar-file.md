# How do I decompress a UNIX tar file?
// plain

Decompressing a UNIX tar file is a simple process.

1. First, open a terminal window and navigate to the directory containing the tar file.

2. Then, use the command `tar -xvf <filename>.tar` to decompress the tar file. The `-x` flag stands for extract, the `-v` flag stands for verbose output, and the `-f` flag stands for file.

3. The output should look something like this:
```
x file1.txt
x file2.txt
x file3.txt
```

4. This means that the tar file was successfully decompressed and the contents of the tar file are now in the current directory.

5. If you want to decompress the tar file into a specific directory, you can use the command `tar -xvf <filename>.tar -C <destination_directory>`. The `-C` flag stands for change directory.

6. You can also use the `-z` flag to decompress tar.gz files. The command would look like this: `tar -xvzf <filename>.tar.gz`.

7. If you need more information about the tar command, you can read the [GNU Tar Manual](https://www.gnu.org/software/tar/manual/tar.html).

onelinerhub: [How do I decompress a UNIX tar file?](https://onelinerhub.com/cli-tar/how-do-i-decompress-a-unix-tar-file)