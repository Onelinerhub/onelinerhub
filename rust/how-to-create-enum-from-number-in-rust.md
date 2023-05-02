# How to create enum from number in Rust
// plain

Enums in Rust are used to create a type with a fixed set of values. To create an enum from a number, you can use the From trait. This trait allows you to convert a number into an enum variant. The following ## Code example shows how to create an enum from a number:
```
enum MyEnum {
    Variant1,
    Variant2,
    Variant3,
}

let number = 2;
let enum_variant = MyEnum::from(number);
```

The output of this ## Code example is:
```
enum_variant = Variant2
```

The ## Code example uses the From trait to convert the number 2 into the enum variant Variant2. The From trait is implemented for all types that implement the Copy trait. This allows you to convert any number into an enum variant.

Detailed explanation of code parts with inline code enclosed with `: The ## Code example starts by defining an enum with three variants. Then, a number is declared and assigned the value 2. Finally, the From trait is used to convert the number into an enum variant. The From trait is implemented for all types that implement the Copy trait, which allows you to convert any number into an enum variant.

## Helpful links
- [Rust Enums](https://doc.rust-lang.org/book/ch06-00-enums.html)
- [Rust From Trait](https://doc.rust-lang.org/std/convert/trait.From.html)
- [Rust Copy Trait](https://doc.rust-lang.org/std/marker/trait.Copy.html)

group: rust-enums