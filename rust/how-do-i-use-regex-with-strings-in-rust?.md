# How do I use regex with strings in Rust?
// plain

Regex (regular expressions) can be used to match patterns in strings in Rust. To use regex, you need to import the `regex` crate.

```rust
extern crate regex;

use regex::Regex;
```

You can then create a `Regex` object with the pattern you want to match.

```rust
let re = Regex::new(r"\d+").unwrap();
```

You can then use the `is_match` method to check if the pattern matches a string.

```rust
assert!(re.is_match("123"));
```

You can also use the `find` method to find the first match of the pattern in a string.

```rust
let text = "123 456";
let caps = re.find(text).unwrap();
assert_eq!(&text[caps.start()..caps.end()], "123");
```

For more information, see the [Regex documentation](https://docs.rs/regex/1.3.9/regex/).