from django.views import View
from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse, JsonResponse
from django.template import loader
from django.db.models import Sum
from employee.models import Employee, Position, Project
import json

# Create your views here.


def index(request):
    employees = Employee.objects.all().order_by("hire_date")

    return render(
        request, "employee.html", {"employees": employees, "count": len(employees)}
    )


def position(request):
    positions = Position.objects.all()

    return render(request, "position.html", {"positions": positions})


class ProjectView(View):
    def get(self, request):
        projects = Project.objects.all()

        return render(request, "project.html", {"projects": projects})

    def delete(self, request, id):
        project = Project.objects.get(id=id)
        project.delete()

        return JsonResponse({"status": "Success"})


class ProjectStaffView(View):
    def put(self, request, id, eid):
        staff = Employee.objects.get(id=eid)
        project = Project.objects.get(id=id)

        project.staff.add(staff)

        return JsonResponse({"status": "Success"})

    def delete(self, request, id, eid):
        staff = Employee.objects.get(id=eid)
        project = Project.objects.get(id=id)

        project.staff.remove(staff)

        return JsonResponse({"status": "Success"})


def project_detail(request, id):
    project = Project.objects.get(id=id)
    staffs = project.staff.all()

    start_date = project.start_date.strftime("%Y-%m-%d")
    due_date = project.due_date.strftime("%Y-%m-%d")

    return render(
        request,
        "project_detail.html",
        {
            "project": project,
            "staffs": staffs,
            "start_date": start_date,
            "due_date": due_date,
        },
    )
