from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ShoeForm, BagForm, ShuttleForm, AccessoryForm, ClotheForm, StringForm, RacketForm, GripForm
from .models import Shoe, Bag, Shuttle, Accessory, Clothe, String, Racket, Grip, Cart, CartItem, Order, OrderItem
from django.views.generic import ListView, UpdateView
from django.http import HttpResponseBadRequest, HttpResponseForbidden
from django.contrib.contenttypes.models import ContentType
from django.views.decorators.http import require_POST
from django.contrib import messages


def accessory(request):
    accessory = Accessory.objects.all()
    return render(request, 'inventory/categorie/accessory.html', {'accessory_instance': accessory})

def bag(request):
    bag = Bag.objects.all()
    return render(request, 'inventory/categorie/bag.html', {'bag_instance': bag})

def clothe(request):
    clothe = Clothe.objects.all()
    return render(request, 'inventory/categorie/clothe.html', {'clothe_instance': clothe})

def racket(request):
    racket = Racket.objects.all()
    return render(request, 'inventory/categorie/racket.html', {'racket_instance': racket})

def string(request):
    string = String.objects.all()
    return render(request, 'inventory/categorie/string.html', {'string_instance': string})

def shoe(request):
    shoe = Shoe.objects.all()
    return render(request, 'inventory/categorie/shoe.html', {'shoe_instance': shoe})

def shuttle(request):
    shuttle = Shuttle.objects.all()
    return render(request, 'inventory/categorie/shuttle.html', {'shuttle_instance': shuttle})


def product_detail(request, category, product_id):
    model_map = {
        'accessory': Accessory,
        'shoe': Shoe,
        'string': String,
        'bag': Bag,
        'racket': Racket,
        'clothe': Clothe,
        'shuttle': Shuttle,
    }
    model_class = model_map.get(category)

    if model_class is None:
        return HttpResponseForbidden("Invalid category")

    product = get_object_or_404(model_class, id=product_id)

    return render(request, 'inventory/product_detail.html', {'category':category, 'product': product})


# Vue pour la liste des produits (partie privée)
@login_required
def product_list(request):
    category = request.GET.get('category', None)
    products = None
    
    if category:
        if category == 'accessoire':
            products = Accessory.objects.all()
        elif category == 'chaussure':
            products = Shoe.objects.all()
        elif category == 'cordage':
            products = String.objects.all()
        elif category == 'sac':
            products = Bag.objects.all()
        elif category == 'raquette':
            products = Racket.objects.all()
        elif category == 'vetement':
            products = Clothe.objects.all()
        elif category == 'volant':
            products = Shuttle.objects.all()
    else:
        # Si aucune catégorie spécifique n'est sélectionnée, afficher tous les produits
        products = {
            'accessoires': Accessory.objects.all(),
            'chaussures': Shoe.objects.all(),
            'cordages': String.objects.all(),
            'sacs': Bag.objects.all(),
            'raquettes': Racket.objects.all(),
            'vetements': Clothe.objects.all(),
            'volants': Shuttle.objects.all(),
        }

    context = {
        'products': products,
        'category': category,
    }

    return render(request, 'private/product_list.html', context)

# Vue pour ajouter un produit (partie privée)
@login_required
def add_accessory(request):
    if request.method == 'POST':
        form = AccessoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = AccessoryForm()
    return render(request, 'inventory/produits/form_accessory.html', {'form': form})

@login_required
def add_shoe(request):
    if request.method == 'POST':
        form = ShoeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ShoeForm()
    return render(request, 'inventory/produits/form_shoe.html', {'form': form})

@login_required
def add_string(request):
    if request.method == 'POST':
        form = StringForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = StringForm()
    return render(request, 'inventory/produits/form_string.html', {'form': form})

@login_required
def add_racket(request):
    if request.method == 'POST':
        form = RacketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = RacketForm()
    return render(request, 'inventory/produits/form_racket.html', {'form': form})

@login_required
def add_bag(request):
    if request.method == 'POST':
        form = BagForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = BagForm()
    return render(request, 'inventory/produits/form_bag.html', {'form': form})
  
@login_required
def add_clothe(request):
    if request.method == 'POST':
        form = ClotheForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ClotheForm()
    return render(request, 'inventory/produits/form_clothe.html', {'form': form})

@login_required
def add_shuttle(request):
    if request.method == 'POST':
        form = ShuttleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ShuttleForm()
    return render(request, 'inventory/produits/form_shuttle.html', {'form': form})


@login_required
def add_grip(request):
    if request.method == 'POST':
        form = GripForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = GripForm()
    return render(request, 'inventory/produits/form_grip.html', {'form': form})
   

