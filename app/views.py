from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .models import UploadFile


class Home(TemplateView):
    template_name = 'home.html'


def upload(request):
    context = {}

    try:
        if request.method == 'POST':
            uploaded_file = request.FILES['document']
            fs = FileSystemStorage()
            name = fs.save(uploaded_file.name, uploaded_file)
            url = context['url'] = fs.url(name)

            new_upload = UploadFile(document=url)
            new_upload.save()

    except Exception as e:
        pass

    return render(request, 'upload.html', context)