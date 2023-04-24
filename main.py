import requests
import time

# Set up the API endpoint and parameters
api_key = "YOUR_API_KEY_HERE"
username = "owl2050"
profile = "Coconut"

while True:
    api_url = f"https://api.hypixel.net/skyblock/profiles?key={api_key}&name=owl2050"
    response = requests.get(api_url)

    # Parse the API response to find the profile ID for the Coconut profile
    data = response.json()
    if data["success"]:
        profiles = data["profiles"]
        profile_id = None
        for p in profiles:
            if p["cute_name"].lower() == profile.lower():
                profile_id = p["profile_id"]
                break

        # If we found the profile ID, get the farming data for melons
        if profile_id:
            api_url = f"https://api.hypixel.net/skyblock/profile?key={api_key}&profile=Coconut"
            response = requests.get(api_url)
            data = response.json()
            if data["success"]:
                farming_data = data["profile"]["members"][username]["stats"]["farming"]
                farming_xp_per_hour = farming_data["experience"] / farming_data["playtime_minutes"] * 60
                melon_count = farming_data["collections"].get("MELON", {}).get("unlocked_tiers", 0) * 64
                print(f"Melon farming experience points per hour: {farming_xp_per_hour:.2f}")
                print(f"Current melon count: {melon_count}")
            else:
                print("Failed to retrieve skyblock profile data.")
        else:
            print(f"Could not find profile with name '{profile}'.")
    else:
        print("Failed to retrieve skyblock profiles data.")

    # Sleep for 60 seconds before updating again
    time.sleep(60)
