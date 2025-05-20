from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login_view, name='login'),
    path('', views.dashboard, name='dashboard'),
    path('admin_panel', views.admin_panel, name='admin_panel'),
    path('topic/<int:id>', views.topic_view, name='topic'),
    path('admin_topic/<int:id>', views.admin_topic, name='admin_topic'),
    path('notes/<int:id>', views.note_view, name='note'),
    path('admin_note/<int:id>', views.admin_note, name='topic'),
    path('add_subject', views.add_subject, name='add_subject'),
    path('add_topic', views.add_topic, name='add_topic'),
    path('add_note', views.add_note, name='add_note'),
    path('edit_subject', views.edit_subject, name='edit_subject'),
    path('about', views.about, name='about'),
    path('logout', views.logout_view, name='logout'),
    path('privacy_policy', views.privacy_policy, name="privacy_policy"),
    #path('get_class', views.get_class, name='get_class')
]