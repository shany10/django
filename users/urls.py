from django.urls import path

from . import views, adminViews

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.login, name="login"),
    path("inscription", views.inscription, name="inscription"),
    path('get_user_details', views.GetUserDetails),
    path('logout', views.Logout),
    path('isLogin', views.isLogin),
    path('homeAdmin', adminViews.homeAdmin),
    path('secretary', adminViews.secretaryAdmin),
    path('instructor', adminViews.instructorAdmin),
    path('student', adminViews.studentAdmin),
    path('planning', adminViews.planningAdmin),
    path('forfait', adminViews.forfaitAdmin),
    path('add_instructor_save', adminViews.add_instructor_save),
    path('add_secretary_save', adminViews.add_secretary_save),
    path('add_student_save', adminViews.add_student_save),
    path('add_forfait_save', adminViews.add_forfait_save)
]