# How to push forked repository to original master

```bash
git remote add upstream https://github.com/Onelinerhub/onelinerhub.git
git fetch upstream
git push origin main
```

- `git` - base command
- `remote add` - add new remote
- `upstream` - name of the remote
- `https://github.com/Onelinerhub/onelinerhub.git` - original repository URL (the one we've forked from)
- `fetch upstream` - update git data from upstream (original repo)
- `push` - send your changes to specified remote
- `origin main` - send changes to original repo, `main` (usually master) branch

group: forks


