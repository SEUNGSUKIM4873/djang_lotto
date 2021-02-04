from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm

# Create your views here.
def index(request):
    lottos = GuessNumbers.objects.all()
    return render(request, 'lotto/default.html', {'lottos':lottos})


def hello(request):
    return HttpResponse('<h1 style="color:red;">Hello, world!</h1>')


def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST) #채워진 form

        if form.is_valid() :
            lotto = form.save(commit = False) #DB에 반영은 안한다는 의미. 임시저장해서 lotto로 가져온 것.
            lotto.generate()

            return redirect('index_name')

    else :
        form = PostForm() #빈 상태로 받아들이는 것
        return render(request, 'lotto/form.html', {'form':form})


def detail(request, lottokey) : #lottokey는 반드시 일치하지 않아도 됨
    lotto = GuessNumbers.objects.get(pk=lottokey)
    return render(request, 'lotto/detail.html', {'lotto':lotto})
