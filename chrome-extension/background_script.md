# Load background script

```json
{
  "name": "My",
  // ...
  |{|"background": {
  	"service_worker": "bg.js"
	},|}|,
  // ...
}
```

- "background" - specify script to load in background
- "bg.js" - name of the background script to load (should be placed in the same folder as `manifest.json`)

group: background_scripts
