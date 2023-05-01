# Error with custom struct in Rust
// plain

The most common error when working with custom structs in Rust is the "cannot move out of borrowed content" error. This error occurs when a struct is moved out of a borrowed reference, which is not allowed in Rust.

Below is an example of code that will produce this error:

```
struct MyStruct {
    value: i32,
}

fn main() {
    let my_struct = MyStruct { value: 5 };
    let borrowed_struct = &my_struct;
    let moved_struct = my_struct;

    println!("{}", borrowed_struct.value);
}
```

### Output

```
error[E0507]: cannot move out of borrowed content
 --> src/main.rs:9:25
  |
9 |     let moved_struct = my_struct;
  |                         ^^^^^^^^
  |                         |
  |                         cannot move out of borrowed content
  |                         help: consider borrowing here: `&my_struct`
```

Explanation:
- `struct MyStruct { value: i32, }`: This is a custom struct with a single field, `value`, of type `i32`.
- `let my_struct = MyStruct { value: 5 };`: This creates an instance of `MyStruct` with the value `5`.
- `let borrowed_struct = &my_struct;`: This creates a borrowed reference to `my_struct`.
- `let moved_struct = my_struct;`: This attempts to move `my_struct` into `moved_struct`, which is not allowed because `my_struct` is already borrowed.

## Helpful links:
- [Rust Reference - Borrowing](https://doc.rust-lang.org/reference/expressions/operator-expr.html#borrowing)
- [Rust Reference - Move Semantics](https://doc.rust-lang.org/reference/expressions/move-semantics.html)