# How do I install a tar.gz file using the terminal?
// plain

Installing a tar.gz file using the terminal can be done in a few simple steps.

1. First, download the tar.gz file to your computer.

2. Then, open the terminal and navigate to the folder containing the tar.gz file.

3. Extract the contents of the tar.gz file with the command:

```
tar -xzvf <filename>.tar.gz
```

This will extract the contents of the tar.gz file into the same directory.

4. Change to the extracted directory with the command:

```
cd <filename>
```

5. Run the installation script with the command:

```
./configure
```

This will configure the installation.

6. Finally, install the application with the command:

```
make
sudo make install
```

This will install the application.

## Helpful links
- [How to Install Tar.gz Files in Linux](https://www.howtogeek.com/248780/how-to-extract-and-create-tar-gz-files-in-linux/)
- [GNU Tar Manual](https://www.gnu.org/software/tar/manual/tar.html)

onelinerhub: [How do I install a tar.gz file using the terminal?](https://onelinerhub.com/cli-tar/how-do-i-install-a-tar-gz-file-using-the-terminal)