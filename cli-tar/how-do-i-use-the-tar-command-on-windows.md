# How do I use the tar command on Windows?
// plain

The `tar` command is used to create and extract files in a tar archive format. On Windows, the `tar` command is available in the Windows Subsystem for Linux (WSL). To use `tar` on Windows, you must first install WSL and then install the appropriate version of `tar` for your system.

To create a tar archive, use the following command:
```
tar -cvf archive.tar file1 file2 file3
```
This will create a `archive.tar` file containing the files `file1`, `file2`, and `file3`.

To extract the contents of a tar archive, use the following command:
```
tar -xvf archive.tar
```
This will extract the contents of `archive.tar` into the current working directory.

The following list provides a description of the individual parts of the `tar` command:
- `tar`: The command itself.
- `-cvf`: The flags used to indicate the action to be taken (create/extract) and the format of the archive (tar).
- `archive.tar`: The name of the tar archive to be created/extracted.
- `file1`, `file2`, `file3`: The files to be included in the tar archive.

For more information, see the following links:
- [Windows Subsystem for Linux Installation Guide for Windows 10](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
- [tar Manual](https://www.gnu.org/software/tar/manual/tar.html)

onelinerhub: [How do I use the tar command on Windows?](https://onelinerhub.com/cli-tar/how-do-i-use-the-tar-command-on-windows)