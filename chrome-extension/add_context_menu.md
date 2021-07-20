# How to add custom menu item to context menu

Should be executed in [background script](https://developer.chrome.com/docs/extensions/mv3/background_pages/),
which is [specified in manifest.json](/chrome-extension/background_script).
Also, [contextMenus](/chrome-extension/context_menu) permissions should be set.

```javascript
chrome.contextMenus.create({title: 'My menu', id: 'my_menu'});

chrome.contextMenus.onClicked.addListener(function (info, tab) {
  if (info.menuItemId = 'my_menu') {
    console.log(info);
  }
})
```

- chrome.contextMenus.create - adds new menu item to context menu
- 'My menu' - title for new menu item
- 'my_menu' - id of new menu item to reffer to it later
- onClicked.addListener - add listener for context menu click event
- info.menuItemId = 'my_menu' - make sure our menu item is clicked
- console.log(info) - do something when our menu item is clicked
