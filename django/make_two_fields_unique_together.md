# How to make two fields unique together

Making two fields unique together means one field isn't totally unique in whole table, but its unique based on another field. You should add the following code in your model:

```python
class Product(models.Model):
    name = models.CharField(max_length=100)
    shop = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "shop"],
                name="unique_product_name_for_shop",
            ),
        ]
```

- constraints - where you should write all of your constraints of your model
- models.UniqueConstraint - constraint that make two fields unique
- fields=["name", "shop"] - fields that you want them to be unique together
- name - unique name for this constraint
