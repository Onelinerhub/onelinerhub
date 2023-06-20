# How can I use cli sed to deploy an ARM template?
// plain

Using the command line interface `sed` to deploy an ARM template is relatively straightforward.

First, create the ARM template. This can be done in either a text editor or in Azure Portal. Once the template is ready, save it to a file.

Next, use `sed` to modify the ARM template file. For example, the following command would replace the `<location>` placeholder with `eastus`:
```
sed -i 's/<location>/eastus/g' armtemplate.json
```

The output of this command would be:
```
```

Finally, deploy the ARM template file using the `az` command line tool. This can be done using the `az group deployment create` command, as shown below:
```
az group deployment create --name MyDeployment --resource-group MyResourceGroup --template-file armtemplate.json
```

The output of this command would be the deployment details, such as the provisioning state, the template link, and the timestamp.

## Helpful links
- [Azure CLI Documentation](https://docs.microsoft.com/en-us/cli/azure/?view=azure-cli-latest)
- [sed Documentation](https://www.gnu.org/software/sed/manual/sed.html)

onelinerhub: [How can I use cli sed to deploy an ARM template?](https://onelinerhub.com/cli-sed/how-can-i-use-cli-sed-to-deploy-an-arm-template)