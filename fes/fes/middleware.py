from django.shortcuts import redirect

"""
Created by Wenqiang Kuang.

This middleware enable authentications for all management_app related urls. Login is required before visiting all other
urls. 
"""


class CheckUser(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and \
                (request.path.startswith('/management_app/') or request.path.startswith('/login')):
            return redirect("/")

        response = self.get_response(request)

        return response
