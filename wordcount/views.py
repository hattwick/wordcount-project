# Views inventory

from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    # return HttpResponse('Hello, Django User')
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext=request.GET['fulltext']
    print(fulltext) #prints to server log
    print('Word count ')
    wordlist = fulltext.split()
    print(wordlist)
    
    worddictionary = {}   #initialize word count dict

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    print(worddictionary.items)

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',{'fulltext':fulltext, 'count':len(wordlist),'sortedwords':sortedwords})
