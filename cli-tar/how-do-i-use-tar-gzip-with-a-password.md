# How do I use tar gzip with a password?
// plain

`tar` is a command line utility used to compress and decompress files. `gzip` is a compression algorithm used to compress files. To use `tar gzip` with a password, you can use the `--gzip-options` flag with the `--password` option.

```
tar --gzip-options --password=mypassword -cvzf myarchive.tar.gz myfiles
```

This command will create an archive called `myarchive.tar.gz` that is compressed with `gzip` and encrypted with the password `mypassword`.

The parts of the command are as follows:

- `tar`: The command line utility used to compress and decompress files.
- `--gzip-options`: The flag used to specify options for `gzip`.
- `--password`: The option used to specify the password to be used for encryption.
- `-cvzf`: Options used to create an archive with compression.
  - `-c`: Create an archive.
  - `-v`: Verbose output.
  - `-z`: Compress the archive with `gzip`.
  - `-f`: Specify the filename of the archive.
- `myarchive.tar.gz`: The filename of the archive.
- `myfiles`: The files to be included in the archive.

For more information, see the [tar man page](https://linux.die.net/man/1/tar).

onelinerhub: [How do I use tar gzip with a password?](https://onelinerhub.com/cli-tar/how-do-i-use-tar-gzip-with-a-password)