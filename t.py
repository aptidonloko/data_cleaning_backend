from lib.google_search_results import GoogleSearchResults

params = {
    "q" : "name,streetAddress,addressCountry",
    "google_domain" : "google.com",
    "serp_api_key": "AIzaSyBD5A3fk9HX8EoWs0z26bOxt0Ox_FRJIpo"
}

query = GoogleSearchResults(params)
dictionary_results = query.get_dictionary()
print(dictionary_results)
