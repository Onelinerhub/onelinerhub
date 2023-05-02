# How to loop through enum in Rust
// plain

Looping through an enum in Rust is done using a match expression. The match expression allows you to match each variant of the enum and execute code for each variant. The following ## Code example shows how to loop through an enum and print out each variant:
```rust
enum MyEnum {
    Variant1,
    Variant2,
    Variant3,
}

fn main() {
    let my_enum = MyEnum::Variant1;

    match my_enum {
        MyEnum::Variant1 => println!("Variant1"),
        MyEnum::Variant2 => println!("Variant2"),
        MyEnum::Variant3 => println!("Variant3"),
    }
}
```

Output example:
```
Variant1
```

## Explanation
 The ## Code example uses a match expression to loop through the enum. The match expression takes the enum as an argument and then matches each variant of the enum. For each variant, a code block is executed. In this example, the code block prints out the variant name.

## Helpful links
- [Rust Documentation - Match Expressions](https://doc.rust-lang.org/book/ch06-02-match.html)
- [Rust Documentation - Enums](https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html)
- [Rust by Example - Match](https://doc.rust-lang.org/rust-by-example/flow_control/match.html)

group: rust-enums