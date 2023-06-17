# How do I assign roles in Elasticsearch?
// plain

You can assign roles in Elasticsearch using the [Role Mapping API](https://www.elastic.co/guide/en/elasticsearch/reference/current/security-api-role-mapping.html). The Role Mapping API allows you to define a set of roles, and then assign users or groups to those roles.

For example, the following code block creates a new role called `admin` and assigns the `user1` user to that role:

```
PUT /_xpack/security/role_mapping/admin
{
  "roles": ["admin"],
  "enabled": true,
  "rules": {
    "field": {
      "username": "user1"
    }
  }
}
```

The output of this code block will be:

```
{
  "created": true
}
```

The code block consists of the following parts:

* `PUT`: the HTTP method used to create the role mapping
* `/_xpack/security/role_mapping/admin`: the endpoint used to create the role mapping
* `roles`: the list of roles to assign to the user
* `enabled`: a boolean indicating if the role mapping is enabled
* `rules`: a set of rules used to determine which users to assign the role to
  * `field`: the type of rule used, in this case a field rule
  * `username`: the field used to match users
  * `user1`: the value used to match users

This example creates a new role mapping with one user assigned to it. You can also assign multiple users to the same role by adding multiple rules, or assign multiple roles to the same user.

onelinerhub: [How do I assign roles in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-assign-roles-in-elasticsearch)