# How to loop an array in Rust
// plain

Looping an array in Rust is done using a `for` loop. The syntax is as follows:

```
for element in array {
    // code to execute
}
```

The ## Code explanation


- `for`: the keyword used to start the loop
- `element`: the variable used to store the current element of the array
- `in`: the keyword used to separate the variable from the array
- `array`: the array to loop over
- `{`: the opening brace of the loop body
- `// code to execute`: the code to execute for each element of the array
- `}`: the closing brace of the loop body

Example:

```
let array = [1, 2, 3];

for element in array {
    println!("{}", element);
}
```

## Output example


```
1
2
3
```

## Helpful links

- [Rust Documentation - Loops](https://doc.rust-lang.org/book/ch03-05-control-flow.html#loops)

group: rust-loops