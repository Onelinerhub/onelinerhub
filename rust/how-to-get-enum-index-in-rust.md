# How to get enum index in Rust
// plain

You can get the index of an enum in Rust by using the .enum_variant() method. This method returns a tuple containing the variant's index and the variant itself. For example, if you have an enum called Color with variants Red, Blue, and Green, you can get the index of the Red variant by calling Color::Red.enum_variant(). The output of this method will be (0, Color::Red). The first element of the tuple is the index of the variant. You can also use the .variant_index() method to get the index of an enum variant. This method takes the variant as an argument and returns its index. For example, Color::Red.variant_index() will return 0.

group: rust-enums