# Native input custom autocomplete using datalist

```html
<input list="planets">

<datalist id="planets">
  <option value="Earth">
  <option value="Mars">
</datalist>
```

- <input - standard text input
- list="planets" - specify id of datalist tag to use for autocompletion
- id="choises" - datalist tag for ```planets``` input
- option value="Earth" - first item to use for autocomplete (can have any number of `<option` tags)
