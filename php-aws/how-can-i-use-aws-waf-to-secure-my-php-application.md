# How can I use AWS WAF to secure my PHP application?
// plain

AWS WAF can be used to secure a PHP application by setting up rules and conditions to filter and block malicious requests.

For example, the following code block can be used to create a rule that blocks requests with a malicious User-Agent header:
```
aws waf create-rule \
--name BlockMaliciousUserAgent \
--metric-name BlockMaliciousUserAgent \
--change-token $CHANGE_TOKEN \
--predicates '[
    {
        "Negated": false,
        "Type": "ByteMatch",
        "DataId": "MaliciousUserAgentList",
        "FieldToMatch": {
            "Type": "HEADER",
            "Data": "user-agent"
        }
    }
]'
```

The following code block can be used to create a condition that contains a list of malicious User-Agent headers:
```
aws waf create-byte-match-set \
--name MaliciousUserAgentList \
--change-token $CHANGE_TOKEN \
--byte-match-tuples '[
    {
        "FieldToMatch": {
            "Type": "HEADER",
            "Data": "user-agent"
        },
        "TargetString": "MaliciousUserAgent1",
        "TextTransformation": "NONE"
    },
    {
        "FieldToMatch": {
            "Type": "HEADER",
            "Data": "user-agent"
        },
        "TargetString": "MaliciousUserAgent2",
        "TextTransformation": "NONE"
    }
]'
```

Once the rule and condition have been created, they can be added to a web ACL which can then be associated with the PHP application.

1. Create a rule that blocks requests with a malicious User-Agent header
    * `aws waf create-rule`
2. Create a condition that contains a list of malicious User-Agent headers
    * `aws waf create-byte-match-set`
3. Add the rule and condition to a web ACL
    * `aws waf create-web-acl`
4. Associate the web ACL with the PHP application
    * `aws waf associate-web-acl`

## Helpful links
- [AWS WAF Documentation](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html)
- [Create a Rule](https://docs.aws.amazon.com/waf/latest/APIReference/API_CreateRule.html)
- [Create a Byte Match Set](https://docs.aws.amazon.com/waf/latest/APIReference/API_CreateByteMatchSet.html)
- [Create a Web ACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_CreateWebACL.html)
- [Associate a Web ACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_AssociateWebACL.html)

onelinerhub: [How can I use AWS WAF to secure my PHP application?](https://onelinerhub.com/php-aws/how-can-i-use-aws-waf-to-secure-my-php-application)