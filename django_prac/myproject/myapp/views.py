from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def wordCount(request):
    return render(request, "wordCount.html")

def result(request):
    entered_text = request.GET['fulltext'] # 요청이 들어오면 풀텍스트 이름의 텍스트아리아의 데이터 가져와 변수에 저장
    word_list = entered_text.split() # 공백 기준으로 문자열 나눠 리스트에 저장

    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    count = 0

    for word in word_list:
        count = count + 1
    


    return render(request, "result.html", {'alltext': entered_text, 'dictionary': word_dictionary.items(), 'count': count})

def hello(request):
    name_text = request.GET['hello']
    return render(request, "hello.html", {'hello': name_text})