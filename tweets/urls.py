from django.urls import path , re_path
# from .views import TweetListView, TweetCreateView

from . import views

# app_name = "tweets"

urlpatterns = [
    # path('tweets/new/', TweetCreateView.as_view(), name='tweet_new'),
    # path('', TweetListView.as_view(), name='home'),
    path('tweets/new/', views.tweet_new, name='tweet_new'),
    path('', views.tweet_list, name='home'),
    path('delete/<int:id>', views.deleteTweet, name='delete_tweet'),
]