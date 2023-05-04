# How to extend struct from another struct in Rust
// plain

Structs in Rust can be extended from another struct using the `#[derive(PartialEq)]` annotation. This allows the struct to inherit the fields and methods of the parent struct.

## Example

```rust
#[derive(PartialEq)]
struct Parent {
    field1: i32,
    field2: i32,
}

struct Child {
    field3: i32,
}

impl Child : PartialEq {
    fn new(field1: i32, field2: i32, field3: i32) -> Child {
        Child {
            field1: field1,
            field2: field2,
            field3: field3,
        }
    }
}

let parent = Parent { field1: 1, field2: 2 };
let child = Child::new(1, 2, 3);

assert_eq!(parent, child);
```
## Output example

```
assertion successful
```

## Code explanation

- `#[derive(PartialEq)]`: This annotation allows the struct to inherit the fields and methods of the parent struct.
- `impl Child : PartialEq`: This line implements the `PartialEq` trait for the `Child` struct.
- `let parent = Parent { field1: 1, field2: 2 };`: This line creates an instance of the `Parent` struct.
- `let child = Child::new(1, 2, 3);`: This line creates an instance of the `Child` struct.
- `assert_eq!(parent, child);`: This line compares the two structs and checks if they are equal.

## Helpful links
- [Rust Structs](https://doc.rust-lang.org/book/ch05-00-structs.html)
- [Rust Traits](https://doc.rust-lang.org/book/ch10-02-traits.html)

group: rust-struct