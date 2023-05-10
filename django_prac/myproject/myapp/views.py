from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def wordCount(request):
    return render(request, "wordCount.html")

def result(request):
    entered_text = request.GET['fulltext']
    word_list = entered_text.split()

    word_dictionary = {} #빈 딕셔너리 생성

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    return render(request, "result.html", {'alltext2': len(word_list), 'alltext': entered_text, 'dictionary': word_dictionary.items()})
    # 'alltext'에 해당하는 key는 template에서 사용할 변수
    # entered_text에 해당하는 value는 views에서 선언한 함수

def hello(request):
    entered_name = request.GET['user_name']
    return render(request, "hello.html", {'user_name': entered_name})
