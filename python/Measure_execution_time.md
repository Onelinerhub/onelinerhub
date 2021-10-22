# How to measure time of execution

```python
import timeit

sample = """[4,8,17,84,26].sort()""" #code for which execution time is calculated
time = timeit.timeit(code,1)
print("Excetion time : "+time+"seconds")
```      

- timeit.timeit(code,number) - Finds execution in seconds for the given code 
- code - code for which execution time is calculated
- number - number of times code has to be executed