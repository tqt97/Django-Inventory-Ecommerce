from django.contrib import admin
from django.urls import include, path

from ecommerce.drf import views
from ecommerce.search.views import SearchProductInventory

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/inventory/category/all/", views.CategoryListView.as_view(), name="category-list"),
    path("api/inventory/products/category/<str:query>/", views.ProductListView.as_view()),
    path("api/inventory/<int:query>/", views.ProductInventoryByWebId.as_view()),
    path("api/search/<str:query>/", SearchProductInventory.as_view()),
    path("__debug__/", include("debug_toolbar.urls")),
]
