from django.shortcuts import render, HttpResponse



def post_list(request):
    selam = "Burada Gönderiler Listelenecek"
    return HttpResponse(selam)


def post_update(request):
    deneme = "Burada Gönderiler Güncellecektir"
    return HttpResponse(deneme)

def post_delete(request):
    selamet = "Burada Gönderiler Silecektir"
    return HttpResponse(selamet)

def post_create(request):
    merhaba ="<b> Burada gönderi Oluşturulacaktır.<b>"
    return HttpResponse(merhaba)


def sanatcilar(request,sayi):
    sanatcilar_sozluk = {

        '1': 'Eminem',
        '2': 'Tupack',
        '3': 'Tarkan',
        '4': 'Aleyna Tilki',
        '5': 'Müslüm Gürses',
        '6': 'Neşet Ertaş',
        '98': 'teoman',
        '9': 'Selamet Şamlı',
        'selamet':'Yes'

    }

    sanatci = sanatcilar_sozluk.get(sayi,"Bu id numarasına ait sanatci bulunamadi")
    return HttpResponse(sanatci)