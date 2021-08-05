# Calculate the size of directory in bytes.

run this in terminal

```python
python -c "import os;print(sum(os.path.getsize(f) for f in os.listdir('.') if os.path.isfile(f)), 'bytes')"
```

- `-c` flag - allows the execution of statements following the flag
- `import os` - use os module
- `os.listdir('.')` - list all contents of current directory
- `os.path.isfile(f)` - determine if `f` is a file
- `os.path.getsize(f)` - get size of file `f`
