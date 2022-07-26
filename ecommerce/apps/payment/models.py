from django.db import models
from django.utils.translation import gettext_lazy as _


class DeliveryOptions(models.Model):
    """The table contains all delivery options"""

    DELIVERY_CHOICES = [
        ("IS", "In Store"),
        ("SD", "Standard Delivery"),
        ("ED", "Expedited Delivery"),
    ]

    delivery_name = models.CharField(
        verbose_name=_("delivery_name"),
        help_text=_("Is required"),
        max_length=255,
    )

    delivery_price = models.DecimalField(
        verbose_name=_("delivery price"),
        help_text=_("999.99 is max price"),
        error_messages={
            "type": {
                "max_length": _("The price must be between 0 and 999.99"),
            },
        },
        max_digits=5,
        decimal_places=2,
    )

    delivery_method = models.CharField(
        choices=DELIVERY_CHOICES,
        verbose_name=_("delivery_method"),
        help_text=_("Is required"),
        max_length=255,
    )

    delivery_timeframe = models.CharField(
        verbose_name=_("delivery timeframe"),
        help_text=_("Is required"),
        max_length=255,
    )
    order = models.IntegerField(
        verbose_name=_("list order"),
        help_text=_("Is required"),
        default=0
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Delivery option")
        verbose_name_plural = _("Delivery options")

    def __str__(self):
        return self.delivery_name


class PaymentSelections(models.Model):
    """Options as per order"""

    name = models.CharField(
        verbose_name=_("name"),
        help_text=_("Required"),
        max_length=255,
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Payment Selection")
        verbose_name_plural = _("Payment Selections")

    def __str__(self):
        return self.name