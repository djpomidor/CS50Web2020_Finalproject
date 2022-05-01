import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django import forms

from printery.models import *
from printery.forms import *
from django.forms import modelformset_factory

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("user-cabinet"))
    else:
            return render(request, "printery/index.html", {
        })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            if User.objects.get(username = username).is_customer:
                return HttpResponseRedirect(reverse("user-cabinet"))
            elif User.objects.get(username = username).is_employee:
                return HttpResponseRedirect(reverse("backside"))
            else:
                return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "printery/login.html", {
                "message": "Invalid username and/or password.", "form": UserForm()
            })
    else:
        return render(request, "printery/login.html", {
        "form": UserForm()
        })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request, user)
            if User.objects.get(username = user_form.cleaned_data.get('username')).is_customer:
                return HttpResponseRedirect(reverse("user-cabinet"))
            elif User.objects.get(username = user_form.cleaned_data.get('username')).is_employee:
                return HttpResponseRedirect(reverse("backside"))
        else:
            return render(request, "printery/register.html", {
                "message": user_form.errors, 'user_form': user_form
            })
    else:
        return render(request, "printery/register.html", {
        "user_form": UserForm()
        })

@login_required(redirect_field_name='index')
def user_cabinet_view(request):
    return render(request, "printery/user-cabinet.html")

@login_required(redirect_field_name='index')
def backside(request):
    return render(request, "printery/backside.html")

@login_required(redirect_field_name='index')
def create_order(request):
    PartsFormSet = modelformset_factory(Part, form=OrderPartsForm, fields=('part_name', 'pages', 'paper', 'color', 'laminate'),max_num=3, extra=3)
    if request.method == "POST":
        order_form = OrderForm(data=request.POST)
        formset = PartsFormSet(request.POST)
        # print(">>>>>>>>>", formset)

        if all([order_form.is_valid(), formset.is_valid()]):
            # print('!!!!!!!!', formset)
            for form in formset:
                # fields = form.cleaned_data
                # print ("QQQQQQQQQQQ", form['part_name'])
                # x = ""
                # for k, v in form.fields():
                #     if v != "" or "None" and k != 'part_name':
                #         break
                #     else:
                #         x = k[v]
                #         print("kkkkk___", x)
                # if x ==  "" or "None" and fields['part_name'] == 'Null':

                form.cleaned_data['part_name'] = "dfgdfgd"
                print('!!!!!!!!', form.fields['part_name'])
                form.save(commit=False)
            formset.save(commit=False)
            print('!3!3!3!3!3!3!!', form.fields['part_name'])


            order = order_form.save(commit=False)
            order.save()
            order.owner.add(request.user.id)
            order.save()

            instances = formset.save(commit=False)
            for instance in instances:
                print(">>>>>>>>>", instance)
                instance.order_id = order.id
                instance.save()

            return HttpResponseRedirect(reverse("user-cabinet"))
        else:
            return render(request, "printery/create-order.html", {
                "message": order_form.errors, 'order_form': order_form,
                "message_parts": formset.non_form_errors, "parts_form": formset
            })
    else:

        return render(request, "printery/create-order.html", {
            'order_form': OrderForm(),
            'parts_form': PartsFormSet(queryset=Part.objects.none()),
        })

####################################################################

@csrf_exempt
@login_required
def orders_view(request, order_number):
    try:
        order = Order.objects.get(owner=request.user, number=order_number)
    except Order.DoesNotExist:
        return JsonResponse({"error": "Order not found."}, status=404)

    if request.method == "GET":
        return JsonResponse(order.serialize())
