# How to sort list, tupe, set, ...

```python
sorted_list = sorted(iterable_name, key=function, reverse=False)
```

- sorted_list - contain sorted list (any iterable converts to list)
- sorted - built-in function to sort iterables in python
- iterable_name - iterable you want to sort(it can be list, tuple, set, ...)
- function - function to sort iterable by it. its usually lambda. by default its None and sort by default function.
- reverse - reverse the sorting if its True by default its False
