from django.shortcuts import render
from .forms import BasvuruForm

def basvuru(request):
    if request.method == 'POST':
        form = BasvuruForm(request.POST)
        if form.is_valid():
            form.save()
            form = BasvuruForm()

    else:
        form =BasvuruForm()


    context =  {

        'form' :form
    }
    return render(request, "home/index.html", context)



# Create your views here.
