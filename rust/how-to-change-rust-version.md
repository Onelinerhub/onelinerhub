# How to change Rust version
// plain

Changing the version of Rust you are using is a relatively simple process.

The following ## Code example shows how to use the `rustup` command to change the version of Rust you are using:

```
rustup default <version>
```

For example, to change to version 1.45.0, you would use the command:

```
rustup default 1.45.0
```

The output of this command should look something like this:

```
info: syncing channel updates for '1.45.0-x86_64-unknown-linux-gnu'
info: latest update on 2020-07-02, rust version 1.45.0 (5c1f21c3b 2020-06-15)
info: downloading component 'rustc'
info: downloading component 'rust-std'
info: downloading component 'cargo'
info: downloading component 'rust-docs'
info: installing component 'rustc'
info: installing component 'rust-std'
info: installing component 'cargo'
info: installing component 'rust-docs'
info: default toolchain set to '1.45.0-x86_64-unknown-linux-gnu'
```

Here is a ## Explanation of the code parts:

1. `rustup`: This is the command used to manage Rust versions.
2. `default`: This is the subcommand used to set the default version of Rust.
3. `<version>`: This is the version of Rust you want to set as the default.

## Helpful links:

1. [Rustup Documentation](https://rustup.rs/): This is the official documentation for the `rustup` command.
2. [Rust Version History](https://forge.rust-lang.org/release/): This page contains a list of all the versions of Rust released.