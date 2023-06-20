# How to use sed to modify Kubernetes configuration files from the command line?
// plain

The `sed` command can be used to modify Kubernetes configuration files from the command line. It is a powerful command-line utility for manipulating text.

To use `sed` to modify Kubernetes configuration files, the following syntax can be used:

```
sed -i 's/<old-text>/<new-text>/g' <config-file-name>
```

For example, to replace the string `cluster.local` with `example.com` in the file `config.yaml`:

```
sed -i 's/cluster.local/example.com/g' config.yaml
```

The parameters used in the command are as follows:

- `-i`: This option tells `sed` to edit the file in-place.
- `s`: This parameter tells `sed` to search for a string and replace it with another string.
- `<old-text>`: This is the string that will be replaced.
- `<new-text>`: This is the string that will be used to replace the old string.
- `<config-file-name>`: This is the name of the configuration file to be modified.

For more information about using `sed` to modify Kubernetes configuration files, please refer to the following links:

- [Using sed to modify Kubernetes configuration files](https://kubernetes.io/docs/tasks/administer-cluster/configure-update-cluster/#using-sed-to-modify-kubernetes-configuration-files)
- [sed - An Introduction and Tutorial by Bruce Barnett](http://www.grymoire.com/Unix/Sed.html)

onelinerhub: [How to use sed to modify Kubernetes configuration files from the command line?](https://onelinerhub.com/cli-sed/how-to-use-sed-to-modify-kubernetes-configuration-files-from-the-command-line)