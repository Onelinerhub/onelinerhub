# Quickly integrate Ace editor into HTML page.

```html
<textarea id="editor"></textarea>

<script src="https://pagecdn.io/lib/ace/1.4.12/ace.min.js"></script>

<script>
  var editor = ace.edit('editor', {});
  editor.session.setMode('ace/mode/javascript');
</script>
```

- `id="editor"` - this will be replaced by Ace code editor
- `pagecdn.io/lib/ace` - load Ace library from public CDN
- `ace.edit` - init editor
- `'editor'` - id of the element to replace with Ace code editor (textarea in our case)
- `editor.session.setMode` - set syntax highlighter type
- `ace/mode/javascript` - use JS syntax


link_youtube: https://youtu.be/XTOCWQdrPv4
