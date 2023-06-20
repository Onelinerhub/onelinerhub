# How do I gzip a tar file in Linux?
// plain

In Linux, you can gzip a tar file by using the `gzip` command. This command will compress the tar file into a gzip file, which is usually much smaller in size.

```
$ tar -cvf my_files.tar my_files/
$ gzip my_files.tar
```

The above example code creates a tar file called `my_files.tar` from the folder `my_files/` and compresses it into a gzip file.

The `tar` command has the following parts:

* `-c`: creates a tar file
* `-v`: verbose mode, prints the name of each file it archives
* `-f`: specifies the filename of the tar file

The `gzip` command has the following parts:

* `my_files.tar`: the name of the tar file to be compressed

For more information about the `tar` and `gzip` commands, please refer to the following links:

* [tar command](https://linux.die.net/man/1/tar)
* [gzip command](https://linux.die.net/man/1/gzip)

onelinerhub: [How do I gzip a tar file in Linux?](https://onelinerhub.com/cli-tar/how-do-i-gzip-a-tar-file-in-linux)