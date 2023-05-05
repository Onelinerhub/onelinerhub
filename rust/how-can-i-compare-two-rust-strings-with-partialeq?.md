# How can I compare two Rust strings with PartialEq?
// plain

You can compare two Rust strings with PartialEq by using the `==` operator. For example:

```
let string1 = "Hello";
let string2 = "World";

assert!(string1 != string2);
```

The output of this code will be `assertion failed: string1 != string2`.

## Code explanation


- `let string1 = "Hello";` - This declares a variable `string1` and assigns it the value `"Hello"`.
- `let string2 = "World";` - This declares a variable `string2` and assigns it the value `"World"`.
- `assert!(string1 != string2);` - This uses the `assert!` macro to compare the two strings and check if they are not equal.

## Helpful links

- [Rust Documentation - PartialEq](https://doc.rust-lang.org/std/cmp/trait.PartialEq.html)
- [Rust Documentation - assert! macro](https://doc.rust-lang.org/std/macro.assert.html)