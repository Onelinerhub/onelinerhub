# Click outside of an element

```javascript
document.addEventListener('click', (e) => {
  const click_outside_element = document.querySelector('#element');
  let target = e.target;
  do {
    if (target == click_outside_element) return;
  } while (target = target.parentNode);

  console.log('clicked outside');
});
```

- document.addEventListener('click' - adds click event listener to document
- document.querySelector('#element') - this is the element we have to catch the click outside of
- if (target == click_outside_element) return; - this cycle will stop handler execution if click is inside our element
- console.log('clicked outside'); - replace this with your code that should be executed if user clicked ourside of ```#element```
