from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.contenttypes.models import ContentType
from .models import Accessory, Shoe, String, Bag, Racket, Clothe, Shuttle, ProductImage
from .forms import AccessoryForm, ShoeForm, StringForm, BagForm, RacketForm, ClotheForm, ShuttleForm, ProductImageFormSet
from django.contrib.auth.decorators import login_required

@login_required
def edit_product(request, category, product_id):
    model_map = {
        'accessory': Accessory,
        'shoe': Shoe,
        'string': String,
        'bag': Bag,
        'racket': Racket,
        'clothe': Clothe,
        'shuttle': Shuttle,
    }
    form_map = {
        'accessory': AccessoryForm,
        'shoe': ShoeForm,
        'string': StringForm,
        'bag': BagForm,
        'racket': RacketForm,
        'clothe': ClotheForm,
        'shuttle': ShuttleForm,
    }

    model_class = model_map.get(category)
    form_class = form_map.get(category)

    if model_class is None or form_class is None:
        return HttpResponseForbidden("Invalid category")

    product = get_object_or_404(model_class, id=product_id)

    # Créer un formulaire pour le produit principal
    if request.method == 'POST':
        product_form = form_class(request.POST, request.FILES, instance=product)

        if product_form.is_valid():
            product_form.save()
            return redirect('product_list')
    else:
        product_form = form_class(instance=product)

    return render(request, 'private/edit_product.html', {
        'product': product,
        'product_form': product_form,
        'category': category,
    })