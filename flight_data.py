
import datetime as dt
import random
import pandas

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.starting_city_data = {}
        self.endpoint_city_data = {}
        self.every_flight_for_each_city = None
        self.sms_flights_dataframe = None

    def set_sms_flights_dataframe_to_empty(self):

        col_list = ["cityFrom", "cityTo", "price", "trip_start_date", "trip_end_date", "time", "date"]

        empty_dict = {col:[] for col in col_list}

        self.sms_flights_dataframe = pandas.DataFrame(empty_dict)

    def update_sms_flights_dataframe(self, flight):
        new_row_value = []

        for col in flight:
            new_row_value.append(flight[col])

        self.sms_flights_dataframe.loc[len(self.sms_flights_dataframe)] = new_row_value

    def get_randomaly_flight(self, available_flight_list):
        return random.choice(available_flight_list)

    def set_every_flight_for_each_city(self, city_flights):
        self.every_flight_for_each_city = city_flights

    def set_endpoint_city_data(self, data):
        self.endpoint_city_data = data

    def set_starting_city_data(self, city_name, iata_code):
        self.starting_city_data["city"] = city_name
        self.starting_city_data["iataCode"] = iata_code

    def set_iata_to_endpoint_city_data(self, iata_code, index):
        self.endpoint_city_data[index]["iataCode"] = iata_code

    def get_available_total_days_trip_flights(self):
        available_total_days_trip_flights = []
        
        for flight in self.every_flight_for_each_city:
            outbound_date = dt.datetime.fromtimestamp(flight["route"][0]["dTime"]).date()
            return_date = dt.datetime.fromtimestamp(flight["route"][1]["aTime"]).date()

            total_trip_days = return_date - outbound_date + dt.timedelta(days = 1)

            if total_trip_days >= dt.timedelta(days = 7) and total_trip_days <= dt.timedelta(days = 28):
                new_flight = {}
                
                new_flight["cityFrom"] = f'{flight["cityFrom"]}-{self.starting_city_data["iataCode"]}'
                new_flight["cityTo"] = f'{flight["cityTo"]}-{flight["flyTo"]}'
                new_flight["price"] = flight["price"]
                new_flight["trip_start_date"] = dt.datetime.strftime(outbound_date, "%Y-%m-%d")
                new_flight["trip_end_date"] = dt.datetime.strftime(return_date, "%Y-%m-%d")

                available_total_days_trip_flights.append(new_flight)

        return available_total_days_trip_flights

    def filter_the_lowerprice_trips(self, available_total_days_trip_flights, endpoint_city):

        available_flights = []

        for flight in available_total_days_trip_flights:
            if flight["price"] < endpoint_city["lowestPrice"]:
                available_flights.append(flight)

        return available_flights