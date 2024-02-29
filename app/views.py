from urllib import request

from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage


class Home(TemplateView):
    template_name = 'home.html'

def upload(request):
    context = {}
    if request.method == 'POST': #se o metodo no html for um post
        uploaded_file = request.FILES['document'] #aqui ele ta pegando o documento do front
        # print(uploaded_file.name) # . name é uma propriedade padrao que os arquivos tem dentro do django
        # agora va la no settings pra fazer o media_root e o media_url
        #vamos puxar a api agora
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file) #ja esta salvando no caminho que nos colocamos no media_root, e se pesquisarmos media/nomedoarquivo vamos conseguir ver esse arquivo na tela
        #o caminho media nao tem nada a ver o nome da pasta, ele está como media porque definimos no settings
        context ['url'] = fs.url(name) #mandando pro template
    return render(request,'upload.html', context) #tem que chamar ele no front
