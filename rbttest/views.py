from django.shortcuts import render

def question_list(request):
    return render(request, 'rbttest/question_list.html', {})