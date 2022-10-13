from rest_framework.decorators import api_view
from rest_framework.response import Response
import base64

# Create your views here.

@api_view(('GET', 'POST'))
def saveImage(request):
    print("###############")
    img = request.data["Image"].file
    
    #data12 = img.read()
    #UU = data12.encode("base64")
    #UUU = base64.b64decode(UU)

    imgbin = img.read()
    imgB64 = base64.b64encode(imgbin).decode()
    #p_img = request.POST.get('image')
    return Response(data=imgB64)