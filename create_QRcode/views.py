from django.shortcuts import render
import qrcode


def create_QRcode(request):
        
    link = request.GET.get('longlink')  

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4,)
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save('static/QR_code/qr_code.png')  

    return render(request=request, template_name='index.html', context={'qr_image': 'qr_code.png'})
