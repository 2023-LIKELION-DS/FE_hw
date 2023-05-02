from django.shortcuts import render

def index(request):
    return render(request, "index.html")
def wordCount(request):
    return render(request, "wordCount.html")
def result(request):
    entered_text = request.GET['fulltext']  #입력받은 데이터를 저장함
    word_list = entered_text.split() #공백을 기준으로 문자열을 나눔

    word_dictionary = {} 

    for word in word_list:
        if word in word_dictionary: #안에 있으면,
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    return render(request, "result.html", {'alltext':entered_text, 'dictionary':word_dictionary.items()})
#alltext의 값을 enterd_text에 담아 사용하겠다. 
# Create your views here.

#list 함수로 만들기 과제2
