# How do I use the tar command in the command line?
// plain

The `tar` command is a powerful tool for archiving and compressing files. It is used in the command line to create, extract, and modify archives.

To create an archive with `tar`, the basic syntax is:

```
tar -cf <archive_name.tar> <files_to_archive>
```

The `-c` flag tells `tar` to create an archive, and the `-f` flag allows you to specify the file name of the archive.

To extract files from an archive, the basic syntax is:

```
tar -xf <archive_name.tar>
```

The `-x` flag tells `tar` to extract the files from the archive, and the `-f` flag allows you to specify the file name of the archive.

Additionally, `tar` supports a variety of flags for modifying archives, such as `-z` for compressing with gzip, `-j` for compressing with bzip2, and `-v` for verbose output.

For more information about `tar`, see the following links:

* [GNU tar manual](https://www.gnu.org/software/tar/manual/html_node/tar_toc.html)
* [Linux man page for tar](http://man7.org/linux/man-pages/man1/tar.1.html)

onelinerhub: [How do I use the tar command in the command line?](https://onelinerhub.com/cli-tar/how-do-i-use-the-tar-command-in-the-command-line)