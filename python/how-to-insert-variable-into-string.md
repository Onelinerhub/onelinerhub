# How to insert variable into string

```python
var = '10'
str = f'number is {var}'
```

- `var = '10'` - declare test variable to insert into string
- `str` - resulting string with inserted variable
- `f'` - tells python that we're going to insert some variables in this string
- `{var}` - name of the variable to insert (between `{` and `}`)

## Example: 
```python
var = '10'
str = f'number is {var}'
print(str)
```
```
number is 10

```
