from .models import Product

def product_count(request):
    if request.user.is_authenticated:
        count = Product.objects.filter(user=request.user).count()
    else:
        count = 0
    return {'product_count':count}