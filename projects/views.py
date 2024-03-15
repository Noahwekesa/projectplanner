from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    get_object_or_404,
    render,
    redirect,
)

from projects.models import Project


@login_required
def project_delete_view(request, id=None):
    """
    Delete project
    """
    instance = get_object_or_404(Project, id=id, project=request.project)
    if request.method == "POST":
        instance.delete()
        return redirect("project:list")
    context = {"instance": instance}
    return render(request, "items/delete.html", context)


@login_required
def project_detail_update_view(request, id=None):
    instance = get_object_or_404(Project, id=id, project=request.project)
    form = forms.ItemUpdateForm(request.POST or None, instance=instance)
    if form.is_valid():
        item_obj = form.save(commit=False)
        item_obj.last_modified_by = request.user
        item_obj.save()
        return redirect(item_obj.get_absolute_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, "items/detail.html", context)


@login_required
def project_create_view(request):
    if not request.project.is_activated:
        return render(request, "projects/activate.html", {})
    form = forms.ItemCreateForm(request.POST or None)
    if form.is_valid():
        item_obj = form.save(commit=False)
        item_obj.project = request.project
        item_obj.added_by = request.user
        item_obj.save()
        messages.success(request, "Task added successfully!")
        return redirect(item_obj.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "items/create.html", context)


def projects_list_view(request):
    """
    listing all projects
    """
    print(request.project.is_activated)
    projects = Project.objects.all(user=request.user)
    context = {
        "projects": projects,
    }
    return render(request, "projects/list.html", context)


@login_required
def projects_detail_view(request, handle):
    project_obj = get_object_or_404(Project, handle=handle)
    context = {"project_obj": project_obj}
    return render(request, "projects/detail.html", context)


@login_required
def delete_project_from_session(request):
    # delete session project
    try:
        del request.session["project_handle"]
    except:
        pass


@login_required
def activate_project_view(request, handle=None):
    # http://127.0.0.1:8000/activate/projects/project-planner
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
