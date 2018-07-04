from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden, Http404
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from hacker.models import CV

def is_allowed(request, username):
    """ Checks if a given request is allowed to access a given user image """
    # Super-users can immediatly access everything
    if request.user and request.user.is_superuser:
        return True
    
    return request.user.username == username


@login_required
def cv(request, username):
    if is_allowed(request, username):
        cv = get_object_or_404(CV, hacker__profile__username=username)
        if not cv.has_cv:
            raise Http404
        return cv_actual(cv)
    
    return HttpResponseForbidden()

def cv_prod(cv):
    """ Serves a CV URL for production """
    response = HttpResponse()
    response["Content-Disposition"] = "attachment; filename={0}".format(cv.filename)
    response["Content-Type"] = "application/pdf"
    response['X-Accel-Redirect'] = cv.internal_url
    return response

def cv_debug(cv):
    """ Serves a CV URL for development """
    response = HttpResponse(cv.cv.read(), "application/pdf")
    response["Content-Disposition"] = "attachment; filename={0}".format(cv.filename)
    return response



cv_actual = cv_debug if settings.DEBUG else cv_prod