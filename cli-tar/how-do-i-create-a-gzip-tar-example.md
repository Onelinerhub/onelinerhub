# How do I create a gzip tar example?
// plain

Creating a gzip tar example is a simple process. First, create a directory and populate it with files that you want to compress.

```
mkdir example
echo "This is a test" > example/test.txt
```

Next, use the tar command to create a tar archive of the directory.

```
tar -cf example.tar example/
```

Finally, use the gzip command to compress the tar archive.

```
gzip example.tar
```

The resulting file, `example.tar.gz` is a gzip compressed tar archive.

## Code explanation


1. `mkdir example`: creates a directory called `example`
2. `echo "This is a test" > example/test.txt`: creates a file called `test.txt` in the `example` directory
3. `tar -cf example.tar example/`: creates a tar archive of the `example` directory
4. `gzip example.tar`: compresses the tar archive with gzip

## Helpful links

- [tar command](https://www.computerhope.com/unix/utar.htm)
- [gzip command](https://www.computerhope.com/unix/ugzip.htm)

onelinerhub: [How do I create a gzip tar example?](https://onelinerhub.com/cli-tar/how-do-i-create-a-gzip-tar-example)