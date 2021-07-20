# Run GUI commands (export display)

```ini
[program:name]
command=php /home/user/gui.php
environment=DISPLAY=:0
```

- name - pick any name for the process you want to run
- command - command executable (php script in our case)
- DISPLAY=:0 - set display environment variable to enable GUI apps
