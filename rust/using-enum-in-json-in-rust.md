# Using enum in json in Rust
// plain

Enums in Rust can be used in JSON by serializing them into strings. To do this, the `#[serde(rename = "string")]` attribute can be used to specify the string value of the enum. For example, the following code creates an enum with the variants `Foo` and `Bar` and serializes them into strings:
```rust
#[derive(Serialize, Deserialize)]
#[serde(rename = "string")]
enum MyEnum {
    Foo,
    Bar,
}
```
The output of this code would be a JSON object with the string values of the enum:
```json
{
    "string": "Foo"
}
```
The `#[serde(rename = "string")]` attribute can also be used to specify custom string values for each variant of the enum. For example, the following code creates an enum with the variants `Foo` and `Bar` and serializes them into strings with custom values:
```rust
#[derive(Serialize, Deserialize)]
#[serde(rename = "string")]
enum MyEnum {
    #[serde(rename = "foo")]
    Foo,
    #[serde(rename = "bar")]
    Bar,
}
```
The output of this code would be a JSON object with the custom string values of the enum:
```json
{
    "string": "foo"
}
```
Using enums in JSON in Rust can be a useful way to add type safety to your data. It can also help to make your code more readable and maintainable.

## Helpful links
- [Rust Documentation - Enums](https://doc.rust-lang.org/book/ch06-00-enums.html)
- [Serde Documentation - Enums](https://serde.rs/enum-representations.html)
- [Rust by Example - Enums](https://doc.rust-lang.org/rust-by-example/custom_types/enum.html)

group: rust-enums