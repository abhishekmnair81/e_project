from shop.models import Categories

def links(request):

    c=Categories.objects.all()

    return {'links':c}