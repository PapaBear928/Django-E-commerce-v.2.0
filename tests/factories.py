import factory
from ecommerce.apps.store.models import Category, ProductType, ProductSpecification, Product, ProductSpecificationValue
from ecommerce.apps.account.models import Address, Customer
from faker import Faker

fake = Faker()


# Store

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

        name = "django"
        slug = "django"


class ProductTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductType
        django_get_or_create = ("name",)

    name = "drosera"

class ProductSpecificationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductSpecification

    product_type = factory.SubFactory(ProductTypeFactory)
    name = "drosera"


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    product_type = factory.SubFactory(ProductTypeFactory)
    category = factory.SubFactory(CategoryFactory)
    title = "product_title"
    description = fake.text()
    slug = "product_slug"
    regular_price = "9.99"
    discount_price = "4.99"


class ProductSpecificationValueFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductSpecificationValue

    product = factory.SubFactory(ProductFactory)
    specification = factory.SubFactory(ProductSpecificationFactory)
    value = "100"


# Account

class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

        email = "a@a.com"
        name = "user1"
        mobile = "123456789"
        password = "password"
        is_active = True
        is_staff = False

        @classmethod
        def _create(cls, model_class, *args, **kwargs):
            manager = cls._get_menager(model_class)

            if "is_superuser" in kwargs:
                return manager.create_superuser(*args, **kwargs)
            else:
                return manager.create_user(*args, **kwargs)


class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Address

    customer = factory.SubFactory(CustomerFactory)
    full_name = fake.name()
    phone = fake.phone_number()
    zipcode = fake.postcode()
    address_line = fake.street_address()
    address_line2 = fake.street_address()
    city = fake.city_suffix()