# Burger menu example

```html
<nav class="navbar" role="navigation" aria-label="main navigation">
  <div class="navbar-brand">
    <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="burger" onclick="document.querySelector('.navbar-menu').classList.toggle('is-active');document.querySelector('.navbar-burger').classList.toggle('is-active');">
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
    </a>
  </div>

  <div id="burger" class="navbar-menu">
    <div class="navbar-start">
      <a class="navbar-item">Menu item</a>
    </div>

    <div class="navbar-end"></div>
  </div>
</nav>
```

- class="navbar-burger" - burger icon button
- data-target="burger" - specify id of an element to attach burger button to
- div id="burger" - menu container to open/close on burger click
- onclick - js that activates the burger and will run on burger click
