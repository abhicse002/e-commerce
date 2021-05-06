#used for context processor inorder to make this view available throughout the website in different pages
from store.models import Category


def categories(request):
    return {
        'categories' :Category.objects.all()
    }