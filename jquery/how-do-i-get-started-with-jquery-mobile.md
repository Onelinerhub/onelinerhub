# How do I get started with jQuery Mobile?
// plain

1. First, you need to include the jQuery Mobile library in your HTML page. You can do this by adding the following line of code in the <head> tag of your HTML page:
```
<script src="https://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.js"></script>
```
2. Next, create a basic HTML page structure with a <div> tag and a data-role="page" attribute. This will tell jQuery Mobile that this is a page that it needs to enhance:
```
<div data-role="page">
    <div data-role="header">
        <h1>My Page</h1>
    </div>
    <div data-role="main" class="ui-content">
        <p>This is my page content.</p>
    </div>
    <div data-role="footer">
        <h1>Footer</h1>
    </div>
</div>
```
3. Now, you can add additional jQuery Mobile components to your page. For example, to add a listview, you can use the following code:
```
<ul data-role="listview">
    <li><a href="#">Item 1</a></li>
    <li><a href="#">Item 2</a></li>
    <li><a href="#">Item 3</a></li>
</ul>
```
4. Finally, you can add custom styling to your page using CSS. For example, you can add a background color to your page like this:
```
<style>
    .ui-page {
        background-color: #ccc;
    }
</style>
```

This is just a basic overview of how to get started with jQuery Mobile. For more detailed information, please refer to the [jQuery Mobile documentation](https://api.jquerymobile.com/).

onelinerhub: [How do I get started with jQuery Mobile?](https://onelinerhub.com/jquery/how-do-i-get-started-with-jquery-mobile)