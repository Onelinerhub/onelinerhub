# How can I use sed in a CLI for Kubernetes?
// plain

Sed is a powerful command line tool that can be used for text processing in Kubernetes. It can be used to search, find and replace text, delete lines, and perform many other operations.

Here is an example of how to use sed to search for a string in a file and replace it with a new string:

```
$ sed 's/oldstring/newstring/g' filename
```

The command above will replace all occurrences of the string "oldstring" with "newstring" in the file called "filename".

You can also use sed to delete lines in a file that contain a certain string. For example, the following command will delete all lines that contain the string "oldstring":

```
$ sed '/oldstring/d' filename
```

The output of the command above will be the file "filename" with all lines containing "oldstring" removed.

Sed can also be used to perform other operations, such as inserting lines, appending lines, and more. For more information on how to use sed with Kubernetes, see the official Kubernetes documentation [here](https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#using-sed-to-modify-files).

**Code Parts Explanation**

- `sed 's/oldstring/newstring/g' filename` - This command searches for the string "oldstring" and replaces it with "newstring" in the file called "filename".
- `sed '/oldstring/d' filename` - This command deletes all lines that contain the string "oldstring" in the file called "filename".

onelinerhub: [How can I use sed in a CLI for Kubernetes?](https://onelinerhub.com/cli-sed/how-can-i-use-sed-in-a-cli-for-kubernetes)