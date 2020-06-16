from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,'homepage.html')
def about(request):
    return render(request,'about.html')
def count(request):
    word=request.GET['fulltext']
    wordlist = word.split()
    worddictionary = {}
    for words in wordlist:
               if words in worddictionary:
                   #increase
                   worddictionary[words] +=1
               else:
                   #add to dictionary
                   worddictionary[words] =1

    sortedwords=sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request,'count.html',{'madness':word, 'count': len(wordlist),'sortedwords':sortedwords})
