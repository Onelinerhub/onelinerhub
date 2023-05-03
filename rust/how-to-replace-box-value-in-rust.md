# How to replace box value in Rust
// plain

Replacing a box value in Rust is a simple process. To do this, you must first create a new box with the desired value, then assign the new box to the old box. This is demonstrated in the following example:

```rust
let mut old_box = Box::new(5);
let new_box = Box::new(10);
old_box = new_box;
```

The output of this code will be:
```
()
```

The code consists of three parts:
1. `let mut old_box = Box::new(5);` - This creates a new box with the value 5.
2. `let new_box = Box::new(10);` - This creates a new box with the value 10.
3. `old_box = new_box;` - This assigns the new box to the old box, replacing the old value with the new one.

## Helpful links
- [Rust Documentation - Box](https://doc.rust-lang.org/std/boxed/struct.Box.html)

group: rust-box