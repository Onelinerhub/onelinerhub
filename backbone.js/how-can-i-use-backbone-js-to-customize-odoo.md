# How can I use Backbone.js to customize Odoo?
// plain

Backbone.js can be used to customize Odoo by creating custom modules and views. For example, one can create a custom view for a specific model to display the data in a different way.

```
# create custom view
<record model="ir.ui.view" id="my_custom_view">
    <field name="name">My Custom View</field>
    <field name="model">my.model</field>
    <field name="arch" type="xml">
        <tree>
            <field name="field_1" />
            <field name="field_2" />
            <field name="field_3" />
        </tree>
    </field>
</record>
```

The code above creates a custom view for the model `my.model` with three fields `field_1`, `field_2` and `field_3`.

The custom view can be used in an action definition.

```
# create custom action
<record model="ir.actions.act_window" id="my_custom_action">
    <field name="name">My Custom Action</field>
    <field name="res_model">my.model</field>
    <field name="view_mode">tree</field>
    <field name="view_id" ref="my_custom_view" />
</record>
```

The code above creates an action that opens the model `my.model` with the custom view `my_custom_view`.

To use the custom action, one can add it to a menu.

```
# add custom action to menu
<menuitem id="my_custom_menu" name="My Custom Menu" action="my_custom_action" />
```

The code above adds the custom action to the main menu with the name "My Custom Menu".

## Helpful links

- [Odoo Documentation](https://www.odoo.com/documentation/13.0/)
- [Backbone.js Documentation](https://backbonejs.org/)

onelinerhub: [How can I use Backbone.js to customize Odoo?](https://onelinerhub.com/backbone.js/how-can-i-use-backbone-js-to-customize-odoo)