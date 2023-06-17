# How do I add an elasticsearch logo to my website?
// plain

Adding an Elasticsearch logo to your website is a simple process.

1. First, you will need to find the logo you would like to use. You can find the official Elasticsearch logo [here](https://www.elastic.co/brand-guidelines).

2. Once you have the logo downloaded, you can add it to your website either by uploading the file to your website's server or by linking to the file.

3. To upload the file to your website's server, you will need to use an FTP client like [FileZilla](https://filezilla-project.org/) to transfer the file.

4. Once the file is uploaded to the server, you can add the logo to your website using HTML. For example:

```
<img src="elasticsearch-logo.png" alt="Elasticsearch Logo" width="200" height="200" />
```

This code will display the Elasticsearch logo on your website with a width and height of 200px.

5. Alternatively, you can link to the file directly. For example:

```
<img src="https://www.elastic.co/assets/bltada7771f270d08f6/elastic-logo.svg" alt="Elasticsearch Logo" width="200" height="200" />
```

This code will display the Elasticsearch logo on your website with a width and height of 200px.

6. You can also use CSS to style the logo. For example:

```
<style>
img.elasticsearch-logo {
  width: 200px;
  height: 200px;
  border-radius: 10px;
  box-shadow: 0px 0px 10px #ccc;
}
</style>

<img src="elasticsearch-logo.png" alt="Elasticsearch Logo" class="elasticsearch-logo" />
```

This code will display the Elasticsearch logo on your website with a width and height of 200px, a border radius of 10px, and a box shadow of 10px.

7. You can also use JavaScript to add interactivity to the logo. For example:

```
<script>
document.getElementById("elasticsearch-logo").addEventListener("click", function() {
  alert("You clicked the Elasticsearch logo!");
});
</script>

<img src="elasticsearch-logo.png" alt="Elasticsearch Logo" id="elasticsearch-logo" width="200" height="200" />
```

This code will display the Elasticsearch logo on your website with a width and height of 200px and will alert a message when the logo is clicked.

onelinerhub: [How do I add an elasticsearch logo to my website?](https://onelinerhub.com/elasticsearch/how-do-i-add-an-elasticsearch-logo-to-my-website)