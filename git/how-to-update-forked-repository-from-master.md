# How to update forked repository from master

```bash
git remote add upstream https://github.com/Onelinerhub/onelinerhub.git
git fetch upstream
git pull upstream main
```

- `git` - base command
- `remote add` - add new remote
- `upstream` - name of the remote
- `https://github.com/Onelinerhub/onelinerhub.git` - original repository URL (the one we've forked from)
- `fetch upstream` - update git data from upstream (original repo)
- `pull` - gets updated data from remote
- `upstream main` - get changes from original repo, `main` (usually master) branch

group: forks


