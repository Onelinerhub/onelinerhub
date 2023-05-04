# Rust negative for loop example
// plain

Negative for loops in Rust are used to iterate over a range of numbers in reverse order. The syntax for a negative for loop is similar to a regular for loop, but the range is specified with a `.rev()` method.

## Example code

```
for i in (0..10).rev() {
    println!("{}", i);
}
```

## Output example

```
9
8
7
6
5
4
3
2
1
0
```

## Code explanation

- `for i in (0..10).rev()`: This is the loop syntax, which specifies the range of numbers to iterate over. The `.rev()` method reverses the range, so the loop will start at 10 and end at 0.
- `println!("{}", i)`: This is the code that will be executed for each iteration of the loop. In this case, it prints the current value of `i` to the console.

## Helpful links
- [Rust Loops](https://doc.rust-lang.org/book/ch03-05-control-flow.html#loops)
- [Rust Iterators](https://doc.rust-lang.org/book/ch13-02-iterators.html)

group: rust-loops