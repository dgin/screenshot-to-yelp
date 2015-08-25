from django.shortcuts import render


from app1.forms import ScreenshotUploadForm
from app1.screenshot_yelp_script import script


def index(request):
    if request.method == 'POST':

        form = ScreenshotUploadForm(request.POST, request.FILES)
        if form.is_valid():
            data = script.load_website_from_data(request.FILES["image"])
            try:
                text = data["address"]
            except:
                text = ''
        else:
            text = ''
        return render(request, 'index.html', {'form': form, 'text': text})

    else:
        form = ScreenshotUploadForm()
        text = ''
    return render(request, 'index.html', {'form': form, 'text': text})