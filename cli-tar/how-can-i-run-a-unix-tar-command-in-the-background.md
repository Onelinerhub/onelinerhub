# How can I run a Unix tar command in the background?
// plain

To run a Unix tar command in the background, you need to use the `nohup` command. This command allows you to run the command after you log out of the terminal session.

For example, to run the tar command `tar -cvf archive.tar /home/user/Documents` in the background, you can use the following command: `nohup tar -cvf archive.tar /home/user/Documents &`

The output of this command will be:
```
[1] 1234
```

## Code explanation

- `nohup`: This command allows the command to run after the user logs out of the terminal session.
- `tar -cvf archive.tar /home/user/Documents`: This is the command to create an archive of the `/home/user/Documents` directory.
- `&`: This symbol is used to run the command in the background.

## Helpful links
- [nohup](https://linux.die.net/man/1/nohup)
- [tar](https://linux.die.net/man/1/tar)

onelinerhub: [How can I run a Unix tar command in the background?](https://onelinerhub.com/cli-tar/how-can-i-run-a-unix-tar-command-in-the-background)