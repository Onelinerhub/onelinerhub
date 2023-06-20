# How do I remove the absolute path when using the Unix tar command?
// plain

The Unix tar command can be used to create archives of files and directories. To remove the absolute path when using the tar command, you can use the `--transform` option. This option allows you to specify a transformation to be applied to the paths stored in the archive.

For example, the following command will create an archive of the `/home/user/example` directory without the absolute path:

```
tar --transform 's,^/home/user/,,' -cvf example.tar /home/user/example
```

The output of this command should look something like this:

```
example/
example/file1
example/file2
example/file3
```

The `--transform` option takes two arguments: a regular expression and a replacement string. In this example, the regular expression `^/home/user/` matches the absolute path, and the replacement string is an empty string, which results in the absolute path being removed from the archive.

Here are some more resources for learning more about the `--transform` option:

- [GNU tar manual](https://www.gnu.org/software/tar/manual/html_node/transform.html)
- [Stack Overflow: How to use tar with absolute paths](https://stackoverflow.com/questions/19253800/how-to-use-tar-with-absolute-paths)

onelinerhub: [How do I remove the absolute path when using the Unix tar command?](https://onelinerhub.com/cli-tar/how-do-i-remove-the-absolute-path-when-using-the-unix-tar-command)