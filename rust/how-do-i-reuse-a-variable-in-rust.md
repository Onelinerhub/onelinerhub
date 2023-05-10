# How do I reuse a variable in Rust?
// plain

Reusing a variable in Rust is easy and straightforward. You can simply assign a new value to the same variable. For example:

```
let mut x = 5;
x = 10;
```

This will assign the value 10 to the variable x.

You can also use the same variable in a loop, for example:

```
let mut x = 0;
for i in 0..10 {
    x += i;
}
println!("x = {}", x);
```

This will print out the value 45.

The parts of the code are:

- `let mut x = 0;`: This declares a mutable variable x and assigns it the value 0.
- `for i in 0..10 {`: This starts a loop that will iterate 10 times.
- `x += i;`: This adds the value of i to x each time the loop iterates.
- `println!("x = {}", x);`: This prints out the value of x.

## Helpful links

- [Rust Documentation - Variables](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html)
- [Rust Documentation - Loops](https://doc.rust-lang.org/book/ch03-05-control-flow.html#loops)

group: rust-variables