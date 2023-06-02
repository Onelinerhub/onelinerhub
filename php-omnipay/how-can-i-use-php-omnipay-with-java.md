# How can I use PHP Omnipay with Java?
// plain

Using PHP Omnipay with Java is not possible as the two languages are not compatible. However, it is possible to use Omnipay in Java by using a Java library such as [Omnipay-Java](https://github.com/thephpleague/omnipay-java).

## Example code

```java
import com.omnipay.Omnipay;

public class Example {
    public static void main(String[] args) {
        Omnipay omnipay = new Omnipay("Stripe");

        // Set your secret key: remember to change this to your live secret key in production
        // See your keys here: https://dashboard.stripe.com/account/apikeys
        omnipay.setApiKey("sk_test_BQokikJOvBiI2HlWgH4olfQ2");

        // Charge the Customer instead of the card:
        Map<String, Object> chargeParams = new HashMap<String, Object>();
        chargeParams.put("amount", 10.00);
        chargeParams.put("currency", "USD");
        chargeParams.put("customer", "cus_4fdAW5ftNQow1a");
        Map<String, Object> charge = omnipay.charge(chargeParams);
        System.out.println(charge);
    }
}
```

## Output example

```
{id=ch_1BbWV9FoF5j8EQ, object=charge, amount=1000, amount_refunded=0, application=null, application_fee=null, balance_transaction=null, captured=true, created=1520391809, currency=usd, customer=cus_4fdAW5ftNQow1a, description=null, destination=null, dispute=null, failure_code=null, failure_message=null, fraud_details={}, invoice=null, livemode=false, metadata={}, on_behalf_of=null, order=null, outcome=null, paid=true, receipt_email=null, receipt_number=null, refunded=false, refunds={object=list, data=[], has_more=false, total_count=0, url=/v1/charges/ch_1BbWV9FoF5j8EQ/refunds}, review=null, shipping=null, source={id=card_1BbWV7FoF5j8EQ, object=card, address_city=null, address_country=null, address_line1=null, address_line1_check=null, address_line2=null, address_state=null, address_zip=null, address_zip_check=null, brand=Visa, country=US, customer=cus_4fdAW5ftNQow1a, cvc_check=pass, dynamic_last4=null, exp_month=8, exp_year=2018, fingerprint=Xt5EWLLDS7FJjR1c, funding=credit, last4=4242, metadata={}, name=null, tokenization_method=null}, source_transfer=null, statement_descriptor=null, status=succeeded, transfer_group=null}
```

The code above is an example of how to use the Omnipay-Java library to charge a customer using Stripe. The code first imports the Omnipay library, then creates an instance of the Omnipay class. It then sets the API key and creates a hashmap of parameters for the charge. Finally, it charges the customer and prints the output.

## Helpful links
- [Omnipay-Java](https://github.com/thephpleague/omnipay-java)
- [Stripe Documentation](https://stripe.com/docs/api)

onelinerhub: [How can I use PHP Omnipay with Java?](https://onelinerhub.com/php-omnipay/how-can-i-use-php-omnipay-with-java)