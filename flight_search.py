
import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def searching_endpoint_city(self, kiwi_headers, body):
        return requests.get(url = "https://api.tequila.kiwi.com/locations/query", headers = kiwi_headers, params = body)


    def searching_flight(self, body, headers):
        return requests.get(url = "https://api.tequila.kiwi.com/search", params = body, headers = headers)