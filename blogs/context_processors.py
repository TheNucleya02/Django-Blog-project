from . import models

def get_categories(request):
    categories = models.Category.objects.all()
    return dict(categories=categories)