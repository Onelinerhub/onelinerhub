# Change directory and all dependencies permissions

```bash
find /home/usr/ -type d -exec chmod 777 {} \;
```

* ```/home/usr/``` - Base path to change permissions.
* ```-type d``` - Search for directories (affects files too).
* ```-exec``` - Execute next command.
* ```chmod 777``` - Grants all permissions to all users. The tables explain their meanings:

Number Position | Affects
:---: | :---:
First | user
Second | group
Third | others

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

* ```{}``` - Will be replaced by the path.
* ```\;``` - Denotes the end of command.