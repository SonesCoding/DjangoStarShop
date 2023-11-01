from django.views import View
from django.views.generic import ListView
from django.shortcuts import render,redirect, get_object_or_404

from .models import Star
from .forms import StarForm, CartForm

def hp(request):
         return render(request,'starshop/hp.html')
        
def lab(request):
        return render(request,'starshop/lab.html')

##def basic(request):
    ## return render(request,'starshop/basic.html',context={'star_list':models.Star.objects.all()})

def star_detail(request, name, price, color, Quote, createdBy):
    star = get_object_or_404(
        Star,
        name = name,
        price = price,
        color = color,
        Quote = Quote,
        createdBy = createdBy
        )
    
    return render(
        request,
        'starshop/star_detail.html',
        {'star': star})

class star_create(View):
    form_class = StarForm
    template_name = 'starshop/lab.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'form': self.form_class()})

    def star(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_star = bound_form.save()
            return redirect(new_star)
        else:
            return render(
                request,
                self.template_name,
                {'form': bound_form})
            
            ## This create view is from the module 5. I liked this way 
            ##over all other options I had explored
class checkout(View):
    form_class = CartForm
    template_name = 'starshop/shop-cart.html'
    
    def get(self, request):
        return render(
            request,
            self.template_name,
            {'form': self.form_class()})