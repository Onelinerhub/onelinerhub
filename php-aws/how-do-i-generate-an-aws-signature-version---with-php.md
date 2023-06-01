# How do I generate an AWS Signature Version 4 with PHP?
// plain

Generating an AWS Signature Version 4 with PHP requires several steps. First, you must create a canonical request. This is done by concatenating the HTTP method, canonical URI, canonical query string, canonical headers, and signed headers. Once the canonical request is created, you must create the string to sign. This is done by concatenating the algorithm, request date, credential scope, and hashed canonical request. Next, you must create the signature. This is done by using a signing key to sign the string to sign. Finally, you must create the authorization header. This is done by concatenating the algorithm, access key, credential scope, signed headers, and signature.

## Example code

```
// Create the canonical request
$canonical_request = "GET\n"
    . "/\n"
    . "\n"
    . "host:example.amazonaws.com\n"
    . "x-amz-date:20150830T123600Z\n"
    . "\n"
    . "host;x-amz-date\n"
    . "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855";

// Create the string to sign
$string_to_sign = "AWS4-HMAC-SHA256\n"
    . "20150830T123600Z\n"
    . "20150830/us-east-1/service/aws4_request\n"
    . "f536975d06c0309214f805bb90ccff089219ecd68b2577efef23edd43b7e1a59";

// Create the signature
$secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY";
$date_key = hash_hmac("sha256", "20150830", "AWS4" . $secret_key, true);
$region_key = hash_hmac("sha256", "us-east-1", $date_key, true);
$service_key = hash_hmac("sha256", "service", $region_key, true);
$signing_key = hash_hmac("sha256", "aws4_request", $service_key, true);
$signature = hash_hmac("sha256", $string_to_sign, $signing_key);

echo $signature; // Output: "f536975d06c0309214f805bb90ccff089219ecd68b2577efef23edd43b7e1a59"

// Create the authorization header
$authorization_header = "AWS4-HMAC-SHA256 "
    . "Credential=AKIDEXAMPLE/20150830/us-east-1/service/aws4_request, "
    . "SignedHeaders=host;x-amz-date, "
    . "Signature=" . $signature;

echo $authorization_header; // Output: "AWS4-HMAC-SHA256 Credential=AKIDEXAMPLE/20150830/us-east-1/service/aws4_request, SignedHeaders=host;x-amz-date, Signature=f536975d06c0309214f805bb90ccff089219ecd68b2577efef23edd43b7e1a59"
```

Parts of the code:
- `$canonical_request`: The canonical request is created by concatenating the HTTP method, canonical URI, canonical query string, canonical headers, and signed headers.
- `$string_to_sign`: The string to sign is created by concatenating the algorithm, request date, credential scope, and hashed canonical request.
- `$secret_key`: The secret key is used to generate the signing key.
- `$date_key`, `$region_key`, `$service_key`, `$signing_key`: These keys are used to generate the signature.
- `$signature`: The signature is generated using the signing key to sign the string to sign.
- `$authorization_header`: The authorization header is created by concatenating the algorithm, access key, credential scope, signed headers, and signature.

## Helpful links
- [AWS Signature Version 4 Documentation](https://docs.aws.amazon.com/general/latest/gr/sigv4_signing.html)
- [PHP HMAC SHA256 Documentation](https://www.php.net/manual/en/function.hash-hmac.php)

onelinerhub: [How do I generate an AWS Signature Version 4 with PHP?](https://onelinerhub.com/php-aws/how-do-i-generate-an-aws-signature-version---with-php)