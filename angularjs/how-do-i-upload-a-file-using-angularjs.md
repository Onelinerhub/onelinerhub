# How do I upload a file using AngularJS?
// plain

Uploading a file using AngularJS can be done using a combination of the ```$http``` and ```FormData``` services.

Below is an example of how to upload a file using AngularJS:

```
// Create a new FormData object
var fd = new FormData();

// Take the selected file from the input and append it to the FormData object
fd.append("file", fileInputElement.files[0]);

// Make an AJAX (http request) call to the server
$http.post("/upload", fd, {
    withCredentials: true,
    headers: {'Content-Type': undefined },
    transformRequest: angular.identity
})
.success(function(data) {
    // Handle success
})
.error(function(data) {
    // Handle error
});
```

This code will take the file from the ```fileInputElement``` and send it to the server using an AJAX call. The ```FormData``` object is used to store the file and the ```$http``` service is used to make the request. The ```withCredentials``` and ```transformRequest``` options are used to ensure that the file is sent correctly.

## Code explanation


- ```var fd = new FormData();```: This line creates a new ```FormData``` object which will be used to store the file.

- ```fd.append("file", fileInputElement.files[0]);```: This line takes the file from the ```fileInputElement``` and appends it to the ```FormData``` object.

- ```$http.post("/upload", fd, {...})```: This line makes an AJAX call to the server, sending the ```FormData``` object.

- ```withCredentials: true```: This option is used to ensure that the file is sent correctly.

- ```headers: {'Content-Type': undefined }```: This option is used to ensure that the file is sent correctly.

- ```transformRequest: angular.identity```: This option is used to ensure that the file is sent correctly.

## Helpful links

- [FormData on MDN](https://developer.mozilla.org/en-US/docs/Web/API/FormData)
- [$http on AngularJS Documentation](https://docs.angularjs.org/api/ng/service/$http)

onelinerhub: [How do I upload a file using AngularJS?](https://onelinerhub.com/angularjs/how-do-i-upload-a-file-using-angularjs)