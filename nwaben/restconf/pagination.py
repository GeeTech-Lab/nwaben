from rest_framework import pagination


class nwabenAPIPagination(pagination.LimitOffsetPagination):
    default_limit = 10
    max_limit = 20