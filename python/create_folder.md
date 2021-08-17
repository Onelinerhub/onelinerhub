# Creating a folder

```python
import os
foo = os.getlogin()
os.mkdir(f'C:\\Users\\{foo}\\Desktop')
```

- os - library imported to get operating system commands
- os.getlogin() - function that returns the username of the computer
- os.mkdir(path) - function that creates the folder. Pass the argument in the "path" to specify where the folder will be created
