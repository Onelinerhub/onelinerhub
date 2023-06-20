# How do I create a gzip tar archive?
// plain

Creating a gzip tar archive is a straightforward process. The following example code creates a tar archive of the current directory, compresses it with gzip, and names it "myarchive.tar.gz":

```
tar -czf myarchive.tar.gz .
```

This command has several parts:

* `tar`: the tar command to create an archive
* `-czf`: the flags for creating a gzip compressed tar archive
* `myarchive.tar.gz`: the name of the resulting archive
* `.`: the directory to be archived

The output of this command will be something like this:

```
$ tar -czf myarchive.tar.gz .
$
```

For more information about creating tar archives with gzip, see the [GNU tar manual](https://www.gnu.org/software/tar/manual/html_node/tar_49.html).

onelinerhub: [How do I create a gzip tar archive?](https://onelinerhub.com/cli-tar/how-do-i-create-a-gzip-tar-archive)