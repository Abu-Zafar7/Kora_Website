from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.http import JsonResponse
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm, SignUpForm

def home(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'website/home.html', {'questions': questions})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully! You can login now.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SignUpForm()
    return render(request, 'website/signup.html', {'form': form})


@login_required
def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            messages.success(request, 'Question posted successfully!')
            return redirect('home')
    else:
        form = QuestionForm()
    return render(request, 'website/ask_question.html', {'form': form})

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answers.all().order_by('-created_at')
    if request.method == 'POST' and request.user.is_authenticated:
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            messages.success(request, 'Answer posted successfully!')
            return redirect('question_detail', pk=pk)
    else:
        form = AnswerForm()
    return render(request, 'website/question_detail.html', {
        'question': question,
        'answers': answers,
        'form': form
    })

@login_required
def upvote_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    if request.user in answer.downvotes.all():
        answer.downvotes.remove(request.user)
    if request.user in answer.upvotes.all():
        answer.upvotes.remove(request.user)
    else:
        answer.upvotes.add(request.user)
    return JsonResponse({
        'upvotes': answer.upvote_count(),
        'downvotes': answer.downvote_count()
    })

@login_required
def downvote_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    if request.user in answer.upvotes.all():
        answer.upvotes.remove(request.user)
    if request.user in answer.downvotes.all():
        answer.downvotes.remove(request.user)
    else:
        answer.downvotes.add(request.user)
    return JsonResponse({
        'upvotes': answer.upvote_count(),
        'downvotes': answer.downvote_count()
    }) 
