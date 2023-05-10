from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def wordCount(request):
    return render(request, "wordCount.html")

def result(request):
    return render(request, "result.html")

def hello(request):
    entered_name = request.GET['userName']
    return render(request, "hello.html", {'userName': entered_name})

def result(request):
    entered_text = request.GET['fulltext']
    word_list = entered_text.split()

    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    
    return render(request, 'result.html', {'alltext2':len(word_list),'alltext': entered_text, 'dictionary': word_dictionary.items()})
