import pytest
from django.urls import reverse


def test_store_category_string(product_category):
	assert product_category.__str__() == "django"

def test_category_reverse_url(client, product_category):
	category = product_category
	url = reverse("store:all_products", args=[category])
	resposne = client.get(url)
	assert resposne.status_code == 200


def test_product_spec_string(product_specification):
	assert product_specification.__str__() == "drosera"


def test_product_string(product):
	assert product.__str__() == "product_title"


def test_product_url_resolve(client, product):
	slug = "product_slug"
	url = reverse("store:product_detail", args=[slug])
	response = client.get(url)
	assert response.status_code == 200


def test_product_specifcation_value(product_spec_value):
	assert product_spec_value.__str__() == "100"