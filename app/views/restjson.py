from django.http.response import JsonResponse
import json
from app.models import Branch

def getSidebarBranchData(request):
    context = []

    branches = Branch.objects.all()

    for branch in branches:
        context.append({'pk': branch.pk, 'name': branch.name})

    return JsonResponse(context, safe=False)