def test_get_all_categories(api_client, category_with_multiple_children):
    endpoint = "/api/inventory/category/all/"
    response = api_client().get(endpoint)

    assert response.status_code == 200
    assert len(response.data) == len(category_with_multiple_children)
    # assert response.data["results"][0]["name"] == "parent"
    # assert response.data["results"][1]["name"] == "child"
