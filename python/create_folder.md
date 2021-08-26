# Creating a folder

```python
import os
foo = os.getlogin()
os.mkdir(f'C:\\Users\\{foo}\\Desktop')
```

- os - library to get operating system commands
- os.getlogin() - returns the username of the computer
- os.mkdir( - creates folder, specified in the arguments
