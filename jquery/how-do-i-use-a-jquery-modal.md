# How do I use a jQuery modal?
// plain

Using a jQuery modal is a great way to display content in a popup window. Here is an example of how to create a simple modal:

```
<div id="myModal" class="modal">
  <div class="modal-content">
    <span class="close">&times;</span>
    <p>Some text in the Modal..</p>
  </div>
</div>
```

The code above creates a modal with a close button. To make the modal appear, the following JavaScript code can be used:

```
// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
```

The code above will open and close the modal when the user clicks a button and when clicking outside of the modal.

Parts of the code explained:
* `var modal = document.getElementById("myModal");` - This line of code gets the modal element from the HTML.
* `btn.onclick = function() {modal.style.display = "block";}` - This line of code assigns an event listener to the button that will open the modal when clicked.
* `span.onclick = function() {modal.style.display = "none";}` - This line of code assigns an event listener to the close button that will close the modal when clicked.
* `window.onclick = function(event) {if (event.target == modal) {modal.style.display = "none";}}` - This line of code assigns an event listener to the window that will close the modal when clicked outside of the modal.

## Helpful links
* [jQuery Modal Tutorial](https://www.w3schools.com/howto/howto_css_modals.asp)
* [MDN: Using JavaScript Modals](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Show_and_hide#Using_JavaScript_modals)

onelinerhub: [How do I use a jQuery modal?](https://onelinerhub.com/jquery/how-do-i-use-a-jquery-modal)