# oneliner:hub
A lib of micro code pieces, well explained and mostly single-line solutions @ [onelinerhub.com](https://onelinerhub.com/).

**460** code pieaces collected already and counting!

![oneliner:hub example](/example.png)

## Help by contributing
Just create a pull request with new/updated codes.
Feel free to add/update any tech code piece you find useful.

### Help needed now:
- Python code pieces
- Lua code pieces
- Git code pieces
- Any new technologies not listed [here](https://onelinerhub.com/) are also welcome

## Principles
- Micro solutions are ment to solve specific issue in **modern** versions of technologies (browsers, compilers, databases, etc.)
- Solution should be as short and simple as possible
- Solution should be explained by components (variables, functions, operations, etc.)
- Image illustrations are welcome

## Code file micro-format
- Each code file should be placed in it's main technology folder (e.g. "php", "bash", etc).
- File should have short but understandable naming in underscore format (e.g. "redirect_header.md")
- Extension is always ".md", so all the markdown works
- File must include title (```"# title"```) as the first line (technology title is automatically added in UI ```{title} with {technology}``` unless you specify it manually, like ```{title} in {technology}```)
- File must include actual code snippet in the [highlighted code](https://guides.github.com/features/mastering-markdown/) block
- File should also include code parts description, so it's well explained (example in [template](/template.md))
- File can also include group definition to link similar solution (e.g. different date formats or string comparison methods)
- You can upload PNG file with the same file name as the code file and it will automatically be rendered in UI
- Example can be specified using ```## Example``` header followed by 2 code blocks (input and output examples)

Use [this template](/template.md) for creating new code pieces.
