# How to use tar shell to manage cash?
// plain

Using the tar shell command, you can manage your cash in a few different ways. Here is an example of how to use tar to compress a directory containing cash:

```
tar -czvf cash.tar.gz cash_directory
```

This command will compress the cash_directory and store it in a tarball called cash.tar.gz.

## Code explanation


- tar: the tar command
- -czvf: flags to compress, create, verbosely list files, and use the archive file specified
- cash.tar.gz: the name of the tarball
- cash_directory: the directory containing the cash

You can also use tar to extract the cash from the tarball:

```
tar -xzvf cash.tar.gz
```

This will extract the contents of the tarball, cash.tar.gz, into the current directory.

## Code explanation


- tar: the tar command
- -xzvf: flags to extract, verbosely list files, and use the archive file specified
- cash.tar.gz: the name of the tarball

For more information, see the following links:

- [tar manual](https://www.gnu.org/software/tar/manual/tar.html)
- [How to Use Tar Command to Create Archives in Linux](https://www.tecmint.com/tar-command-examples-in-linux/)

onelinerhub: [How to use tar shell to manage cash?](https://onelinerhub.com/cli-tar/how-to-use-tar-shell-to-manage-cash)