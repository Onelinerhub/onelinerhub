# How to edit files from the result of find command

```bash
nano $(find . -name "*.js")
```

- find . -name "*.js" - will find all ```js``` files in current directory
- nano - nano will open all found file one by one (```ctrl + x``` will close current file and open the next one)
