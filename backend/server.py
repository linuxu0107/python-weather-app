from flask import Flask, request
from ApiService import ApiService

app = Flask(__name__)


@app.route("/api/v1/weather/<city_name>", methods=['GET'])
async def weather_data(city_name):
    api_service = ApiService()
    data = await api_service.get_data(city_name)
    #api_service = await ApiService()
    #result = api_service.get_data(city_name)
    return data