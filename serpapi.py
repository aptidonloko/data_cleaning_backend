from lib.google_search_results import GoogleSearchResults

params = {
    "q" : "streetAddress",
    "hl" : "en",
    "gl" : "us",
    "google_domain" : "google.com",
    "serp_api_key": "AIzaSyBD5A3fk9HX8EoWs0z26bOxt0Ox_FRJIpo",
}

query = GoogleSearchResults(params)
json_results = query.get_json()
print(json_results)

