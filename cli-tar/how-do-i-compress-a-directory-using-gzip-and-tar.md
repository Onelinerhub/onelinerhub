# How do I compress a directory using gzip and tar?
// plain

Using gzip and tar together is a convenient way to compress a directory. The following example code will compress a directory called "mydir" into a single gzipped tarball file called "mydir.tar.gz":

```
tar -zcvf mydir.tar.gz mydir
```

The flags used in the command are as follows:

* `-z`: Compress the tarball with gzip
* `-c`: Create a new tarball
* `-v`: Verbosely show the progress
* `-f`: Specify the filename of the tarball

The output of the command should look something like this:

```
$ tar -zcvf mydir.tar.gz mydir
mydir/
mydir/file1.txt
mydir/file2.txt
mydir/subdir1/
mydir/subdir1/file3.txt
mydir/subdir2/
mydir/subdir2/file4.txt
```

For more information, see the [GNU tar manual](https://www.gnu.org/software/tar/manual/html_node/tar_51.html).

onelinerhub: [How do I compress a directory using gzip and tar?](https://onelinerhub.com/cli-tar/how-do-i-compress-a-directory-using-gzip-and-tar)