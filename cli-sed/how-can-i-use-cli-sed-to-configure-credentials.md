# How can I use cli sed to configure credentials?
// plain

The `sed` command line utility can be used to configure credentials in a text file. `sed` is a stream editor that allows you to search for and replace strings in a file.

For example, to replace the `username` and `password` strings in a file called `credentials.txt`, you could use the following command:

```
sed -i 's/username/myusername/g; s/password/mypassword/g' credentials.txt
```

This command will replace all occurrences of `username` with `myusername` and `password` with `mypassword` in the `credentials.txt` file.

## Code explanation


* `sed` - The command line utility used to search and replace strings in a file.
* `-i` - The option used to edit the file in place.
* `'s/username/myusername/g; s/password/mypassword/g'` - The search and replace command used to replace `username` with `myusername` and `password` with `mypassword`.
* `credentials.txt` - The file containing the credentials to be configured.

## Helpful links

* [Sed Tutorial](https://www.grymoire.com/Unix/Sed.html)
* [Sed Manual](https://www.gnu.org/software/sed/manual/sed.html)

onelinerhub: [How can I use cli sed to configure credentials?](https://onelinerhub.com/cli-sed/how-can-i-use-cli-sed-to-configure-credentials)