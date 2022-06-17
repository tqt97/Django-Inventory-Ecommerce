from django.http import HttpResponse
from ecommerce.drf.serializers import ProductInventorySerializer
from ecommerce.search.documents import ProductInventoryDocument
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from elasticsearch_dsl.query import Q


class SearchProductInventory(APIView, LimitOffsetPagination):
    productinventory_serializer = ProductInventorySerializer
    search_document = ProductInventoryDocument

    def get(self, request, query):
        try:
            q = Q("multi_match", query=query, fields=["product.name"], fuzziness="AUTO") & Q(
                "bool",
                should=[
                    Q("match", is_default=True),
                ],
                minimum_should_match=1,
            )

            search = self.search_document.search().query(q)
            response = search.execute()
            results = self.paginate_queryset(response, request, view=self)
            serializer = self.productinventory_serializer(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            return HttpResponse(e, status=500)
