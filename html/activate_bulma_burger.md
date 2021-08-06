# Activate burger in Bulma navbar

```html
onclick="document.querySelector('.navbar-menu').classList.toggle('is-active');document.querySelector('.navbar-burger').classList.toggle('is-active');"
```

- `onclick` - add the `onclick` attribute to the anchor `<a>` tag in the below [Bulma navbar burger](https://bulma.io/documentation/components/navbar/):

```html
<a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
  <span aria-hidden="true"></span>
  <span aria-hidden="true"></span>
  <span aria-hidden="true"></span>
</a>
```
