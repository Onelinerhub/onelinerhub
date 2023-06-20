# How can I get the best compression when using tar and gzip?
// plain

The best compression when using tar and gzip can be achieved by using the `-9` flag. This flag will enable maximum compression. The example code below shows how to use the `-9` flag:

```
tar -czvf archive.tar.gz -9 file1 file2
```

The `-c` flag tells the tar command to create an archive, `-z` tells it to compress the archive using gzip, `-v` is for verbose output and `-f` specifies the filename of the resulting archive. The `-9` flag enables maximum compression.

## Code explanation


- `-c`: Create an archive
- `-z`: Compress the archive using gzip
- `-v`: Verbose output
- `-f`: Specify the filename of the resulting archive
- `-9`: Enable maximum compression

For further information, please refer to the following resources:

- [GNU tar Manual](https://www.gnu.org/software/tar/manual/tar.html)
- [Linux tar command](https://linuxize.com/post/how-to-use-tar-command-in-linux/)

onelinerhub: [How can I get the best compression when using tar and gzip?](https://onelinerhub.com/cli-tar/how-can-i-get-the-best-compression-when-using-tar-and-gzip)