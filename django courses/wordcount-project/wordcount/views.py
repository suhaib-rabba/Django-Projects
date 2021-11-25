from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1
        else:
            #add to the dictionary
            worddictionary[word] = 1

    trail=[1,2,3,4,5,6,7]
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    context={'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords
    ,'counting':trail}

    return render(request, 'count.html',context)