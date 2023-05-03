# How to borrow as static in Rust
// plain

Static borrowing in Rust is a way to borrow a value without taking ownership of it. This allows the value to be used without having to move it.

```
let mut x = 5;

{
    let y = &x; // y is a reference to x
    println!("{}", y);
}

x = 6;
```

## Output example

```
5
```

The code above shows an example of static borrowing. The variable `x` is declared as mutable and assigned the value `5`. A reference to `x` is then created and assigned to `y`. The reference `y` is then used to print the value of `x`. Finally, the value of `x` is changed to `6`.

The parts of the code are:

- `let mut x = 5;`: This declares a mutable variable `x` and assigns it the value `5`.
- `let y = &x;`: This creates a reference to `x` and assigns it to `y`.
- `println!("{}", y);`: This prints the value of `x` using the reference `y`.
- `x = 6;`: This changes the value of `x` to `6`.

## Helpful links

- [Rust Reference](https://doc.rust-lang.org/reference/index.html)
- [Rust Book](https://doc.rust-lang.org/book/index.html)

group: rust-borrow