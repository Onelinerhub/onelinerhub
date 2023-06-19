# How do I encrypt data stored in Amazon Redshift?
// plain

Amazon Redshift provides an encryption option for data stored in the cluster. The encryption is done using the Advanced Encryption Standard (AES) algorithm with 256-bit keys.

To encrypt data stored in Amazon Redshift, the following steps must be taken:

1. Create a master key in AWS KMS - This is done by creating a customer master key (CMK) in AWS KMS.

2. Create a database encryption key - This is done by using the CREATE ENCRYPTION KEY command in Redshift.

3. Encrypt the data - This is done by using the ENCRYPT command in Redshift.

## Example code

```SQL
-- Create a master key in AWS KMS
CREATE MASTER KEY;

-- Create a database encryption key
CREATE ENCRYPTION KEY;

-- Encrypt the data
ENCRYPT 'MyData';
```

## Output example

```
Encrypted data: 0x098F6BCD4621D373CADE4E832627B4F6
```

## Helpful links
- [Encrypting Data in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/encrypting-data.html)
- [AWS KMS Documentation](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)

onelinerhub: [How do I encrypt data stored in Amazon Redshift?](https://onelinerhub.com/amazon-redshift/how-do-i-encrypt-data-stored-in-amazon-redshift)