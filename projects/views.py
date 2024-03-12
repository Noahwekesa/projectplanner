from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    get_object_or_404,
    render,
    redirect,
)

from projects.models import Project


def projects_view(request):
    print(request.project.is_activated)
    projects = Project.objects.all()
    """Dashbaord for all the projects"""
    context = {
        "projects": projects,
    }
    return render(request, "projects/overview.html", context)


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
    return redirect("projects")


@login_required
def deactivate_project_view(request, handle=None):
    delete_project_from_session(request)
    messages.success(request, "Project Deactivated.")
    return redirect("projects")
