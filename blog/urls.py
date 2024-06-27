from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Index.as_view()),
    path('about/', views.AboutList.as_view(), name='about-detail'),
    path('projects/', views.ProjectList.as_view()),
    path('blog/', views.BlogList.as_view()),
    path('certificates/', views.CertificatesList.as_view()),
    path('<slug:slug>/blog', views.BlogDetail.as_view(), name='blog_detail'),
    path('<slug:slug>/projects', views.ProjectDetail.as_view(), name='projects_detail'),
    path('documents/', views.DocumentList.as_view(), name='document_list'),
    path('documents/<int:pk>/', views.DisplayPDFView.as_view(), name='display_pdf'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)