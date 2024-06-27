from django.shortcuts import render
from django.views import generic, View
from django.views.generic import TemplateView
from .models import Project, About, Blog, Certificates, Document
from django.http import FileResponse
from django.shortcuts import get_object_or_404


class ProjectList(generic.ListView):
    queryset = Project.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/projects.html'


class ProjectDetail(generic.DetailView):
    model = Project
    template_name = 'blog/project_detail.html'


class Index(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")


class AboutList(generic.ListView):
    queryset = About.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/about.html'


class BlogList(generic.ListView):
    queryset = Blog.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/blog.html'


class BlogDetail(generic.DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'


class CertificatesList(generic.ListView):
    queryset = Certificates.objects.all()
    template_name = 'certificates/certificates.html'


class DocumentList(generic.ListView):
    queryset = Document.objects.all()
    template_name = 'documents/documents.html'
    context_object_name = 'documents'


class DisplayPDFView(View):
    def get(self, request, pk, *args, **kwargs):
        document = get_object_or_404(Document, pk=pk)
        if document.pdf:
            return FileResponse(document.pdf.open('rb'), content_type='application/pdf')
        else:
            raise Http404("PDF not found")
