# How do I configure PostgreSQL to use Kerberos authentication?
// plain

1. Install the Kerberos client packages on the host running PostgreSQL:
```
$ sudo apt-get install krb5-user
```

2. Create a Kerberos principal for the PostgreSQL user:
```
$ kadmin.local
kadmin.local:  addprinc postgres/<hostname>
kadmin.local:  exit
```

3. Create a keytab file for the PostgreSQL user:
```
$ kadmin.local
kadmin.local:  ktadd -k /etc/postgresql.keytab postgres/<hostname>
kadmin.local:  exit
```

4. Configure the PostgreSQL server to use Kerberos authentication:
Edit the file `/etc/postgresql/9.6/main/pg_hba.conf` and add the following line:
```
host    all             all             0.0.0.0/0               gss include_realm=0
```

5. Restart the PostgreSQL server:
```
$ sudo service postgresql restart
```

6. Configure the Kerberos client on the PostgreSQL host:
Edit the file `/etc/krb5.conf` and add the following lines:
```
[libdefaults]
    default_realm = <YOUR_REALM>

[realms]
    <YOUR_REALM> = {
        kdc = <KDC_SERVER_IP_ADDRESS>
    }
```

7. Test the Kerberos authentication:
```
$ psql -U postgres -h localhost
Password for user postgres:
psql (9.6.11)
Type "help" for help.

postgres=#
```

## Helpful links
- [PostgreSQL Documentation on Kerberos Authentication](https://www.postgresql.org/docs/current/auth-kerberos.html)
- [Kerberos Documentation](https://web.mit.edu/kerberos/krb5-1.15/doc/admin/)

onelinerhub: [How do I configure PostgreSQL to use Kerberos authentication?](https://onelinerhub.com/postgresql/how-do-i-configure-postgresql-to-use-kerberos-authentication)