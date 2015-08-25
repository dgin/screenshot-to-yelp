import webbrowser
try:
    import Image
except ImportError:
    from PIL import Image
from PIL import ImageFilter
import pytesseract
import yelp_phone_search

'''
Uses a python wrapper for tesseract.
Pulls phone number, address, and categories from image.
'''
def data_from_screen(path):
    image = Image.open(path)
    # Enhance image: helps distinguish 3's,8's
    im1 = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    data = {}

    text = pytesseract.image_to_string(im1)
    text = text.translate(None, '!@#$%^&*()_+=[]{}|\\\'/;:"<>?')
    split = [s.rstrip() for s in text.splitlines() if s]
    for i in xrange(len(split)):
        print split[i]
        if split[i][-5:].isdigit() and not split[i].isdigit():
            data["address"] = split[i]
        # Categories are right below review quantity
        elif split[i][-6:] == "eviews":
            data["categories"] = split[i+1]
            data["name"] = split[i-1]

    text = text.translate(None, '!@#$%^&*()_+-=[]{}|\\\'/;:",.<>? ')
    for line in text.splitlines():
        if line.isdigit() and len(line) == 10:
            data["phone"] = line

    return data

'''
First queries the Yelp API's phone search with the phone number obtained above.
If it finds nothing, tries the generic search using address and categories.
'''
def load_website_from_data(path):
    data = data_from_screen(path)

    try:
        yelp_url = yelp_phone_search.main(data["phone"])["businesses"][0]["mobile_url"]
    except IndexError:
        try:
            yelp_url = yelp_phone_search.search_alt(data)["businesses"][0]["mobile_url"]
        except IndexError:
            return "Sorry! We couldn't find the business you're looking for!"

    webbrowser.open(yelp_url, new=2, autoraise=True)

    return data
