# How do I use the tar command line in Windows 10?
// plain

The `tar` command line utility is available for Windows 10 through the Windows Subsystem for Linux (WSL). To use it, you must first install WSL and then install a Linux distribution of your choice.

Once you have installed WSL, open a command prompt and type `wsl` to enter the Linux environment. Then you can use the `tar` command to create, extract, and view the contents of a tar file.

For example, to create a tar file called `example.tar` from the folder `myfiles`, you would use the following command:

```
tar -cf example.tar myfiles
```

This will create a tar file of the contents of the `myfiles` folder. To extract the contents of the tar file, you would use the following command:

```
tar -xf example.tar
```

This will extract the contents of `example.tar` into the current directory. To view the contents of the tar file without extracting it, you would use the following command:

```
tar -tf example.tar
```

This will list the contents of `example.tar`.

#### List of code parts
* `tar` - the command to run the tar utility
* `-cf` - create a tar file
* `-xf` - extract the contents of a tar file
* `-tf` - view the contents of a tar file

#### List of relevant links
* [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
* [Tar Command Reference](https://www.computerhope.com/unix/utar.htm)

onelinerhub: [How do I use the tar command line in Windows 10?](https://onelinerhub.com/cli-tar/how-do-i-use-the-tar-command-line-in-windows---)