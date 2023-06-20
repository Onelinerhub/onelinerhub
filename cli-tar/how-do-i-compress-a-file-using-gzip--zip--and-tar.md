# How do I compress a file using gzip, zip, and tar?
// plain

**Gzip**

Gzip is a popular file compression program that is used to create .gz files. To compress a file using gzip, you can use the following command:

```
gzip filename
```

This command will create a new .gz file with the same name as the original file. To decompress the file, you can use the following command:

```
gunzip filename.gz
```

**Zip**

Zip is a popular file compression program that is used to create .zip files. To compress a file using zip, you can use the following command:

```
zip filename.zip filename
```

This command will create a new .zip file with the same name as the original file. To decompress the file, you can use the following command:

```
unzip filename.zip
```

**Tar**

Tar is a popular file archiving program that is used to create .tar files. To compress a file using tar, you can use the following command:

```
tar -cvf filename.tar filename
```

This command will create a new .tar file with the same name as the original file. To decompress the file, you can use the following command:

```
tar -xvf filename.tar
```

The `-c` flag is used to create a new archive, the `-v` flag is used to display the progress of the operation, and the `-f` flag is used to specify the name of the archive.

## Helpful links
* [Gzip](https://www.gnu.org/software/gzip/)
* [Zip](https://infozip.sourceforge.io/)
* [Tar](https://www.gnu.org/software/tar/)

onelinerhub: [How do I compress a file using gzip, zip, and tar?](https://onelinerhub.com/cli-tar/how-do-i-compress-a-file-using-gzip--zip--and-tar)