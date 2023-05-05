# How do I compare a string and a str in Rust?
// plain

Comparing strings in Rust is done using the `==` operator. This operator will compare two strings and return `true` if they are equal, and `false` if they are not.

## Example

```
let str1 = "Hello";
let str2 = "World";

println!("{}", str1 == str2);
```
## Output example

```
false
```

The `==` operator compares two strings by comparing each character in the strings. If all characters in the strings are the same, then the strings are equal and the `==` operator will return `true`.

In addition to the `==` operator, Rust also provides the `str::eq` method which can be used to compare two strings. This method takes two `&str` references as arguments and returns `true` if the strings are equal, and `false` if they are not.

## Example

```
let str1 = "Hello";
let str2 = "World";

println!("{}", str1.eq(&str2));
```
## Output example

```
false
```

## Helpful links
- [Rust Documentation - Strings](https://doc.rust-lang.org/stable/std/string/index.html)
- [Rust Documentation - Primitive Types](https://doc.rust-lang.org/stable/book/ch03-02-data-types.html#primitive-types)