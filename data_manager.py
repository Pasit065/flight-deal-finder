
import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.edited_data_dict = {}

    def get_google_sheet_data(self):
        return requests.get(url = "https://api.sheety.co/97593a8b37701d613736370881bd41fc/flightDeals/prices")

    def set_editing_data_format(self, editing_col, new_data):
        self.edited_data_dict[editing_col] = new_data

    def get_iata_code(self, city_data, city_name):
        for city_component in city_data["locations"]:
            if city_component["name"] == city_name:
                return city_component["code"]
        
    def get_put_body_params(self):
        body = {}
        body["price"] = {}

        for editing_col in self.edited_data_dict:
            body["price"][editing_col] = self.edited_data_dict[editing_col]

        return body

    def put_data(self, row_num, body):
        return requests.put(url = f"https://api.sheety.co/221735387aa47ffc34f79e124d328d66/flightDealsProject/prices/{row_num}", json = body)
