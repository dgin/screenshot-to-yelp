import rauth
 
def main(phone):
    params = get_search_parameters(phone)

    return get_results(params)
 
def get_results(params, is_phone=True):

    # API Keys here
    consumer_key = "LM8exyo5oOnZyV5MyyNIGA"
    consumer_secret = "7IAhPNR2oqW9acrZfA-KtYdn0Wo"
    token = "DQw_8H-jNPU86EchgVBvwl1JkOLbBSg1"
    token_secret = "ESk44SB54vuxJZHXe_YuN2SdEPM"

    session = rauth.OAuth1Session(
        consumer_key = consumer_key
        ,consumer_secret = consumer_secret
        ,access_token = token
        ,access_token_secret = token_secret)

    if is_phone:
        request = session.get("http://api.yelp.com/v2/phone_search",params=params)
    else:
        request = session.get("http://api.yelp.com/v2/search",params=params)

    # Transforms the JSON API response into a Python dictionary
    data = request.json()
    session.close()
    return data

def get_search_parameters(term):
    # See the Yelp API for more details
    params = {}
    params["phone"] = term
 
    return params

def search_alt(data):
    params = get_search_parameters_alt(data)

    return get_results(params, is_phone=False)

# If phone number returns nothing, try search terms
def get_search_parameters_alt(data):
    # See the Yelp API for more details, as above
    params = {}
    params["term"] = data["name"] + " " + data["categories"]
    params["location"] = data["address"]
    params["radius_filter"] = "500"
    params["limit"] = "1"
    params["sort"] = "1"

    return params
