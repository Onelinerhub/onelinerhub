# How do I compare Unix tar and zip files?
// plain

**Comparing Unix tar and zip files**

Unix tar and zip files are both archive formats used to package multiple files into a single file for easier storage and transport.

The two formats differ in their compression algorithms. Unix tar does not compress the files, while zip files use a lossless compression algorithm to reduce file size.

To compare the two formats, one can use the Unix command line. The following example code uses the `tar` and `zip` commands to compare the size of two files:

```
$ ls -lh file1.txt file2.txt
-rw-r--r--  1 user  staff   4.0K Feb 20 12:00 file1.txt
-rw-r--r--  1 user  staff   8.0K Feb 20 12:00 file2.txt

$ tar -cf files.tar file1.txt file2.txt
$ zip files.zip file1.txt file2.txt

$ ls -lh files.tar files.zip
-rw-r--r--  1 user  staff   12K Feb 20 12:02 files.tar
-rw-r--r--  1 user  staff   8.2K Feb 20 12:02 files.zip
```

The output of the commands shows that the zip file is smaller than the tar file, since the zip file was compressed.

In conclusion, zip files are generally smaller than tar files, but tar files have the advantage of not requiring any additional software to open the archive.

## Helpful links

- [Unix Tar Command Tutorial](https://www.linode.com/docs/tools-reference/tools/using-the-tar-command-in-linux/)
- [Unix Zip Command Tutorial](https://www.linode.com/docs/tools-reference/tools/using-the-zip-command-in-linux/)

onelinerhub: [How do I compare Unix tar and zip files?](https://onelinerhub.com/cli-tar/how-do-i-compare-unix-tar-and-zip-files)