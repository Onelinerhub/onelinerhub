# How to get inner enum value in Rust
// plain

To get the inner enum value in Rust, you can use the match expression. The match expression allows you to compare a value against a list of patterns and execute code based on which pattern matches. For example, if you have an enum with two variants, you can use the match expression to get the inner enum value:
```
rust
enum MyEnum {
    Variant1(String),
    Variant2(i32),
}

let my_enum = MyEnum::Variant1("Hello".to_string());

match my_enum {
    MyEnum::Variant1(s) => println!("Variant1: {}", s),
    MyEnum::Variant2(i) => println!("Variant2: {}", i),
}
```

Output example:
```
Variant1: Hello
```

## Explanation
 The match expression is used to compare the value of `my_enum` against the two variants of the enum. If the value is `MyEnum::Variant1`, the code inside the first block is executed, printing the string `Hello`. If the value is `MyEnum::Variant2`, the code inside the second block is executed, printing the integer value.

## Helpful links
- [Rust match expression](https://doc.rust-lang.org/book/ch06-02-match.html)
- [Rust enums](https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html)
- [Rust match arms](https://doc.rust-lang.org/book/ch06-02-match.html#match-arms)

group: rust-enums