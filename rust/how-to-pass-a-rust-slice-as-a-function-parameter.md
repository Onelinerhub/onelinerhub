# How to pass a Rust slice as a function parameter?
// plain

Passing a Rust slice as a function parameter is done by using the `&[T]` syntax. This syntax indicates that the function takes a slice of type `T`. For example:

```
fn print_slice(slice: &[i32]) {
    for item in slice {
        println!("{}", item);
    }
}

let arr = [1, 2, 3];
print_slice(&arr);
```

## Output example

```
1
2
3
```

- `fn print_slice(slice: &[i32])`: This declares a function called `print_slice` that takes a slice of type `i32` as a parameter.
- `let arr = [1, 2, 3]`: This creates an array of type `i32` with the values `1`, `2`, and `3`.
- `print_slice(&arr)`: This passes the array `arr` as a parameter to the function `print_slice`.

## Helpful links
- [Rust Documentation - Slices](https://doc.rust-lang.org/book/ch04-03-slices.html)
- [Rust Documentation - Functions](https://doc.rust-lang.org/book/ch03-03-how-functions-work.html)

group: rust-slice