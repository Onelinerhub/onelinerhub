# Enable autocompletion in Ace editor.

```html
<script src="https://pagecdn.io/lib/ace/1.4.12/ace.min.js"></script>
<script src="https://pagecdn.io/lib/ace/1.4.12/ext-language_tools.min.js"></script>

<textarea id="editor"></textarea>

<script>
  var editor = ace.edit('editor', { enableBasicAutocompletion: true, enableSnippets: true, enableLiveAutocompletion: true });
  editor.session.setMode('ace/mode/javascript');
</script>
```

- `ace.min.js` - load Ace lib from CDN
- `ext-language_tools.min.js` - load language tools for autocompletion
- `var editor` - ace editor object
- `<textarea id="editor"` - HTML element to replace with Ace editor
- `'editor'` - ID of HTML element to replace with code editor
- `enableBasicAutocompletion` - enables autocompletion
- `enableSnippets` - enables custom snippets
- `enableLiveAutocompletion` - enables live code suggestions


link_youtube: https://youtu.be/lVjot_rFtxI
