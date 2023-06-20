# How can I use tar gzip to create a multithreaded archive?
// plain

Tar gzip can be used to create a multithreaded archive by passing the `-I` or `--use-compress-program` option to the `tar` command. This option allows you to specify an external compression program such as `pigz` which is a multithreaded gzip implementation.

For example, to create a tar gzip archive using 4 threads you would run the following command:

```
tar -cvf archive.tar.gz -I pigz -p 4 <files-to-archive>
```

This command will create an archive named `archive.tar.gz` using 4 threads to compress the specified `<files-to-archive>`.

The parts of this command are:

* `tar` - The tar command which is used to create archives
* `-cvf` - Options to create a tar archive (`-c`), use a file as the archive (`-f`) and create the archive in verbose mode (`-v`)
* `archive.tar.gz` - The name of the archive to be created
* `-I pigz` - Option to specify an external compression program (in this case `pigz`)
* `-p 4` - Option to specify the number of threads to use for compression (in this case 4)
* `<files-to-archive>` - The files to be archived

## Helpful links

* [Tar command manual](https://www.gnu.org/software/tar/manual/html_node/tar_112.html)
* [Pigz manual](http://zlib.net/pigz/pigz.pdf)

onelinerhub: [How can I use tar gzip to create a multithreaded archive?](https://onelinerhub.com/cli-tar/how-can-i-use-tar-gzip-to-create-a-multithreaded-archive)