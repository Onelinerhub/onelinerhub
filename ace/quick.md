# Quickly integrate Ace editor into HTML page.

```html
<textarea id="editor"></textarea>

<script src="https://cdnjs.cloudflare.com/ajax/libs/ace/1.4.5/ace.js"
        integrity="sha256-5Xkhn3k/1rbXB+Q/DX/2RuAtaB4dRRyQvMs83prFjpM="
        crossorigin="anonymous"></script>

<script>
  var editor = ace.edit('editor', {});
  editor.session.setMode('ace/mode/javascript');
</script>
```

- <textarea id="editor" - this will be replaced by Ace code editor
- cdnjs.cloudflare.com - load Ace library from public CDN
- ace.edit - init editor
- 'editor' - id of the element to replace with Ace code editor (textarea in our case)
- editor.session.setMode - set syntax highlighter type
- ace/mode/javascript - use JS syntax
