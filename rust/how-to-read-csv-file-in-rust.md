# How to read CSV file in Rust
// plain

Reading a CSV file in Rust is relatively straightforward. The easiest way to do this is to use the csv crate, which provides a Reader type that can be used to iterate over the records in a CSV file. To use the crate, you first need to add it to your Cargo.toml file. Then, you can create a Reader instance and use its methods to read the CSV file. For example, the following code snippet reads a CSV file and prints out each record:
```rust
use csv::Reader;

fn main() {
    let mut rdr = Reader::from_path("my_file.csv").unwrap();
    for result in rdr.records() {
        let record = result.unwrap();
        println!("{:?}", record);
    }
}
```
The output of this code would be something like:
```
[1, "John", "Doe"]
[2, "Jane", "Smith"]
```
The Reader type provides several methods for reading CSV files, such as `records()` which returns an iterator over the records in the file, and `deserialize()` which can be used to deserialize each record into a Rust struct. For more information, please refer to the [csv crate documentation](https://docs.rs/csv/1.1.3/csv/).

group: rust-files