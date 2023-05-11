# How to replace strings using Rust regex?
// plain

Rust regex can be used to replace strings in a variety of ways. The `replace` method can be used to replace all occurrences of a pattern with a given string. For example:

```rust
let re = Regex::new(r"(\w+)").unwrap();
let before = "Hello World";
let after = re.replace_all(before, "Goodbye");
println!("{}", after);
```

## Output example

```
GoodbyeGoodbye
```

The code above uses the `Regex::new` method to create a new Regex object, which is then used to call the `replace_all` method. This method takes two arguments: the string to be replaced and the string to replace it with. In this case, all occurrences of the pattern `(\w+)` are replaced with the string `Goodbye`.

Alternatively, the `replace_all` method can also take a closure as its second argument. This closure can be used to perform more complex replacements, such as replacing each occurrence of a pattern with a different string. For example:

```rust
let re = Regex::new(r"(\w+)").unwrap();
let before = "Hello World";
let after = re.replace_all(before, |caps: &Captures| {
    let word = caps[1].to_string();
    match word.as_str() {
        "Hello" => "Goodbye".to_string(),
        "World" => "Universe".to_string(),
        _ => word,
    }
});
println!("{}", after);
```

## Output example

```
GoodbyeUniverse
```

In this example, the closure takes a `Captures` object as its argument, which contains the matched pattern. The closure then uses a `match` expression to check the matched pattern and return the appropriate replacement string.

## Helpful links

- [Rust Regex Documentation](https://doc.rust-lang.org/regex/regex/index.html)
- [Rust Regex Tutorial](https://rust-lang-nursery.github.io/rust-cookbook/text/regex.html)

group: rust-regex

onelinerhub: [How to replace strings using Rust regex?](https://onelinerhub.com/rust/how-to-replace-strings-using-rust-regex)