# How do I split strings in Rust?
// plain

Strings in Rust can be split using the `split()` method. This method takes a string and a delimiter as parameters and returns an iterator of strings.

## Example code

```
let my_string = "Hello, World!";
let split_string = my_string.split(",");
```

## Output example

```
["Hello", " World!"]
```

## Code explanation

- `let my_string = "Hello, World!";`: This line declares a string variable called `my_string` and assigns it the value `"Hello, World!"`.
- `let split_string = my_string.split(",");`: This line calls the `split()` method on the `my_string` variable, passing in the delimiter `","` as a parameter. This returns an iterator of strings.

## Helpful links
- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)
- [Rust Documentation - Str Split](https://doc.rust-lang.org/std/primitive.str.html#method.split)