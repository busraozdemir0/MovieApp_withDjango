from django.shortcuts import render,redirect
from django.contrib.auth.models import User # User modeli alıyoruz
from django.contrib import auth
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password) # girilen bilgilere ait kulanıcı var mı yok mu?
        if user is not None: # gerçekten bir user objesi varsa
            auth.login(request, user) # sessionid oluşturacak
            messages.add_message(request, messages.SUCCESS, 'Oturum açıldı.')
            return redirect('/admin/login/')
        else:
            messages.add_message(request, messages.ERROR, 'Hatalı kullanıcı adı veya parola!')
            return redirect('login')
    else:
        return render(request, 'user/login.html')

def register(request):
    if request.method=='POST':
        # get form values
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        repassword=request.POST['repassword']

        if password == repassword:
            # Username
            if User.objects.filter(username = username).exists(): # username alanına göre filtreleme yaptıktan sonra gönderdiğimiz username eğer varsa True dönecek. Yani veritabanında aynı isimde girilmiş başka kullanıcı varsa mesajla uyaracağız.
                messages.add_message(request, messages.WARNING, 'Bu kullanıcı adı daha önceden alınmış.')
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists(): # username alanına göre filtreleme yaptıktan sonra gönderdiğimiz username eğer varsa True dönecek. Yani veritabanında aynı isimde girilmiş başka kullanıcı varsa mesajla uyaracağız.
                    messages.add_message(request, messages.WARNING, 'Bu e-mail daha önceden alınmış.')
                    return redirect('register')
                else:
                    # her şey tamam
                    user=User.objects.create_user(username=username, password=password, email=email) # create_superuser deseydik admin kullanıcısı gibi yetkileri olan kullanıcı oluşturacaktı
                    user.save()
                    messages.add_message(request, messages.SUCCESS, 'Hesabınız oluşturuldu.')
                    return redirect('login')
        else:
            print('Parolalar eşleşmiyor')

        return redirect('register') # başarılı olduktan sonra dönecek olan sayfa
    else:
        return render(request, 'user/register.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        messages.add_message(request,messages.SUCCESS,"Oturumunuz kapatıldı.")
    return redirect('index')