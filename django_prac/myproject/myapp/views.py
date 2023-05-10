from django.shortcuts import render

# Create your views here.
def index(request) :
    return render(request, "index.html")

def wordCount(request) :
    return render(request, "wordCount.html")

def result(request) :
    entered_text = request.GET['fulltext']
    word_list = entered_text.split()

    word_dictionary = {}

    for word in word_list :
        if word in word_dictionary :
            word_dictionary[word] += 1
        else :
            word_dictionary[word] = 1

    totalCount = len(word_list)

    return render(request, "result.html", {'alltext': entered_text, 'dictionary': word_dictionary.items(), 'totalCount': totalCount})

def hello(request) :
    name = request.GET['name']

    return render(request, "hello.html", {'name': name})