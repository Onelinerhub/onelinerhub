# Change permissions using chmod in bash

```bash
chmod 777 /path
```

- chmod - changes permissions of file or directory
- 777 - allow read and write for all users
- /path - path to dir (or file) to change permissions of

Number | Permission Type | Symbol
:---: | :---: | :---:
0 | No Permission | ---
1 | Execute | --x
2 | Write | -w-
3 | Execute + Write | -wx
4 | Read | r--
5 | Read + Execute | r-x
6 | Read + Write | rw-
7 | Read + Write + Execute | rwx

group: chmod
