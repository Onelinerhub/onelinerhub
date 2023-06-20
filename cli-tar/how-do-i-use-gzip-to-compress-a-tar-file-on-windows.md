# How do I use gzip to compress a tar file on Windows?
// plain

Using gzip to compress a tar file on Windows is possible with the help of 7-Zip. The following example code demonstrates how to compress a tar file named `example.tar` into a gzip file named `example.tar.gz`:

```
7z a -tgzip example.tar.gz example.tar
```

The above command will compress `example.tar` into `example.tar.gz` using gzip compression.

The parts of the command are as follows:

- `7z`: The 7-Zip command line executable
- `a`: The “add” command, which adds files to an archive
- `-tgzip`: The “use gzip” command, which tells 7-Zip to use gzip compression
- `example.tar.gz`: The name of the gzip archive to be created
- `example.tar`: The name of the tar file to be compressed

For more information on using 7-Zip from the command line, see the [7-Zip Command Line Documentation](https://sevenzip.osdn.jp/chm/cmdline/syntax.htm).

onelinerhub: [How do I use gzip to compress a tar file on Windows?](https://onelinerhub.com/cli-tar/how-do-i-use-gzip-to-compress-a-tar-file-on-windows)