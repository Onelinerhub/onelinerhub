# How do I use the tar command in a CMD prompt?
// plain

The tar command is used to create, modify, list, and extract files from an archive file. It is commonly used in Linux and Unix-like operating systems, but can also be used in Windows via the Command Prompt.

To use the tar command in a CMD prompt, first open the Command Prompt by pressing the `Windows` key + `R`, then type `cmd` and press `Enter`.

Once the Command Prompt is open, you can use the tar command. For example, to create an archive file called `myfile.tar` from the contents of the `myfolder` directory, you would use the following command:

```
tar -cvf myfile.tar myfolder
```

This command will create an archive file called `myfile.tar` from the contents of the `myfolder` directory.

To extract the contents of the `myfile.tar` archive file, you would use the following command:

```
tar -xvf myfile.tar
```

This command will extract the contents of the `myfile.tar` archive file into the current directory.

For more information on the tar command, see the [GNU tar manual](https://www.gnu.org/software/tar/manual/tar.html).

onelinerhub: [How do I use the tar command in a CMD prompt?](https://onelinerhub.com/cli-tar/how-do-i-use-the-tar-command-in-a-cmd-prompt)