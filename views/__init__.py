def initialize_routes(api):
    from .books import initialize_routes as init_books_routes
    init_books_routes(api)
    