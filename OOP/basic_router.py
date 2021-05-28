class Router(object):
    '''    Simple routing class for a web framework.
    The router accepts bindings for a given url, http method and an action.
    Then, when a request with a bound url and method comes in, it returns the result of the action.'''
    def __init__(self):
        self.urlpatterns = {}

    def bind(self, url, request_type, response):
        self.urlpatterns[url, request_type] = response

    def run_request(self, *request):
        if request in self.urlpatterns:
            return self.urlpatterns[(request)]()
        else:
            return 'Error 404: Not Found'


# Example
# router = Router()

# router.bind('/hello', 'GET', lambda: 'hello world')
#router.run_request('/hello', 'GET') == 'hello world'

# router.bind('/login', 'GET', lambda: 'Please log-in.')
# router.run_request('/login', 'GET') == 'Please log-in.'


