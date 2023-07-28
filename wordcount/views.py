#wordcount
from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'homecount.html')

def count(request):
    wordtext = request.GET['wordtext']
    wordlist = wordtext.split()
    worddict = {}
    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1

    count = len(worddict)
    return render(request, 'countwords.html', {'textentered' : wordtext , 'wordcount' : count , 'worddict' : worddict.items() })

def about(request):
    return render(request, 'about.html')
