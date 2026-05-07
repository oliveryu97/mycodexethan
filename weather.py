#!/usr/bin/env python3
"""Simple weather CLI tool using Open-Meteo free API."""

import sys
import urllib.request
import json
import argparse

def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,weather_code,wind_speed_10m"
    with urllib.request.urlopen(url) as r:
        data = json.loads(r.read())
    
    temp = data["current"]["temperature_2m"]
    code = data["current"]["weather_code"]
    wind = data["current"]["wind_speed_10m"]
    
    codes = {
        0: "Clear", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
        45: "Fog", 48: "Depositing rime fog",
        51: "Drizzle", 53: "Freezing drizzle", 55: "Heavy drizzle",
        61: "Rain", 63: "Freezing rain", 65: "Heavy rain",
        71: "Snow", 73: "Snow grains", 75: "Heavy snow",
        80: "Rain showers", 82: "Violent showers", 95: "Thunderstorm"
    }
    
    condition = codes.get(code, "Unknown")
    return f"{temp}°C, {condition}, Wind: {wind} km/h"

def main():
    parser = argparse.ArgumentParser(description="Simple weather CLI")
    parser.add_argument("--lat", default="40.7128", help="Latitude")
    parser.add_argument("--lon", default="-74.0060", help="Longitude")
    parser.add_argument("--city", default="New York", help="City name")
    args = parser.parse_args()
    
    weather = get_weather(args.lat, args.lon)
    print(f"\n📍 {args.city}")
    print(f"🌤️  {weather}")

if __name__ == "__main__":
    main()
