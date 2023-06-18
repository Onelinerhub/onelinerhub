# How do I add a link using ReactJS?
// plain

To add a link using ReactJS, you can use the `<a>` element to wrap the link and the link text.

## Example code

```
<a href="https://www.example.com" target="_blank" rel="noopener noreferrer">Link Text</a>
```

This will render a link to the specified URL with the text given in the `Link Text` part. The `target` attribute is set to `_blank` so that the link will open in a new tab when clicked. The `rel` attribute is set to `noopener noreferrer` to ensure that no referrer information is sent when the link is clicked.

The code is composed of the following parts:

1. `<a>` - the anchor element that wraps the link
2. `href` - the attribute that contains the URL to link to
3. `target` - the attribute that specifies where the link should open
4. `rel` - the attribute that specifies that no referrer information should be sent
5. `Link Text` - the text that will be displayed as the link

## Helpful links
- [MDN - <a>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a)
- [MDN - target](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a#attr-target)
- [MDN - rel](https://developer.mozilla.org/en-US/docs/Web/HTML/Link_types#Noopener)

onelinerhub: [How do I add a link using ReactJS?](https://onelinerhub.com/reactjs/how-do-i-add-a-link-using-reactjs)