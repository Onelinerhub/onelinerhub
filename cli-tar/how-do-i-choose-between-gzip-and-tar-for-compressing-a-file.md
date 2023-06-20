# How do I choose between gzip and tar for compressing a file?
// plain

When deciding between gzip and tar for compressing a file, there are a few things to consider.

**1. File Type**

Gzip is best used for compressing single files, while tar is better for archiving multiple files.

**2. Compression Ratio**

Gzip generally has a higher compression ratio than tar.

**3. Speed**

Gzip is usually faster than tar since it compresses only one file at a time.

**4. Example Code**

To compress a single file with gzip:

```
gzip filename
```

To compress multiple files into an archive with tar:

```
tar -czvf archive.tar.gz /path/to/files/*
```

**5. Output**

The output of the above commands will be a single compressed file named `filename.gz` and an archive named `archive.tar.gz`, respectively.

**6. Links**

- [Gzip - Wikipedia](https://en.wikipedia.org/wiki/Gzip)
- [Tar - Wikipedia](https://en.wikipedia.org/wiki/Tar_(computing))

onelinerhub: [How do I choose between gzip and tar for compressing a file?](https://onelinerhub.com/cli-tar/how-do-i-choose-between-gzip-and-tar-for-compressing-a-file)