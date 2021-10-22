# How to measure time of execution

```python
import time
start_time = time.time()
# code to measure goes here
print("--- %s seconds ---" % (time.time() - start_time))
```      

- import time - module to manipulate time
- start_time - Saves the start time
- time.time() - start_time - calculates delta between current time and time before code execution
- "--- %s seconds ---" % - formats execution time

## Example
```python
import time, random
start_time = time.time()
time.sleep(random.random())
print("--- %s seconds ---" % (time.time() - start_time))
```
```bash
--- 0.8802111148834229 seconds ---
```
