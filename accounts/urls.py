from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', views.Signup.as_view(), name='signup'),
    path('profile/update/', views.UpdateProfile.as_view(), name='update_profile'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', views.ViewProfile.as_view(), name='profile'),
    path('allProfiles/', views.ProfileViewList.as_view(), name='all_profiles'),
    path('<int:pk>/deleteProfile/', views.DeleteProfile.as_view(), name='delete_profile'),
    path('allUsers/', views.UserViewList.as_view(), name='all_users'),
    path('<int:pk>/deleteUser/', views.DeleteUser.as_view(), name='delete_user'),

]