# How do I install a tar.gz file using the command line?
// plain

Installing a tar.gz file using the command line is easy.

First, navigate to the directory containing the tar.gz file you wish to install.

```
$ cd /path/to/directory/
```

Next, use the `tar` command to unpack the tar.gz file.

```
$ tar -xzf filename.tar.gz
```

This will unpack the contents of the tar.gz file into the current directory.

If you wish to extract the tar.gz file to a specific directory, use the `-C` flag.

```
$ tar -xzf filename.tar.gz -C /path/to/directory
```

Finally, you can use the `make` command to install the contents of the tar.gz file.

```
$ make
```

This will compile and install the contents of the tar.gz file.

#### List of Code Parts

* `cd`: navigate to the directory containing the tar.gz file
* `tar -xzf`: unpack the tar.gz file
* `-C`: extract the tar.gz file to a specific directory
* `make`: compile and install the contents of the tar.gz file

#### Relevant Links

* [How to Unpack and Install Tar.gz Files in Linux](https://www.howtogeek.com/248780/how-to-unpack-and-install-tar-gz-files-in-linux/)

onelinerhub: [How do I install a tar.gz file using the command line?](https://onelinerhub.com/cli-tar/how-do-i-install-a-tar-gz-file-using-the-command-line-1687282582)