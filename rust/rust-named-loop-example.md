# Rust named loop example
// plain

A `named loop` in Rust is a loop that can be labeled with a name. This allows the loop to be `break`ed or `continue`ed from anywhere in the code.

## Example code

```rust
'outer: loop {
    println!("Entered the outer loop");

    'inner: loop {
        println!("Entered the inner loop");

        // This would break only the inner loop
        break 'inner;

        println!("This point will never be reached");
    }

    println!("This point is reached");

    // This breaks the outer loop
    break 'outer;
}

println!("Exited the outer loop");
```

## Output example

```
Entered the outer loop
Entered the inner loop
This point is reached
Exited the outer loop
```

## Code explanation


1. `'outer: loop` - This is the outer loop, labeled with the name `outer`.
2. `break 'inner` - This statement breaks the inner loop, labeled with the name `inner`.
3. `break 'outer` - This statement breaks the outer loop, labeled with the name `outer`.

## Helpful links

- [Rust Documentation - Loops](https://doc.rust-lang.org/book/ch03-05-control-flow.html#loops)
- [Rust Documentation - Labeled Blocks](https://doc.rust-lang.org/book/ch03-05-control-flow.html#labeled-blocks)

group: rust-loops