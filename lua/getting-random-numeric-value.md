# Getting random numeric value

```lua
math.randomseed(os.time())
rand = math.random(1, 10)
```

- `math.randomseed(os.time())` - init unique random generator (use local time for seed)
- `math.random` - return random number within given range
- `1, 10` - min and max value of the number to generate
- `rand` - will contain generated random number

## Example: 
```lua
math.randomseed(os.time())
print( math.random(1, 10) )
print( math.random(1, 10) )
print( math.random(1, 10) )
```
```
7
10
3

```

