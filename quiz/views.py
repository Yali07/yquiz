from django.shortcuts import redirect, render, get_object_or_404
from .forms import TitleForm, QuestionForm
from .models import Question,QuizTitle

# Create your views here.

def index(request):
    form = TitleForm()
    if request.method == 'POST':
        form = TitleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    title = QuizTitle.objects.all()
    titles = []
    for t in title:
        count = Question.objects.filter(title=t).count()
        if not request.user.is_superuser:
            if count == 10:
                titles.append(QuizTitle.objects.get(title=t))
        else:
            titles = title
    context = {"title":titles}
    return render(request,'home.html',context)

def quiz_view(request,slug):
    title = get_object_or_404(QuizTitle,slug=slug)
    questions = title.questions.all()
    question_count= questions.count()
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.title = title
            quiz.save()
            return redirect("quiz",slug=slug)
    context = {"title":title}
    if question_count == 10:
        q1=title.questions.all()[0]
        q2=title.questions.all()[1]
        q3=title.questions.all()[2]
        q4=title.questions.all()[3]
        q5=title.questions.all()[4]
        q6=title.questions.all()[5]
        q7=title.questions.all()[6]
        q8=title.questions.all()[7]
        q9=title.questions.all()[8]
        q10=title.questions.all()[9]
        context ={'q1':q1,'q2':q2,'q3':q3,'q4':q4,'q5':q5,'q6':q6,'q7':q7,'q8':q8,'q9':q9,'q10':q10,'question_count':question_count,"title":title}
    return render (request,'quiz.html',context)