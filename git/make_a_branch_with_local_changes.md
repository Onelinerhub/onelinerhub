# Make a new branch with uncommitted changes
Do you ever make changes to `main`/`master`, then realise that you haven't made a branch?

```git
git checkout -b example/example-changes
git commit -am "Change example"
```

- `git checkout` - navigate to the following branch
- `-b` - create a new branch
- `example/example-changes` - name of the new branch
- `git commit` - commit the changes to the new branch
- `-am` - commit all the changed files with a message
- `"Change example"` - the commit message