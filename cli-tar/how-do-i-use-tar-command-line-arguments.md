# How do I use tar command line arguments?
// plain

The `tar` command line utility is used to store, list, and extract files from an archive file. The command line arguments used with `tar` can be broken down into the following categories:

1. **Create an archive**
    - `-c`: Create an archive
    - `-f`: Specify the filename of the archive
    - `-v`: Display progress information
    - `-z`: Compress the archive with gzip
    - `-j`: Compress the archive with bzip2

## Example


```
tar -cvf my_archive.tar ./my_folder
```

2. **List the contents of an archive**
    - `-t`: List the contents of an archive

## Example


```
tar -tf my_archive.tar
```

3. **Extract files from an archive**
    - `-x`: Extract files from an archive

## Example


```
tar -xf my_archive.tar
```

For more information, see the [GNU tar manual](https://www.gnu.org/software/tar/manual/tar.html).

onelinerhub: [How do I use tar command line arguments?](https://onelinerhub.com/cli-tar/how-do-i-use-tar-command-line-arguments)