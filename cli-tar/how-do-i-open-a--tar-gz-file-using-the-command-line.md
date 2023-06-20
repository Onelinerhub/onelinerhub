# How do I open a .tar.gz file using the command line?
// plain

Using the command line, you can open a .tar.gz file with the following command:

```
tar -xzvf filename.tar.gz
```

The command has four parts:

1. `tar`: This command is used to create, modify, and extract files from an archive.
2. `-x`: This flag tells `tar` to extract the files from the archive.
3. `-z`: This flag tells `tar` to uncompress the archive using gzip.
4. `-vf`: This flag tells `tar` to be verbose and display the progress of the extraction.

The output of the command will look something like this:

```
x filename1
x filename2
x filename3
```

This indicates that the files `filename1`, `filename2`, and `filename3` were successfully extracted from the archive.

## Helpful links

- [GNU tar Manual](https://www.gnu.org/software/tar/manual/html_node/tar_49.html)
- [How to Extract tar.gz Files](https://www.howtogeek.com/248780/how-to-extract-files-from-a-tar-ball-in-linux/)

onelinerhub: [How do I open a .tar.gz file using the command line?](https://onelinerhub.com/cli-tar/how-do-i-open-a--tar-gz-file-using-the-command-line)