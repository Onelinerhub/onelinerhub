# Onelinerhub
Lib of micro code pieces, well explained and mostly single-line solutions @ [onelinerhub.com](https://onelinerhub.com/).

## Why we do it and where we go
We're building non-profit opensource code hub to address following issues:
- clear simple modern solutions for repeatable coding challeges
- moderated single-standard solutions instead of "here's a list of 25 answers with 125 comments"
- code parts explanations to fight dumb copy-paste, but educate instead
- no ads, no paid access, just community contributions and usefulness instead of profits 

## Help by contributing
- Join our organization here: https://github.com/Onelinerhub
- Clone [repo](https://github.com/Onelinerhub/onelinerhub) and create pull requests
- Create [issues](https://github.com/Onelinerhub/onelinerhub/issues) to request UI/code updates

Feel free to add/update any tech code piece you find useful.


## Principles
- 3 main principles for code pieces here are: simple, modern, minimal
- Micro solutions are ment to solve specific issue in **modern** versions of technologies (browsers, compilers, databases, etc.)
- Solution should be as short and simple as possible
- Solution should be explained by components (variables, functions, operations, etc.)
- Image illustrations are welcome

## Code file micro-format
- Each code file should be placed in it's main technology folder (e.g. "php", "bash", etc).
- File should have short but understandable naming in underscore format (e.g. "redirect_header.md")
- Extension is always ".md", so all the markdown works
- File must include title (```"# title"```) as the first line (technology title is automatically added in UI ```{title} #{technology}```)
- File must include actual code snippet in the [highlighted code](https://guides.github.com/features/mastering-markdown/) block
- File should also include code parts description, so it's well explained (example in [template](/template.md))
- File can also include group definition to link similar solution (e.g. different date formats or string comparison methods)
- You can upload PNG file with the same file name as the code file and it will automatically be rendered in UI
- Example can be specified using ```## Example``` header followed by 2 code blocks (input and output examples)

Use [this template](/template.md) for creating new code pieces.

## FAQ
> "What if I want to create new folder/technology in onelinerhub repo?"

You are welcome to do it with pull request as long as it is useful technology/solution for engineers

> "What if I want to edit some published code?"

You are welcome to do it with pull request as long as it will make the code better (simple, modern, minimal)

> "Can I post multi-line code (not a one-liner)?"

Yes, as long as the solution is targeted towards specific problem and is well explained

## API

We're happy to provide our code collection for integrations of all types. At this point, search API is available publicly with no need to register any keys.

Usage is as simple as calling `api.onelinerhub.com/search` endpoint with `quqery` parameter (GET or POST):

```bash
curl "https://api.onelinerhub.com/search?query=php+header+jon"
```

You'll get JSON array with the following objects:
```json
{
  "url": "...", // public URL of the code piece page
  "tech": "...", // technology of this code
  "subject": "...", // Full title for the code
  "lang": "...", // Code piece language
  "code": "..." // Code piece itself
}
```

Example:
```json
[
    {
        "url": "https:\/\/onelinerhub.com\/javascript\/fetch_post_uri",
        "tech": "javascript",
        "subject": "Ajax post x-www-form-urlencoded data",
        "lang": "javascript",
        "code": "fetch('\/backend.php', {\n  method: 'post',\n  headers: { 'Content-Type': 'application\/x-www-form-urlencoded;charset=UTF-8' },\n  body: 'var1=' + encodeURIComponent('Donald Trump :(') + '&amp;var2=123'\n}).then(function(r) {\n  return r.json();\n}).then(function(data) {\n  console.log(data);\n});"
    },
    {
        "url": "https:\/\/onelinerhub.com\/php\/json_content_type",
        "tech": "php",
        "subject": "Set content type to JSON",
        "lang": "php",
        "code": "header('Content-Type: application\/json');\necho json_encode([]);"
    }
]
```
