# How to measure time of execution

```python
import time
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
```      

- start_time - Notes the start time
- main() - Contains the program whose time is to be measured
- ...