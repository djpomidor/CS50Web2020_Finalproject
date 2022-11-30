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
import json

from printery.models import *
from printery.forms import *
from django.forms import modelformset_factory

# Create your views here.
################################################################################
def index(request):
    if request.user.is_authenticated and request.user.is_customer:
        return HttpResponseRedirect(reverse("user-cabinet"))
    elif request.user.is_authenticated and request.user.is_employee:
        return HttpResponseRedirect(reverse("manage"))
    else:
        return render(request, "printery/index.html", {
        })
################################################################################
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
                return HttpResponseRedirect(reverse("manage"))
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

################################################################################
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

################################################################################
def register(request):
    # CompanyFormSet = modelformset_factory(Company, form=CompanyForm, fields=('name',))
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        company_form = CompanyForm(data=request.POST)
        if all([user_form.is_valid(), company_form.is_valid()]):
            company_form.save()
            user = user_form.save(commit=False)
            user.company = Company.objects.get(name = company_form.cleaned_data.get('name'))
            user.set_password(user.password)
            user.save()
            login(request, user)
            if User.objects.get(username = user_form.cleaned_data.get('username')).is_customer:
                return HttpResponseRedirect(reverse("user-cabinet"))
            elif User.objects.get(username = user_form.cleaned_data.get('username')).is_employee:
                return HttpResponseRedirect(reverse("manage"))
        else:
            for field in user_form.errors:
                user_form[field].field.widget.attrs['class'] += ' is-invalid'
            for field in company_form.errors:
                company_form[field].field.widget.attrs['class'] += ' is-invalid'
            return render(request, "printery/register.html", {
                # "message": user_form.errors,
                "user_form": user_form,
                "company_form": company_form,
                # "message_company": company_form.errors,
            })
    else:
        return render(request, "printery/register.html", {
        "user_form": UserForm(),
        "company_form": CompanyForm(),
        })
################################################################################
@login_required(redirect_field_name='index')
def user_cabinet_view(request):
    if request.user.is_customer:
        return render(request, "printery/user-cabinet.html", {
        })
    else:
        return HttpResponseRedirect(reverse("manage"))
################################################################################

@login_required(redirect_field_name='index')
def create_order(request):
    PartsFormSet = modelformset_factory(Part, form=OrderPartsForm, fields=('part_name', 'pages', 'paper', 'color', 'laminate'),max_num=3, extra=3)
    if request.method == "POST":
        order_form = OrderForm(data=request.POST)
        formset = PartsFormSet(request.POST)

        if all([order_form.is_valid(), formset.is_valid()]):
            for form in formset:
                form.save(commit=False)
            formset.save(commit=False)
            order = order_form.save(commit=False)
            order.save()
            order.owner.add(request.user.id)
            order.save()

            instances = formset.save(commit=False)
            for instance in instances:
                instance.order_id = order.id
                instance.save()

            new_order = Order.objects.get(number=order.number)

            return render(request, "printery/create-order.html", {
                'order_form': order_form,
                'parts_form': Part.objects.filter(order_id=new_order.id),
                "successful_submit": True,
                "new_order": order,
            })
        else:
            return render(request, "printery/create-order.html", {
                "message": order_form.errors,
                "message_parts": formset.errors,
                "order_form": order_form,
                "parts_form": formset
            })
    else:

        return render(request, "printery/create-order.html", {
            'order_form': OrderForm(),
            'parts_form': PartsFormSet(queryset=Part.objects.none()),
        })
####################################################################

@csrf_exempt
@login_required
def orders_view(request, order_number = 0):
    if not order_number:
        orders = Order.objects.filter(owner=request.user).order_by("-created").all()
        # parts = Part.objects.filter(order_id=[order.id for order in orders])
        # print("!!!", parts)

        # for order in orders:
        #     for part in Part.objects.filter(order_id=order.id):
        #         # order | part
        #         resp.append(order.serialize() | part.serialize())


        # def ser(order):
        #     for part in Part.objects.filter(order_id=order.id):
        #         print("::::::::::", order.serialize() | part.serialize())
        #         return order.serialize()
        # print("!!!!!!", [order.serialize() for order in orders])
        # return JsonResponse([ser(order) for order in orders], safe=False)

        return JsonResponse([order.serialize() for order in orders], safe=False)

    try:
        order = Order.objects.get(owner=request.user, number=order_number)
    except Order.DoesNotExist:
        return JsonResponse({"error": "Order not found."}, status=404)

    if request.method == "GET":
        return JsonResponse(order.serialize())

#####################################################################
@login_required(redirect_field_name='index')
def manage(request):
    if request.user.is_customer:
        return HttpResponseRedirect(reverse("user-cabinet"))
    return render(request, "printery/manage.html")

################################################################################

@login_required(redirect_field_name='index')
def print_schedule(request):
    return render(request, "printery/manage.html")
