from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    get_object_or_404,
    render,
    redirect,
)

from projects.models import Project
from . import forms


@login_required
def project_list_view(request):
    object_list = Project.objects.filter(owner=request.user)
    return render(request, "projects/list.html", {"object_list": object_list})


@login_required
def project_detail_update_view(request, handle=None):
    instance = get_object_or_404(Project, handle=handle, owner=request.user)
    form = forms.ProjectUpdateForm(request.POST or None, instance=instance)
    if form.is_valid():
        project_obj = form.save(commit=False)
        project_obj.last_modified_by = request.user
        project_obj.save()
        return redirect(project_obj.get_absolute_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, "projects/detail.html", context)


@login_required
def project_delete_view(request, handle=None):
    """
    Delete project
    """
    instance = get_object_or_404(Project, handle=handle, owner=request.project)
    if request.method == "POST":
        instance.delete()
        return redirect("project:list")
    context = {"instance": instance}
    return render(request, "projects/delete.html", context)


@login_required
def project_create_view(request):
    if not request.project.is_activated:
        return render(request, "projects/create.html", {})
    form = forms.ProjectCreateForm(request.POST or None)
    if form.is_valid():
        project_obj = form.save(commit=False)
        project_obj.project = request.project
        project_obj.added_by = request.user
        project_obj.save()
        return redirect(project_obj.get_absolute_url())
    context = {"form": form}
    return render(request, "projects/create.html", context)


@login_required
def projects_detail_view(request, handle):
    project_obj = get_object_or_404(Project, handle=handle)
    context = {"project_obj": project_obj}
    return render(request, "projects/detail.html", context)


@login_required
def delete_project_from_session(request):
    try:
        del request.session["project_handle"]
    except:
        pass


@login_required
def activate_project_view(request, handle=None):
    try:
        project_obj = Project.objects.get(owner=request.user, handle=handle)
    except:
        project_obj = None
        print("not here")
    if project_obj is None:
        delete_project_from_session(request)
        messages.error(request, "Project could not activate. Try again.")
        return redirect("projects")
    request.session["project_handle"] = handle
    messages.success(request, "Project activated.")
    print(project_obj, handle)
    return redirect("projects:list")


@login_required
def deactivate_project_view(request, handle=None):
    delete_project_from_session(request)
    messages.success(request, "Project Deactivated.")
    return redirect("projects")
