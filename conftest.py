import pytest
import factory
from pytest_factoryboy import register

from tests.factories import CategoryFactory, ProductTypeFactory, \
    ProductSpecifcationFactory, ProductSpecificationValueFactory, ProductFactory, CustomerFactory, AddressFactory


register(CategoryFactory)
register(ProductTypeFactory)
register(ProductSpecifcationFactory)
register(ProductSpecifcationValueFactory)
register(ProductFactory)
register(AddressFactory)

register(CustomerFactory)

@pytest.fixture
def product_category(db, category_factory):
    category = category_factory.create()
    return category


@pytest.fixture
def product_type(db, product_type_factory):
    product_type = product_type_factory.create()
    return product_type


@pytest.fixture
def product_specification(db, product_specification_factory):
    product_spec = product_specification_factory.create()
    return product_spec


@pytest.fixture
def product( product_factory):
    product = product_factory.create()
    return product


@pytest.fixture
def product_spec_value(db, product_specification_value_factory):
    product_spec_value = product_specification_value_factory.create()
    return product_spec_value


#CUSTOMER


@pytest.fixture
def customer(db, customer_factory):
    new = customer_factory.create()
    return new


@pytest.fixture
def adminuser(db, customer_factory):
    new = customer_factory.create(name="admin_user", is_staff=True, is_superuser=True)
    return new

@pytest.fixture
def address(db, address_factory):
    new_address = address_factory.create()
    return new_address