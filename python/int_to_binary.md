# Convert integer to binary

```python
binary = f"{num:#016b}"
```

- num - integer value
- \# - `0b` prefix
- 0 - prepend leading zeros
- 16 - bit length
- b - binary format

## Examples

32-bit with prefix and leading zeros

```python
binary = f"{123:#032b}" # "0b00000000000000000000000001111011"
```

8-bit without prefix and leading zeros

```python
binary = f"{123:8b}" # "1111011"
```

8-bit without prefix and leading zeros (alternative)

```python
binary = bin(123) # "1111011"
```
