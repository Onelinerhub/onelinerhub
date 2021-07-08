# Run certain program in multiple threads (processes)

```ini
[program:prcs]
...
numprocs=3
process_name=%(program_name)s_%(process_num)02d
```

- \[program:prcs\] - program configuration block
- numprocs=3 - amount of processes (threads) to launch (```3``` in our example)
- process_name - this should be defined to differ between threads by name
- %(program_name) - will substitute with the name of the program (```prcs```)
- %(process_num)02d - process number (doudle digit format)
