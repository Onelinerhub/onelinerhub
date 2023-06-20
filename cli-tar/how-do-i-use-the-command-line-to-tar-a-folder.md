# How do I use the command line to tar a folder?
// plain

Using the command line to tar a folder is a simple process.

First, navigate to the folder you wish to tar using the `cd` command. Then, use the `tar` command to create a tar archive. The syntax for this command is as follows: `tar -cvf <name_of_tar_archive>.tar <name_of_folder_to_tar>`. For example, to create a tar archive of a folder named 'my_folder', the command would be:

```
tar -cvf my_folder.tar my_folder
```

This command will create a tar archive named `my_folder.tar` in the current directory.

The parts of this command are as follows:
* `tar`: The tar command is used to create archives of files.
* `-cvf`: This is a set of flags used to indicate the action (create archive) and the format (tar).
* `my_folder.tar`: This is the name of the tar archive that will be created.
* `my_folder`: This is the name of the folder that will be archived.

For more information on using the `tar` command, see the [GNU tar manual](https://www.gnu.org/software/tar/manual/tar.html).

onelinerhub: [How do I use the command line to tar a folder?](https://onelinerhub.com/cli-tar/how-do-i-use-the-command-line-to-tar-a-folder)