# Example of struct of structs in Rust
// plain

Structs of structs in Rust are a way of nesting structs within each other. This allows for more complex data structures to be created.

## Example code

```rust
struct Outer {
    inner: Inner,
}

struct Inner {
    data: i32,
}

fn main() {
    let outer = Outer {
        inner: Inner { data: 5 },
    };

    println!("The inner data is: {}", outer.inner.data);
}
```

## Output example

```
The inner data is: 5
```

## Code explanation


- `struct Outer`: This is the outer struct which contains an inner struct.
- `struct Inner`: This is the inner struct which contains a data field.
- `let outer = Outer { inner: Inner { data: 5 } }`: This creates an instance of the outer struct, with an instance of the inner struct inside it.
- `println!("The inner data is: {}", outer.inner.data)`: This prints out the data field of the inner struct.

## Helpful links

- [Rust Structs](https://doc.rust-lang.org/book/ch05-01-defining-structs.html)
- [Rust Structs of Structs](https://doc.rust-lang.org/book/ch05-03-method-syntax.html#nested-structs)

group: rust-struct