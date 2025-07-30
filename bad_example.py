#!/usr/bin/env python3
import os
import sys
import json
import math
import random
import time
from datetime import datetime
import requests

# Global variables everywhere - BAD PRACTICE!
userName = ""
user_age = 0
TOTAL_SCORE = 0
data_List = []
config_dict = {}
temp_var = None
counter = 1
MAX_RETRIES = 5
api_key = "sk-1234567890abcdef"  # Hardcoded API key - VERY BAD!
BASE_URL = "https://api.example.com"

def Calculate_user_score(name, Age, bonus=10):
    global TOTAL_SCORE, counter
    # Inconsistent naming and no type hints
    temp_score = Age * 2.5 + bonus
    if name == "admin":
        temp_score = temp_score * 1.5  # Magic number
    TOTAL_SCORE += temp_score
    counter += 1
    return temp_score

# Mixed indentation and very long line that violates PEP 8 guidelines by being way too long for readability
def processUserData(userData, settings={"default": True, "timeout": 30, "retries": 3}):
  global data_List, config_dict, temp_var
  # No error handling, mixed indentation
  for user in userData:
        if user["status"] == "active":
            score = Calculate_user_score(user["name"], user["age"])
            data_List.append({"name": user["name"], "score": score, "processed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
            # Nested logic without proper structure
            if score > 50:
                if user["age"] > 18:
                    if "premium" in user:
                        temp_var = "premium_adult"
                    else:
                        temp_var = "regular_adult"
                else:
                    temp_var = "minor"
            else:
                temp_var = "low_score"
        config_dict[user["name"]] = temp_var

def fetchDataFromAPI(endpoint):
    # No error handling, global variable usage
    global temp_var
    url = BASE_URL + "/" + endpoint + "?key=" + api_key
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            print("Error:", response.status_code)  # Poor error handling
            return None
    except:
        print("Something went wrong")  # Bare except clause
        return {}

# Main logic scattered without proper function structure
userName = input("Enter your name: ")
try:
    user_age = int(input("Enter your age: "))
except:
    user_age = 25  # Default fallback

# Hardcoded test data
test_users = [
    {"name": "Alice", "age": 25, "status": "active"},
    {"name": "Bob", "age": 17, "status": "active", "premium": True},
    {"name": "Charlie", "age": 30, "status": "inactive"},
    {"name": "admin", "age": 35, "status": "active"}
]

# Process data
processUserData(test_users)

# More global operations
for i in range(10):
    random_num = random.randint(1, 100)
    if random_num > 50:
        TOTAL_SCORE += random_num * 0.1

# Print results without proper formatting
print("User:", userName)
print("Total Score:", TOTAL_SCORE)
print("Counter:", counter)
print("Data List Length:", len(data_List))

# Try to fetch some API data (will likely fail)
api_data = fetchDataFromAPI("users")
if api_data:
    print("API Data received")
else:
    print("No API data")

# File operations without proper resource management
try:
    with open("results.txt", "w") as f:
        f.write(f"Results for {userName}\n")
        f.write(f"Total Score: {TOTAL_SCORE}\n")
        f.write(f"Processed users: {len(data_List)}\n")
except:
    pass  # Silent failure

# More scattered logic
current_time = datetime.now()
if current_time.hour > 12:
    greeting = "Good afternoon"
elif current_time.hour > 18:
    greeting = "Good evening"
else:
    greeting = "Good morning"

print(f"{greeting}, {userName}!")

# Unnecessary loop
for item in data_List:
    if item["score"] > 40:
        print(f"{item['name']} has a good score: {item['score']}")

# More global variable manipulation
temp_var = "final_state"
config_dict["final_user"] = userName
config_dict["execution_time"] = str(current_time)

# End of script - no proper cleanup or structure