from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseForbidden


def require_hacker(view):
    """ A decorator for views that ensures a hacker exists """

    @login_required
    def wrapper(request, *args, **kwargs):

        # Try to retrieve the hacker
        try:
            _ = request.user.hacker

        # return to retrieve a forbidden response if it does not exist
        except ObjectDoesNotExist:
            return HttpResponseForbidden()

        return view(request, *args, **kwargs)

    # and return the wrapper
    return wrapper


def require_unset_component(component, alternative):
    """ A decorator for views that ensures a given hacker property does not exist """

    def decorator(view):
        @require_hacker
        def wrapper(request, *args, **kwargs):
            # if the given component does not exist, go to the alternate view
            if request.user.hacker.has_component(component):
                return alternative(request, *args, **kwargs)

            # else use the normal one
            return view(request, *args, **kwargs)

        # and return the wrapper
        return wrapper

    # and return the decorator
    return decorator


def require_setup_completed(alternative):
    """ A decorator for views that ensures that and hacker has setup all components """

    def decorator(view):
        @require_hacker
        def wrapper(request, *args, **kwargs):
            # if we are missing a component, return to the main page
            if request.user.hacker.get_first_unset_component() is not None:
                return alternative(request, *args, **kwargs)

            # else use the normal one
            return view(request, *args, **kwargs)

        # and return the wrapper
        return wrapper

    # and return the decorator
    return decorator
