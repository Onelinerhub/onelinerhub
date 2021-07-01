# Update programs and remove unused packages

```bash
sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get autoremove -y
```

- sudo - Super User DO command.
- apt-get - Advanced Packaging Tool.
- update - Resynchronize the package index files from source.
- upgrade - Install the newest versions of packages.
- autoremove - Remove all packages which are already installed and no longer needed.
- -y - Automatic answer "yes" to the prompts.
