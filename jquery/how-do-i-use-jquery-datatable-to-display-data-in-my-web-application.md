# How do I use jQuery datatable to display data in my web application?
// plain

Using jQuery DataTables to display data in a web application is relatively simple. First, include the jQuery and DataTables library in your web page:

```
<script src="https://code.jquery.com/jquery-3.3.1.js"></script>
<script src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js"></script>
```

Then, create an HTML table with the data you want to display. For example:

```
<table id="example">
  <thead>
    <tr>
      <th>Name</th>
      <th>Position</th>
      <th>Office</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Tiger Nixon</td>
      <td>System Architect</td>
      <td>Edinburgh</td>
    </tr>
    <tr>
      <td>Garrett Winters</td>
      <td>Accountant</td>
      <td>Tokyo</td>
    </tr>
  </tbody>
</table>
```

To enable DataTables, use the following JavaScript code:

```
$(document).ready(function() {
    $('#example').DataTable();
});
```

The table will now be styled and enhanced with features such as sorting, searching, and pagination.

Parts of the code:

- `<script src="https://code.jquery.com/jquery-3.3.1.js"></script>` - This line includes the jQuery library.
- `<script src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js"></script>` - This line includes the DataTables library.
- `$(document).ready(function() {` - This is the start of a jQuery function that will run when the document is ready.
- `$('#example').DataTable();` - This line calls the DataTable() method on the table with the id of "example".

## Helpful links
- [jQuery](https://jquery.com/)
- [DataTables](https://datatables.net/)

onelinerhub: [How do I use jQuery datatable to display data in my web application?](https://onelinerhub.com/jquery/how-do-i-use-jquery-datatable-to-display-data-in-my-web-application)