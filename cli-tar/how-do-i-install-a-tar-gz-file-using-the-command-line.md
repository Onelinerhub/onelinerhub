# How do I install a tar.gz file using the command line?
// plain

Installing a tar.gz file using the command line is a simple process.

1. First, you need to extract the file:
```
tar -xvzf file.tar.gz
```
This will extract the file into the current directory.

2. Next, you need to navigate to the directory with the extracted files:
```
cd file
```

3. Finally, you can install the files:
```
./configure
make
make install
```
The `configure` command prepares the files for installation, the `make` command compiles the files, and the `make install` command installs the files.

## Code explanation
**
* `tar -xvzf file.tar.gz`: Extract the file
* `cd file`: Navigate to the extracted files directory
* `./configure`: Prepare the files for installation
* `make`: Compile the files
* `make install`: Install the files

**## Helpful links**
* [GNU tar manual](https://www.gnu.org/software/tar/manual/tar.html)
* [Linux Tutorial - Installing tar.gz and tar.bz2 Files](https://www.linuxnix.com/linuxunix-install-tar-gz-tar-bz2-files/)

onelinerhub: [How do I install a tar.gz file using the command line?](https://onelinerhub.com/cli-tar/how-do-i-install-a-tar-gz-file-using-the-command-line)