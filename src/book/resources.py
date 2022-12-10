from import_export import resources
from . import models


class BookResource(resources.ModelResource):
    class Meta:
        model = models.Book
