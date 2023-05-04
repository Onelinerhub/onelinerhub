# Rust for loop range inclusive example
// plain

A `for` loop in Rust can be used to iterate over a range of values. The range can be inclusive or exclusive. An example of an inclusive range is shown below:

```
for i in 0..=5 {
    println!("{}", i);
}
```

This code will output the following:

```
0
1
2
3
4
5
```

The code consists of the following parts:

- `for`: This is the keyword used to start a loop.
- `i`: This is the variable used to store the current value of the loop.
- `0..=5`: This is the range of values that the loop will iterate over. The `..=` indicates that the range is inclusive.
- `println!("{}", i);`: This is the code that will be executed for each iteration of the loop. It prints the current value of `i` to the console.

## Helpful links

- [Rust Loops](https://doc.rust-lang.org/book/ch03-05-control-flow.html#loops)

group: rust-loops