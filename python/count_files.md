# Count numbers of files in current directory

```bash
python -c "import os;print(len(os.listdir(os.getcwd())))"
```

- `-c` - <p>flag allows the execution of statements following the flag</p>
- `import os` - <p>use os module</p>
- `os.getcwd()` - <p>get path to current (working) directory</p>
- `os.listdir(` - <p>list all contents of directory</p>

## Example: 
```bash
import os; print(len(os.listdir(os.getcwd())))
```
```
1

```
