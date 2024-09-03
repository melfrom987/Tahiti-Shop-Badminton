from django import template

register = template.Library()

@register.filter(name='format_price')
def format_price(value):
    # Convertir en chaîne de caractères pour manipuler
    value_str = str(value)
    
    # Séparer les parties entières et décimales
    parts = value_str.split('.')
    integer_part = parts[0]
    
    # Ajouter un espace tous les trois chiffres à partir de la droite
    integer_part_with_spaces = ""
    for i, digit in enumerate(reversed(integer_part)):
        if i > 0 and i % 3 == 0:
            integer_part_with_spaces = digit + " " + integer_part_with_spaces
        else:
            integer_part_with_spaces = digit + integer_part_with_spaces
    
    # Recomposer la valeur avec la partie décimale si elle existe
    if len(parts) > 1:
        formatted_value = integer_part_with_spaces + "." + parts[1]
    else:
        formatted_value = integer_part_with_spaces
    
    # Ajouter ' XPF' à la fin
    formatted_value += ' XPF'
    
    return formatted_value

@register.filter
def get_item_price(item_price, quantity):
    return item_price * quantity