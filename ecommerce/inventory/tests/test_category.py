from ecommerce.inventory.models import Category


def test_create_category(single_category):
    new_category = single_category
    get_category = Category.objects.all().first()
    assert new_category.id == get_category.id


def test_create_category_with_children(category_with_child):
    new_category = category_with_child
    get_category = Category.objects.all().first()
    assert get_category.children.first().id == new_category.id
