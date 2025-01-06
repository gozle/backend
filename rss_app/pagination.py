from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10   # default number of items per page
    page_size_query_param = "page_size" #query param to control page size
    max_page_size = 100 # maximum items per page