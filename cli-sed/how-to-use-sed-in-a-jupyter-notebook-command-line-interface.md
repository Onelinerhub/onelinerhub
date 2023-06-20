# How to use sed in a Jupyter Notebook command line interface?
// plain

Sed (stream editor) is a powerful command-line tool for manipulating text. It can be used in a Jupyter Notebook command line interface (CLI) to perform various text processing tasks. Here is an example of how to use sed in a Jupyter Notebook CLI:

```
$ echo "This is a test string" | sed 's/test/example/'

This is a example string
```

In this example, the `echo` command is used to output the text `This is a test string`, which is then piped to the `sed` command. The `sed` command then searches for the string `test` and replaces it with `example`, resulting in the output `This is a example string`.

## Code explanation


* `echo "This is a test string"`: Outputs the text `This is a test string`
* `sed 's/test/example/'`: Searches for the string `test` and replaces it with `example`

For more information on how to use sed in a Jupyter Notebook CLI, please refer to the following resources:

* [Sed Tutorial](https://www.grymoire.com/Unix/Sed.html)
* [Using sed with Jupyter Notebook](https://www.jeremyjordan.me/sed-jupyter/)

onelinerhub: [How to use sed in a Jupyter Notebook command line interface?](https://onelinerhub.com/cli-sed/how-to-use-sed-in-a-jupyter-notebook-command-line-interface)