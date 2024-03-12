from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404

from .models import Item
from . import forms


@login_required
def item_list_view(request):
    object_list = Item.objects.filter(project=request.project)
    context = {"object_list": object_list}
    return render(request, "items/list.html", context)


@login_required
def item_detail_update_view(request, id=None):
    instance = get_object_or_404(Item, id=id, project=request.project)
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
def item_create_view(request):
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
