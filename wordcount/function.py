from django.shortcuts import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('你好！')  # HttpResponse 返回一个字符串
    return render(request, 'home.html') # request 请求

def count(request):
    print(request.GET['text'])
    # request.GET['text'] # 获取home.html中输入的文本信息
    user_text = request.GET['text']
    total_count = len(request.GET['text'])
    word_dict = {}
    for word in user_text:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    sorted_dict = sorted(word_dict.items(),
                         key=lambda w: w[1], reverse=True)

    return render(request, 'count.html',
                  {'total_count': total_count, 'user_text': user_text,
                   'word_dict': word_dict, 'sorted': sorted_dict})

def about(request):
    return render(request, 'about.html')