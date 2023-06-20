# How can I make tar archives rsyncable with gzip compression?
// plain

Using `rsync` and `gzip` together is an efficient way to create tar archives that can be synchronized between two locations. The basic command for this is as follows:

```
rsync -avz --compress-level=9 <source_dir> <destination_dir>
```

This command will compress the files in the `<source_dir>` directory with `gzip` and then transfer them to the `<destination_dir>` directory using `rsync`.

The `-a` flag stands for "archive mode" and preserves the original file permissions, ownership, and timestamps. The `-v` flag stands for "verbose" and will output what files are being transferred. The `-z` flag stands for "compress" and will compress the files before transferring them.

The `--compress-level` flag specifies the level of compression used by `gzip`. A value of `9` is the highest level of compression and is recommended for most cases.

In addition, `tar` can be used to create an archive of the source directory before transferring it. This can be done with the following command:

```
tar -czvf <archive_name>.tar.gz <source_dir>
```

The `-c` flag stands for "create" and will create an archive. The `-z` flag stands for "compress" and will compress the archive with `gzip`. The `-v` flag stands for "verbose" and will output the files being added to the archive. The `-f` flag stands for "file" and specifies the name of the archive.

Once the archive is created, it can be transferred to the destination directory using `rsync`:

```
rsync -avz <archive_name>.tar.gz <destination_dir>
```

This command will transfer the archive to the `<destination_dir>` directory using `rsync`.

## Code explanation
**

- `rsync -avz --compress-level=9 <source_dir> <destination_dir>`: Compresses the files in the `<source_dir>` directory with `gzip` and then transfers them to the `<destination_dir>` directory using `rsync`.
- `tar -czvf <archive_name>.tar.gz <source_dir>`: Creates an archive of the `<source_dir>` directory and compresses it with `gzip`.
- `rsync -avz <archive_name>.tar.gz <destination_dir>`: Transfers the archive to the `<destination_dir>` directory using `rsync`.

**## Helpful links**

- [rsync Documentation](https://rsync.samba.org/documentation.html)
- [tar Documentation](https://www.gnu.org/software/tar/manual/tar.html)

onelinerhub: [How can I make tar archives rsyncable with gzip compression?](https://onelinerhub.com/cli-tar/how-can-i-make-tar-archives-rsyncable-with-gzip-compression)