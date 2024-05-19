from django.shortcuts import render, redirect, get_object_or_404
from .models import Industry
from django.core.paginator import Paginator
from django.contrib.admin.views.decorators import staff_member_required
from .forms import IndustryForm
from django.contrib.auth.decorators import login_required


def industry_list(request):
    industries = Industry.objects.all().order_by('-created_at')  
    paginator = Paginator(industries, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'industries.html', {'page_obj': page_obj})

@login_required
@staff_member_required
def add_industry(request):
    if request.method == 'POST':
        form = IndustryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('industry_list')
    else:
        form = IndustryForm()
    return render(request, 'add_industry.html', {'form': form, 'header_style': 'light',})

def industry_detail(request, industry_id):
    industry = get_object_or_404(Industry, id=industry_id)
    return render(request, 'industries-single-industry.html', {'industry': industry})
