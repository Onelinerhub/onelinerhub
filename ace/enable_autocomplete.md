# Enable autocompletion in Ace editor.

```html
&lt;script src=&quot;https://pagecdn.io/lib/ace/1.4.12/ace.min.js&quot;&gt;&lt;/script&gt;
&lt;script src=&quot;https://pagecdn.io/lib/ace/1.4.12/ext-language_tools.min.js&quot;&gt;&lt;/script&gt;

&lt;textarea id=&quot;editor&quot;&gt;&lt;/textarea&gt;

&lt;script&gt;
  var editor = ace.edit('editor', { enableBasicAutocompletion: true, enableSnippets: true, enableLiveAutocompletion: true });
  editor.session.setMode('ace/mode/javascript');
&lt;/script&gt;
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
