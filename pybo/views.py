import PIL
from django.shortcuts import render
from .models import Image
from django.http import HttpResponse

from account.models import Account
from PIL import Image

# 참고
# https://gosmcom.tistory.com/143 : 로그인 처리 이름 불러오기
# https://free-eunb.tistory.com/43 : 이미지 for 문처리

def index(request):
    userstate = request.session.get('user')
    name = {}

    if userstate: #현재 로그인 상태이면! 이름을 출력할 수 있게끔
        account = Account.objects.get(pk=userstate)
        #name['name'] = '문진영'
        name['name'] = account.username

        return render(request, 'main.html', name)

    else:
        return render(request, 'main.html')

def use(request):
    userstate = request.session.get('user')
    account = Account.objects.get(pk=userstate)
    name = account.username

    if request.method == "POST" and 'btnimg' in request.POST:
        img = request.FILES.get('image', None)
        '''re_img = PIL.open(img)
        
        src_width, src_height = re_img
        src_ratio = float(src_height) / float(src_width)
        dst_height = round(scr_ratio * width) '''

        if not img:
            #에러메시지 출력해줬음 좋겠음 이미지를 선택해주세요~~뭐 이런거 일단은 새로고침 형태로 이동
            imgList = Image.objects.filter(email=account.useremail)

            return render(request, 'use.html', {'name': name, 'imgList': imgList})
            #return render(request, 'use.html', {'name':name})

        else:
            image = Image(
                email=account.useremail,
                image = img,
            )

            image.save()

            #imgList = Image.objects.filter(email=account.useremail)
            #return HttpResponse(Image.image)
        imgList = Image.objects.filter(email=account.useremail)
        return render(request, 'use.html', {'name': name, 'imgList': imgList})

    else:
        imgList = Image.objects.filter(email=account.useremail)

        return render(request, 'use.html', {'name': name, 'imgList': imgList})
        #return render(request, 'use.html', {'name': name})


def image(request, id):
    #이미지 추출하기 버튼을 눌렀을 때
    if request.method=="POST" and 'btnrun' in request.POST:
        img_info = Image.objects.get(pk=id)
        img_rcs = img_info.image
        #여기서 새롭게 함수를 이동해야 하나?
        return HttpResponse("추출중입니다")

    else:
        userstate = request.session.get('user')
        account = Account.objects.get(pk=userstate)
        name = account.username

        imgList = Image.objects.filter(email=account.useremail)

        img_info = Image.objects.get(pk=id)
        img_rcs = img_info.image

        return render(request, 'use.html', {'name':name, 'imgList':imgList, 'img_rcs':img_rcs})