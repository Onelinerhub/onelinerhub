# How to zero pad a number

```python
padded = "{:05d}".format(number)
```

- `padded` - will contain zero-padded string
- `05d` - pad using 5 places
- `format(` - formats string and injects specified variables
- `number` - number to pad

## Example: 
```python
padded = "{:05d}".format(523)
print(padded)
```
```
00523

```
