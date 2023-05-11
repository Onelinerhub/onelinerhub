# How to use captures_iter with regex in Rust?
// plain

Using `captures_iter` with regex in Rust is a powerful way to extract data from strings. `captures_iter` returns an iterator of all the captures that match a given pattern.

## Example code

```rust
let re = Regex::new(r"(\d{4})-(\d{2})-(\d{2})").unwrap();
let text = "Today is 2020-04-30";

for cap in re.captures_iter(text) {
    println!("Year: {}, Month: {}, Day: {}", &cap[1], &cap[2], &cap[3]);
}
```

## Output example

```
Year: 2020, Month: 04, Day: 30
```

## Code explanation

- `Regex::new(r"(\d{4})-(\d{2})-(\d{2})")`: creates a new Regex object with the given pattern.
- `captures_iter`: returns an iterator of all the captures that match the given pattern.
- `&cap[1], &cap[2], &cap[3]`: accesses the captures from the iterator.

## Helpful links
- [Regex Documentation](https://doc.rust-lang.org/regex/regex/index.html)
- [captures_iter Documentation](https://doc.rust-lang.org/regex/regex/struct.Regex.html#method.captures_iter)

group: rust-regex

onelinerhub: [How to use captures_iter with regex in Rust?](https://onelinerhub.com/rust/how-to-use-captures_iter-with-regex-in-rust)