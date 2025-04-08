from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import CustomLoginForm

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='website/login.html', form_class=CustomLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('ask/', views.ask_question, name='ask_question'),
    path('question/<int:pk>/', views.question_detail, name='question_detail'),
    path('answer/<int:answer_id>/upvote/', views.upvote_answer, name='upvote_answer'),
    path('answer/<int:answer_id>/downvote/', views.downvote_answer, name='downvote_answer'),
]