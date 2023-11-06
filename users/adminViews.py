from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse
from django.template import loader
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from users.models import RDV, CustomUser, Forfait

@csrf_exempt
def homeAdmin(request):
    template = loader.get_template('core/admin/homeAdmin.html')
    return HttpResponse(template.render())

@csrf_exempt
def planningAdmin(request):
    template = loader.get_template('core/admin/planning.html')
    return HttpResponse(template.render())


@csrf_exempt
def instructorAdmin(request):
    template = loader.get_template('core/admin/instructor.html')
    return HttpResponse(template.render())

@csrf_exempt
def add_instructor_save(request):
    if request.method != 'POST':
        return HttpResponse('Method Not Allowed')
    else: 
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        address = request.POST.get('address')
        password = request.POST.get('password')
        try:
            user = CustomUser.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password,
                user_type='Instructor'
            ) 
            user.instructor.address=address
            rdv_obj=RDV.objects.get(id=id)
            user.instructor.rdv_id=rdv_obj
            user.save()
            messages.success(request, 'Student added')
            return HttpResponseRedirect('/instructor')
        except:
            messages.error(request, 'Failed to add instructor')
            return HttpResponseRedirect('/instructor')
        
@csrf_exempt
def secretaryAdmin(request):
    template = loader.get_template('core/admin/secretary.html')
    return HttpResponse(template.render())

@csrf_exempt
def add_secretary_save(request):
    if request.method != 'POST':
        return HttpResponse('Method Not Allowed')
    else: 
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        address = request.POST.get('address')
        password = request.POST.get('password')
        try:
            user = CustomUser.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password,
                user_type='Secretary'
            ) 
            user.secretary.address=address
            user.save()
            messages.success(request, 'secretary added')
            return HttpResponseRedirect('/secretary')
        except:
            messages.error(request, 'Failed to add secretary')
            return HttpResponseRedirect('/secretary')

@csrf_exempt
def studentAdmin(request):
    template = loader.get_template('core/admin/student.html')
    return HttpResponse(template.render())

@csrf_exempt
def add_student_save(request):
    if request.method != 'POST':
        return HttpResponse('Method Not Allowed')
    else: 
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        forfait = request.POST.get('forfait')
        address = request.POST.get('address')
        password = request.POST.get('password')
        try:
            user = CustomUser.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password,
                user_type='Student'
            )
            user.student.address=address
            user.student.forfait=forfait
            rdv_obj=RDV.objects.get(id=id)
            user.student.rdv_id=rdv_obj
            user.save()
            messages.success(request, 'Student added')
            return HttpResponseRedirect('/student')
        except:
            messages.error(request, 'Failed to add student')
            return HttpResponseRedirect('/student')
        
@csrf_exempt
def forfaitAdmin(request):
    template = loader.get_template('core/admin/forfait.html')
    return HttpResponse(template.render())

@csrf_exempt
def add_forfait_save(request):
    if request.method != 'POST':
        return HttpResponseRedirect('Method Not Allowed')
    else: 
        forfait = request.POST.get('forfait')

        try:
            forfait_model=Forfait(forfait_hours=forfait)
            forfait_model.save()
            messages.success(request, 'Forfait added')
            return HttpResponseRedirect('/forfait')
        except:
            messages.error(request, 'Failed to add forfait')
            return HttpResponseRedirect('/forfait')