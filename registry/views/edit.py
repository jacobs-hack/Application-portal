from django.contrib.messages import get_messages
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

from registry.views.registry import default_alternative
from ..decorators import require_setup_completed

from ..forms import HackerForm, AcademicForm, ApplicationForm, OrganizationalForm, CVForm


def editViewFactory(prop, FormClass, name, with_files=False):
    """ Generates an edit view for a given section of the profile """

    @require_setup_completed(default_alternative)
    def edit(request):

        # figure out the edit url to redirect to
        if prop is None:
            url = reverse('edit')
        else:
            url = reverse('edit_{}'.format(prop))

        # load the instance
        if prop is None:
            instance = request.user.hacker
        else:
            instance = getattr(request.user.hacker, prop)

        if request.method == 'POST':
            # load files from request (if set)
            if with_files:
                files = request.FILES or None
            else:
                files = None

            # load the form
            form = FormClass(data=request.POST, files=files, instance=instance)

            # check that the form is valid
            if form.is_valid():
                form.clean()

                # Create the Address form
                instance = form.save(commit=False)
                instance.save()

                # Add a success message
                messages.success(request, 'Changes saved. ')

                # and then continue to the main portal page.
                return redirect(url)

        # if we did not have any post data, simply create a new form
        else:
            form = FormClass(instance=instance)

        # and return the request
        return render(request, 'portal/edit.html',
                      {
                          'form': form,
                          'name': name,
                          'messsages': get_messages(request),
                          'with_files': with_files
                      })

    return edit

edit = editViewFactory(None,
                       HackerForm,
                       'General Information')
academic = editViewFactory('academic',
                           AcademicForm,
                           'Academic Data')

application = editViewFactory('application',
                              ApplicationForm,
                               'jacobsHack! Application')

organizational = editViewFactory('organizational',
                                 OrganizationalForm,
                                 'Organizational Details')

cv = editViewFactory('cv', 
                     CVForm,
                     'CV', 
                     with_files=True)


@require_setup_completed(default_alternative)
def password(request):
    # if we have something that needs to be setup return to the main page
    if request.user.hacker.get_first_unset_component() is not None:
        return redirect(reverse('portal'))

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request,
                             'Your password was successfully updated!')
            return redirect('edit_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'portal/edit.html', {
        'form': form,
        'name': 'Password',
        'messsages': get_messages(request),
        'with_files': False
    })
