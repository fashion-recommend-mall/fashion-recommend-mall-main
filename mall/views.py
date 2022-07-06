import requests

from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from mall.forms import UploadFileForm
from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')
deep_learning_server = "http://localhost:3000"

# Create your views here.
def index(request):

  if request.method == 'POST':
      form = UploadFileForm(request.POST, request.FILES)

      if form.is_valid():

        f = request.FILES["file"]
        path = default_storage.save('static/media/img.jpeg', ContentFile(f.read()))

        #result = requests.get(deep_learning_server+f'/upload?img_path=http://localhost:8000/{path}')

        #print(result.text)
        return render(request, 'mall.html')
  else:
      form = UploadFileForm()

  return render(request, 'style.html')

    