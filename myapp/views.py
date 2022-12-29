from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'name': 'Patrick',
        'age': 23,
        'nationality': 'British'
    }
    return render(request, 'index.html', context)


def counter(request):
    text = request.GET['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount_of_words': amount_of_words})


