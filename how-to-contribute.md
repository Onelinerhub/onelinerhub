# How to contribute to Onelinerhub

Have and idea of a useful code but don't know how to write it? Create an [issue](https://github.com/Onelinerhub/onelinerhub/issues/new) here so community might help. Search through current [open issues](https://github.com/Onelinerhub/onelinerhub/issues) for requested solutions you can help with.

## Requirements for contributors
Basically everyone (having a github account) can contribute any amount of code solutions for any technology.
You need to follow our simple guidelines:
- code solution should be useful to other developers,
- code should solve specific issue in a simplest possible way,
- no need to write "ideal", "universal" or "all-possible-issues-solved" solutions, we're here to connect specific issue to it's simplest and clear solution,
- explain your solution so it's clear for not-so-experienced or not-familiar-with engineers.

## Code file (\*.md) format
- Each code file should be placed in it's main technology folder (e.g. "php", "bash", etc).
- File should have short but understandable naming in underscore format (e.g. "redirect_header.md").
- Extension is always ".md", so all the markdown works.
- File must include title (```"# title"```) as the first line.
- File must include actual code snippet in the [highlighted code](https://guides.github.com/features/mastering-markdown/) block.
- File should also include code explanation block, so it's well explained (a list with "{part} - {description}" pairs like [here](/template_simple.md)), markdown will work here also.
- You can upload PNG file with the same file name as the code file and it will automatically be added to the code page in UI (like [here](https://onelinerhub.com/ffmpeg/downmix_audio)).

### Example
Given [this code example](/javascript/array_unique.md), this is how it's `md` file looks like:
![Code example](/code_example.png)

This will render into:

![UI example](/ui_example.png)

## Code templates
- [Simple template](/template_simple.md)
- [Advanced template](/template.md)
