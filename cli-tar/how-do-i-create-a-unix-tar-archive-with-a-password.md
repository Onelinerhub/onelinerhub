# How do I create a Unix tar archive with a password?
// plain

Creating a Unix tar archive with a password is done using the tar command in combination with the gpg command.

The following example code will create a tar archive named `archive.tar` and encrypt it with a password `password`:
```
tar -cvf archive.tar file1 file2
gpg -c --cipher-algo AES256 archive.tar
```
The output of the command should be:
```
Enter passphrase:
Repeat passphrase:
```

The code has the following parts:

1. `tar -cvf archive.tar file1 file2`: This creates a tar archive named `archive.tar` containing the files `file1` and `file2`.
2. `gpg -c --cipher-algo AES256 archive.tar`: This command encrypts the tar archive `archive.tar` using the AES256 algorithm and prompts the user for a passphrase.

## Helpful links

- [GNU Tar Manual](https://www.gnu.org/software/tar/manual/tar.html)
- [GnuPG Manual](https://www.gnupg.org/documentation/manuals/gnupg/)

onelinerhub: [How do I create a Unix tar archive with a password?](https://onelinerhub.com/cli-tar/how-do-i-create-a-unix-tar-archive-with-a-password)