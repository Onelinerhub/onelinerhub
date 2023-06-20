# How do I create a tar.gz file using a shell script?
// plain

A tar.gz file is a compressed archive created using the tar command and gzip compression. To create a tar.gz file using a shell script, use the following code:

```
#!/bin/bash

# Create a tar.gz archive
tar -czvf archive.tar.gz /path/to/directory
```

This code will create a tar.gz archive of the directory at `/path/to/directory`.

The code consists of the following parts:

- `#!/bin/bash` - This is the shebang line which tells the shell which interpreter to use.
- `tar -czvf archive.tar.gz /path/to/directory` - This is the command which does the actual archiving. The `-c` flag creates an archive, `-z` compresses the archive with gzip, `-v` enables verbose output, and `-f` specifies the output file.

For more information, see the [GNU tar manual](https://www.gnu.org/software/tar/manual/html_node/tar_49.html).

onelinerhub: [How do I create a tar.gz file using a shell script?](https://onelinerhub.com/cli-tar/how-do-i-create-a-tar-gz-file-using-a-shell-script)