@login_required
def product_update(request):
    selected_category = request.GET.get('category')
    products = None

    if selected_category == 'shoe':
        products = Shoe.objects.all()
    elif selected_category == 'accessory':
        products = Accessory.objects.all()
    elif selected_category == 'racket':
        products = Racket.objects.all()
    elif selected_category == 'string':
        products = String.objects.all()
    elif selected_category == 'racket':
        products = Racket.objects.all()
    elif selected_category == 'bag':
        products = Bag.objects.all()
    elif selected_category == 'clothe':
        products = Clothe.objects.all()
    elif selected_category == 'shuttle':
        products = Shuttle.objects.all()

    if request.method == 'POST':
        category = request.POST.get('category')
        product_id = request.POST.get('product')
        return redirect('edit_product', category=category, product_id=product_id)

    return render(request, 'private/product_update.html', {
        'selected_category': selected_category,
        'products': products,
    })

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
        'grip': Grip,
    }
    form_map = {
        'accessory': AccessoryForm,
        'shoe': ShoeForm,
        'string': StringForm,
        'bag': BagForm,
        'racket': RacketForm,
        'clothe': ClotheForm,
        'shuttle': ShuttleForm,
        'grip': GripForm,
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

@login_required
def delete_product(request, category, product_id):
    if request.method == "POST":
        model_map = {
            'accessory': Accessory,
            'bag': Bag,
            'clothe': Clothe,
            'racket': Racket,
            'string': String,
            'shoe': Shoe,
            'shuttle': Shuttle,
        'grip': Grip,
        }
        model = model_map.get(category)
        if model:
            product = get_object_or_404(model, id=product_id)
            product.delete()
            return redirect('product_list')
        else:
            return HttpResponseForbidden("Invalid category")

    return HttpResponseForbidden("Invalid request method")

@login_required
def add_to_cart(request, category, product_id):
    model_map = {
        'accessory': Accessory,
        'shoe': Shoe,
        'string': String,
        'bag': Bag,
        'racket': Racket,
        'clothe': Clothe,
        'shuttle': Shuttle,
        'grip': Grip,
    }
    model_class = model_map.get(category)

    if model_class is None:
        return HttpResponseForbidden("Invalid category")

    product = get_object_or_404(model_class, id=product_id)
    quantity = int(request.POST.get('quantity', 1))

    if quantity > product.quantity:
        #logger.warning("Requested quantity exceeds available stock")
        return redirect('product_detail', category=category, product_id=product_id)

    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        content_type=ContentType.objects.get_for_model(product),
        object_id=product.id)
    cart_item.quantity = quantity
    cart_item.save()

    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()

    total_price = sum(item.get_total_price() for item in items)


    context = {
        'cart': cart,
        'items': items,
        'total_price': total_price,
    }

    return render(request, 'shop/cart_detail.html', context)

@login_required
@require_POST
def update_cart_item(request, category, item_id):
    item = get_object_or_404(CartItem, id=item_id)

    valid_categories = ['accessory', 'shoe', 'string', 'bag', 'racket', 'clothe', 'shuttle']
    if category not in valid_categories:
        return HttpResponseForbidden("Invalid category")

    if not user_can_modify_item(request.user, item):  # Exemple de fonction pour vérifier les autorisations
        return HttpResponseForbidden("Vous n'êtes pas autorisé à effectuer cette action.")

    quantity = int(request.POST.get('quantity', 0))
    if quantity < 0:
        return HttpResponseForbidden("La quantité ne peut pas être négative.")
    if quantity == 0:
        item.delete()
        messages.success(request, "L'article a été retiré du panier.")
    else:
        item.quantity = quantity
        item.save()
        messages.success(request, "La quantité a été mise à jour.")

    return redirect('cart_detail')


def user_can_modify_item(user, item):
    #Vérifier si l'utilisateur est propriétaire de l'objet
    if item.cart.user == user:  # Supposons que CartItem a une relation à un modèle Cart avec un champ 'user'
        return True

    return False

@login_required
@require_POST
def remove_cart_item(request, category, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    messages.success(request, "L'article a été retiré du panier.")
    return redirect('cart_detail')

 
    ###
@login_required
def orders_detail(request):
    if request.user.is_authenticated and request.user.groups.filter(name='Vendeurs').exists():
        orders = Order.objects.filter(product__isnull=False)  # Filtrer les commandes avec des produits
        context = {'orders': orders}
        return render(request, 'private/orders_detail.html', context)
    else:
        return render(request, 'home')

@login_required

@login_required
def add_to_order(request):
    if request.method == 'POST':
        products = request.POST.getlist('products[]')
        quantities = request.POST.getlist('quantities[]')
        
        # Vérifiez que les listes ont la même longueur
        if len(products) != len(quantities):
            return HttpResponseBadRequest("Les listes de produits et de quantités ne sont pas de la même longueur.")
        
        # Traitez les données pour créer la commande
        for product_id_str, quantity_str in zip(products, quantities):
            # Vérifiez que les valeurs ne sont pas vides
            if product_id_str and quantity_str:
                try:
                    product_id = int(product_id_str)
                    quantity = int(quantity_str)
                    
                    # Déterminez le type de produit en fonction de la catégorie ou du modèle
                    if 'accessory' in product_id_str:
                        product = Accessory.objects.get(id=product_id)
                    elif 'bag' in product_id_str:
                        product = Bag.objects.get(id=product_id)
                    elif 'clothe' in product_id_str:
                        product = Clothe.objects.get(id=product_id)
                    elif 'racket' in product_id_str:
                        product = Racket.objects.get(id=product_id)
                    elif 'shoe' in product_id_str:
                        product = Shoe.objects.get(id=product_id)
                    elif 'Shuttle' in product_id_str:
                        product = Shuttle.objects.get(id=product_id)
                    elif 'string' in product_id_str:
                        product = String.objects.get(id=product_id)
                    else:
                        return HttpResponseBadRequest("Type de produit non pris en charge.")
                    
                    # Créez l'élément de commande associé
                    order_item = OrderItem.objects.create(
                        product=product,
                        quantity=quantity,
                        # Ajoutez d'autres champs si nécessaire
                    )
                    
                    # Optionnel : Vous pouvez également faire d'autres actions comme déduire le stock du produit
                    
                except ValueError:
                    return HttpResponseBadRequest("Les valeurs de produits ou de quantités ne sont pas valides.")
                except (Accessory.DoesNotExist, Bag.DoesNotExist, Clothe.DoesNotExist, 
                        Racket.DoesNotExist, Shoe.DoesNotExist, Shuttle.DoesNotExist, 
                        String.DoesNotExist):
                    return HttpResponseBadRequest("Le produit avec cet ID n'existe pas.")
        
        # Redirigez l'utilisateur vers une page de confirmation ou une autre vue
        return redirect('home')
    
    return HttpResponseBadRequest("Méthode HTTP non autorisée.")