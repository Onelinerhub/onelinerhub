# How do I access a tuple variable by index in Rust?
// plain

You can access a tuple variable by index in Rust using the `.` operator. For example:

```
let my_tuple = (1, 2, 3);
let first_element = my_tuple.0;
```

This will set `first_element` to `1`.

## Code explanation


- `let my_tuple = (1, 2, 3);`: This creates a tuple with three elements.
- `let first_element = my_tuple.0;`: This accesses the first element of the tuple and assigns it to the variable `first_element`.

## Helpful links

- [Rust Documentation - Tuples](https://doc.rust-lang.org/book/ch03-02-data-types.html#tuples)

group: rust-variables