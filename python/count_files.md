# Count numbers of files in current directory

```bash
python -c "import os;print(len(os.listdir(os.getcwd())))"
```

- -c - flag allows the execution of statements following the flag
- import os - use os module
- os.getcwd() - get path to current (working) directory
- os.listdir( - list all contents of directory
