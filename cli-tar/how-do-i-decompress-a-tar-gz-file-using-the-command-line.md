# How do I decompress a tar.gz file using the command line?
// plain

Decompressing a `tar.gz` file using the command line is a simple process.

The basic command to use is `tar -xzvf <filename.tar.gz>`, where `<filename.tar.gz>` is the name of the file you are decompressing.

For example, if the file you are decompressing is called `example.tar.gz`, you would use the command:

```
tar -xzvf example.tar.gz
```

This command will output a list of the files that are being decompressed:

```
x example/
x example/file1.txt
x example/file2.txt
```

The `-x` flag tells `tar` to extract the files. The `-z` flag tells `tar` to decompress the file using `gzip` compression. The `-v` flag stands for verbose, which means it will output the list of files it is extracting. The `-f` flag tells `tar` which file to extract from.

You can find more information about the `tar` command [here](https://www.computerhope.com/unix/utar.htm).

onelinerhub: [How do I decompress a tar.gz file using the command line?](https://onelinerhub.com/cli-tar/how-do-i-decompress-a-tar-gz-file-using-the-command-line)