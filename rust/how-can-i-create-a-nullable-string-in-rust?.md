# How can I create a nullable string in Rust?
// plain

A nullable string in Rust can be created using the `Option<String>` type. This type is an enum that can either be `Some(String)` or `None`.

## Example code

```rust
let my_string: Option<String> = Some("Hello World".to_string());
```

## Output example

```
Some("Hello World")
```

## Code explanation

- `Option<String>`: This is the type used to create a nullable string in Rust. It is an enum that can either be `Some(String)` or `None`.
- `Some("Hello World".to_string())`: This is the value assigned to the `my_string` variable. It is a `String` wrapped in the `Some` variant of the `Option<String>` enum.

## Helpful links
- [Rust Documentation - Option](https://doc.rust-lang.org/std/option/enum.Option.html)