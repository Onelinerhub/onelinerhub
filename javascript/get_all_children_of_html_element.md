# Get all children and grandchildren of an html element recursively

```javascript
const getAllChildren = (htmlElement) => {
  if (htmlElement.children.length === 0) return [htmlElement];

  let allChildElements = [];

  for (let i = 0; i < htmlElement.children.length; i++) {
    let children = getAllChildren(htmlElement.children[i]);
    if (children) allChildElements.push(...children);
  }
  allChildElements.push(htmlElement);

  return allChildElements;
};
```

- htmlElement.children.length === 0 - check if we are at the deepest element. If there is no child, we are.
- allChildElements = [] - all child elements for current htmlElement.
- allChildElements.push(...children) - push incoming children from deeper level of recursive call.
- allChildElements.push(htmlElement) - push the element itself at the end of iteration.
