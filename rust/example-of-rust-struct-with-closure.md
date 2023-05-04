# Example of Rust struct with closure
// plain

A Rust struct with closure is a struct that contains a closure as a field. A closure is a function that can capture variables from its environment and use them in its body.

## Example code

```rust
struct ClosureStruct {
    closure: Box<dyn Fn() -> i32>,
}

fn main() {
    let closure_struct = ClosureStruct {
        closure: Box::new(|| {
            println!("Hello from closure!");
            42
        }),
    };

    println!("{}", closure_struct.closure());
}
```

## Output example

```
Hello from closure!
42
```

## Code explanation

- `struct ClosureStruct`: This is the struct that contains the closure.
- `closure: Box<dyn Fn() -> i32>`: This is the field of the struct that contains the closure. The closure takes no arguments and returns an `i32`.
- `Box::new(|| { ... })`: This is the closure that is assigned to the `closure` field. It prints "Hello from closure!" and returns `42`.
- `closure_struct.closure()`: This is how the closure is called.

## Helpful links
- [Closures in Rust](https://doc.rust-lang.org/book/ch13-01-closures.html)
- [Box in Rust](https://doc.rust-lang.org/std/boxed/index.html)

group: rust-struct