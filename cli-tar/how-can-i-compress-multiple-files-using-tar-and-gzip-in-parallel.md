# How can I compress multiple files using tar and gzip in parallel?
// plain

Using GNU Parallel, you can compress multiple files using tar and gzip in parallel. To do this, you need to create a tar archive of the files you want to compress and then pass the tar archive to gzip.

The following example code will compress the files `file1.txt` and `file2.txt` into `files.tar.gz`:

```
tar cvf files.tar file1.txt file2.txt
gzip files.tar
```

The output of the above code will be:

```
file1.txt
file2.txt
```

To compress these files in parallel, you can use the following command:

```
parallel gzip ::: files.tar
```

The output of the above command will be:

```
files.tar.gz
```

The code can be broken down as follows:

- `parallel`: This is the command for running commands in parallel.
- `gzip`: This is the command for compressing files using gzip.
- `:::`: This is the separator for the list of files to be compressed.
- `files.tar`: This is the tar archive containing the files to be compressed.

## Helpful links

- [GNU Parallel Documentation](https://www.gnu.org/software/parallel/)
- [Gzip Documentation](https://www.gnu.org/software/gzip/)

onelinerhub: [How can I compress multiple files using tar and gzip in parallel?](https://onelinerhub.com/cli-tar/how-can-i-compress-multiple-files-using-tar-and-gzip-in-parallel)