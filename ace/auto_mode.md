# Automatically pick a mode based on file extension

```html
<script src="https://pagecdn.io/lib/ace/1.4.12/ext-modelist.min.js"></script>

<script>
  var modes = ace.require('ace/ext/modelist');
  editor.session.setMode( modes.getModeForPath( 'file.js' ).mode );
</script>
```

- ext-modelist.min.js - includes mode list extension to automatically pick modes
- var modes - declares modeList object
- editor - ace editor object ([see how to load](/ace/embed_html))
- editor.session.setMode - set syntaxt mode for editor
- modes.getModeForPath - will automatically detect mode based on file path
- 'file.js' - example file path to get mode for (javascript file in our case)
