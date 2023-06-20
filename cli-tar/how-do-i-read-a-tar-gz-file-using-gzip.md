# How do I read a tar.gz file using gzip?
// plain

**Reading a tar.gz file using gzip**

1. To read a tar.gz file using gzip, first you need to make sure that gzip is installed on your system.

2. Then you can use the following command to read the tar.gz file:

```
gzip -d <filename>.tar.gz
```

3. This will create a tar file with the same name as the tar.gz file, but without the .gz extension.

4. To extract the contents of the tar file, use the following command:

```
tar -xvf <filename>.tar
```

5. This will extract the contents of the tar file into the current directory.

6. To delete the tar file after extracting its contents, use the following command:

```
rm <filename>.tar
```

7. This will delete the tar file from the current directory.

## Helpful links
* [Gzip Manual](https://www.gnu.org/software/gzip/manual/gzip.html)
* [Tar Manual](https://www.gnu.org/software/tar/manual/tar.html)

onelinerhub: [How do I read a tar.gz file using gzip?](https://onelinerhub.com/cli-tar/how-do-i-read-a-tar-gz-file-using-gzip)