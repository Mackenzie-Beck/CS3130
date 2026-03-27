from django.http import HttpResponse

def allowed_user(allowed_groups=[]):
    def inner(func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_groups:
                return func(request, *args, **kwargs)
            else:
                return HttpResponse('<h1> Access is denied......</h1>')
        return wrapper_func
    return inner