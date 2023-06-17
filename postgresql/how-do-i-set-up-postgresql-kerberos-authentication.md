# How do I set up PostgreSQL Kerberos authentication?
// plain

1. Install Kerberos client libraries and configure the krb5.conf file to point to the Kerberos server.
2. Create a service principal for PostgreSQL on the Kerberos server.
```
$ kadmin.local
kadmin.local: addprinc postgres/<hostname>@<REALM>
```
3. Generate a keytab for the service principal.
```
$ kadmin.local
kadmin.local: xst -k postgres.keytab postgres/<hostname>@<REALM>
```
4. Configure PostgreSQL to use Kerberos authentication. Edit the pg_hba.conf file to include the following line:
```
host    all             all             <hostname>/32            gss include_realm=1
```
5. Configure the PostgreSQL server to use the keytab file. Edit the postgresql.conf file to include the following lines:
```
krb_server_keyfile = '/path/to/postgres.keytab'
krb_caseins_users = off
```
6. Restart the PostgreSQL server.
```
$ sudo systemctl restart postgresql
```
7. Test Kerberos authentication by connecting to the PostgreSQL server using the Kerberos user.
```
$ psql -h <hostname> -U <username>
```

## Explanation

1. Install Kerberos client libraries and configure the krb5.conf file to point to the Kerberos server.
   - This step installs the necessary Kerberos libraries and configures the krb5.conf file to point to the Kerberos server.
2. Create a service principal for PostgreSQL on the Kerberos server.
   - This step creates a service principal for PostgreSQL on the Kerberos server.
3. Generate a keytab for the service principal.
   - This step generates a keytab for the service principal, which is necessary for authentication.
4. Configure PostgreSQL to use Kerberos authentication.
   - This step configures PostgreSQL to use Kerberos authentication by adding a line to the pg_hba.conf file.
5. Configure the PostgreSQL server to use the keytab file.
   - This step configures the PostgreSQL server to use the keytab file by adding two lines to the postgresql.conf file.
6. Restart the PostgreSQL server.
   - This step restarts the PostgreSQL server to apply the changes.
7. Test Kerberos authentication by connecting to the PostgreSQL server using the Kerberos user.
   - This step tests Kerberos authentication by connecting to the PostgreSQL server using the Kerberos user.

## Relevant Links

- [Kerberos Authentication Setup for PostgreSQL](https://www.postgresql.org/docs/current/kerberos-auth.html)
- [Kerberos Configuration Files](https://web.mit.edu/kerberos/krb5-1.12/doc/admin/conf_files/krb5_conf.html)
- [PostgreSQL Authentication Configuration File](https://www.postgresql.org/docs/current/auth-pg-hba-conf.html)

onelinerhub: [How do I set up PostgreSQL Kerberos authentication?](https://onelinerhub.com/postgresql/how-do-i-set-up-postgresql-kerberos-authentication)