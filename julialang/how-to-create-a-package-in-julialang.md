# How to create a package in JuliaLang?
// plain

Creating a package in JuliaLang is a simple process. First, create a directory for the package and add a `Project.toml` and `Manifest.toml` file. Then, add the source code for the package in the directory. Finally, use the `Pkg.develop` command to develop the package.

## Example code

```julia
# Create a directory for the package
mkdir MyPackage

# Create Project.toml and Manifest.toml files
touch MyPackage/Project.toml
touch MyPackage/Manifest.toml

# Add source code for the package
# ...

# Develop the package
Pkg.develop("MyPackage")
```

## Output example

```
  Updating registry at `~/.julia/registries/General`
  Updating git-repo `https://github.com/JuliaRegistries/General.git`
 Resolving package versions...
  Updating `~/MyPackage/Project.toml`
  [no changes]
  Updating `~/MyPackage/Manifest.toml`
  [no changes]
```

## Code explanation


1. `mkdir MyPackage`: creates a directory for the package.
2. `touch MyPackage/Project.toml`: creates a `Project.toml` file in the package directory.
3. `touch MyPackage/Manifest.toml`: creates a `Manifest.toml` file in the package directory.
4. `# Add source code for the package`: adds source code for the package in the directory.
5. `Pkg.develop("MyPackage")`: uses the `Pkg.develop` command to develop the package.

## Helpful links

- [Julia Documentation - Creating Packages](https://docs.julialang.org/en/v1/manual/packages/#Creating-Packages-1)
- [Julia Documentation - Package Development](https://docs.julialang.org/en/v1/stdlib/Pkg/#Package-Development-1)

onelinerhub: [How to create a package in JuliaLang?](https://onelinerhub.com/julialang/how-to-create-a-package-in-julialang)