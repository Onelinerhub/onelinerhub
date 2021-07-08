# Make supervisor kill a program when stopping it.

```ini
[program:prcs]
...
stopsignal=KILL
```

- \[program:prcs\] - program configuration block
- stopsignal - defines stop signal to send to the program on stop
- KILL - send ```KILL``` signal (can be any of ``TERM, HUP, INT, QUIT, KILL, USR1, USR2``)
