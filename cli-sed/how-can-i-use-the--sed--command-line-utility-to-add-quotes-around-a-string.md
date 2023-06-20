# How can I use the 'sed' command line utility to add quotes around a string?
// plain

The `sed` command line utility can be used to add quotes around a string. The syntax is as follows:

```
sed 's/^/"/; s/$/"/'
```

This command will add double quotes around the string. The `s` in the command stands for substitute, and the `^` and `$` symbols stand for the beginning and end of the string respectively.

The following example will add double quotes around the string `Hello World`:

```
echo "Hello World" | sed 's/^/"/; s/$/"/'
```

The output of this command is:

```
"Hello World"
```

If you want to use single quotes instead of double quotes, you can use the following command:

```
echo "Hello World" | sed "s/^/'/; s/$/'/"
```

The output of this command is:

```
'Hello World'
```

## Helpful links

- [Sed Command Tutorial](https://www.guru99.com/sed-command-linux-examples.html)
- [Sed Manual](https://www.gnu.org/software/sed/manual/sed.html)

onelinerhub: [How can I use the 'sed' command line utility to add quotes around a string?](https://onelinerhub.com/cli-sed/how-can-i-use-the--sed--command-line-utility-to-add-quotes-around-a-string)