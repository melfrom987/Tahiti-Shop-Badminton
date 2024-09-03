from django.conf import settings

class PrivatePathsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if hasattr(response, 'context_data'):
            response.context_data = response.context_data or {}
            response.context_data['private_paths'] = [
                '/inventory/product_update/',
                '/inventory/product_update/',
                '/inventory/product_delete/',
                '/inventory/product_detail/',
                '/home_private',
                # Ajoutez d'autres chemins privés ici
            ]
        return response