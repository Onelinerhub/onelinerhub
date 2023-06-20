# How can I use the CLI to edit files on GitHub?
// plain

The CLI (Command Line Interface) can be used to edit files on GitHub. To do this, you'll need to install Git, which is a version control system for tracking changes in computer files and coordinating work on those files among multiple people.

Once Git is installed, you can use the `git clone` command to clone a repository from GitHub to your local machine. This will create a local copy of the repository where you can make changes and commit them to the remote repository.

For example, to clone the repository `example/repo` from GitHub, you can run the following command:
```
git clone https://github.com/example/repo.git
```

Once you have the repository cloned to your local machine, you can edit the files using any text editor. When you're finished, you can commit your changes to the remote repository using `git commit` and `git push`.

Here's an example of how you might commit and push changes to the remote repository:
```
git add <file>
git commit -m "Commit message"
git push
```

The `git add` command adds the specified file to the staging area. The `git commit` command commits the changes to the local repository, and the `git push` command pushes the changes to the remote repository.

## Helpful links
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Documentation](https://docs.github.com/en/github)

onelinerhub: [How can I use the CLI to edit files on GitHub?](https://onelinerhub.com/cli-sed/how-can-i-use-the-cli-to-edit-files-on-github)