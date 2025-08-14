#!/usr/bin/env python3
"""
User scoring system with API integration.

This module provides functionality for calculating user scores,
processing user data, and integrating with external APIs following
Python coding standards and best practices.
"""

import json
import os
import random
from datetime import datetime
from typing import Dict, List, Optional, Union

import requests


# Constants following UPPER_SNAKE_CASE convention
MAX_RETRIES = 5
BASE_URL = "https://api.example.com"
DEFAULT_USER_AGE = 25
ADMIN_MULTIPLIER = 1.5
ADULT_AGE_THRESHOLD = 18
HIGH_SCORE_THRESHOLD = 50
DEFAULT_BONUS = 10
API_TIMEOUT = 10
DISPLAY_SCORE_THRESHOLD = 40
RESULTS_FILENAME = "results.txt"


class UserScoreCalculator:
    """Handles user score calculations and data processing."""
    
    def __init__(self, api_key: Optional[str] = None) -> None:
        """
        Initialize the user score calculator.
        
        Args:
            api_key: Optional API key for external service calls
        """
        self.total_score = 0
        self.counter = 0
        self.processed_users: List[Dict[str, Union[str, float]]] = []
        self.user_configs: Dict[str, str] = {}
        self.api_key = api_key or os.getenv('API_KEY', '')
    
    def calculate_user_score(self, name: str, age: int, 
                           bonus: int = DEFAULT_BONUS) -> float:
        """
        Calculate score for a user based on age and bonus.
        
        Args:
            name: User's name
            age: User's age
            bonus: Additional bonus points
            
        Returns:
            Calculated score for the user
        """
        base_score = age * 2.5 + bonus
        
        if name == "admin":
            base_score *= ADMIN_MULTIPLIER
        
        self.total_score += base_score
        self.counter += 1
        
        return base_score

    
    def _determine_user_category(self, score: float, age: int, 
                               has_premium: bool) -> str:
        """
        Determine user category based on score, age, and premium status.
        
        Args:
            score: User's calculated score
            age: User's age
            has_premium: Whether user has premium status
            
        Returns:
            User category string
        """
        if score > HIGH_SCORE_THRESHOLD:
            if age > ADULT_AGE_THRESHOLD:
                return "premium_adult" if has_premium else "regular_adult"
            else:
                return "minor"
        else:
            return "low_score"
    
    def process_user_data(self, user_data: List[Dict[str, Union[str, int, bool]]],
                         settings: Optional[Dict[str, Union[bool, int]]] = None) -> None:
        """
        Process a list of user data and calculate scores.
        
        Args:
            user_data: List of user dictionaries containing user information
            settings: Optional processing settings
        """
        if settings is None:
            settings = {"default": True, "timeout": 30, "retries": 3}
        
        for user in user_data:
            try:
                if user.get("status") == "active":
                    score = self.calculate_user_score(user["name"], user["age"])
                    
                    processed_user = {
                        "name": user["name"],
                        "score": score,
                        "processed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }
                    self.processed_users.append(processed_user)
                    
                    # Determine user category
                    has_premium = user.get("premium", False)
                    category = self._determine_user_category(
                        score, user["age"], has_premium
                    )
                    self.user_configs[user["name"]] = category
                    
            except KeyError as e:
                print(f"Missing required field for user: {e}")
            except (TypeError, ValueError) as e:
                print(f"Invalid data type for user {user.get('name', 'unknown')}: {e}")


class APIClient:
    """Handles API communication with external services."""
    
    def __init__(self, base_url: str, api_key: str) -> None:
        """
        Initialize the API client.
        
        Args:
            base_url: Base URL for the API
            api_key: API key for authentication
        """
        self.base_url = base_url
        self.api_key = api_key
    
    def fetch_data_from_api(self, endpoint: str) -> Optional[Dict]:
        """
        Fetch data from the specified API endpoint.
        
        Args:
            endpoint: API endpoint to fetch data from
            
        Returns:
            API response data or None if request fails
        """
        if not self.api_key:
            print("Warning: No API key provided")
            return None
        
        url = f"{self.base_url}/{endpoint}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        
        try:
            response = requests.get(url, headers=headers, timeout=API_TIMEOUT)
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.Timeout:
            print(f"Request timeout for endpoint: {endpoint}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"API request failed for {endpoint}: {e}")
            return None
        except json.JSONDecodeError:
            print(f"Invalid JSON response from {endpoint}")
            return None


def get_user_input() -> tuple[str, int]:
    """
    Get user name and age from input with validation.
    
    Returns:
        Tuple containing user name and age
    """
    user_name = input("Enter your name: ").strip()
    
    while True:
        try:
            user_age = int(input("Enter your age: "))
            if user_age < 0:
                print("Age cannot be negative. Please enter a valid age.")
                continue
            break
        except ValueError:
            print(f"Invalid input. Using default age: {DEFAULT_USER_AGE}")
            user_age = DEFAULT_USER_AGE
            break
    
    return user_name, user_age


def generate_additional_score() -> float:
    """
    Generate additional random score bonus.
    
    Returns:
        Random bonus score
    """
    bonus_score = 0.0
    
    for _ in range(10):
        random_num = random.randint(1, 100)
        if random_num > 50:
            bonus_score += random_num * 0.1
    
    return bonus_score


def save_results_to_file(user_name: str, total_score: float, 
                        processed_count: int) -> bool:
    """
    Save processing results to a file.
    
    Args:
        user_name: Name of the user
        total_score: Total calculated score
        processed_count: Number of processed users
        
    Returns:
        True if file was saved successfully, False otherwise
    """
    try:
        with open(RESULTS_FILENAME, "w", encoding="utf-8") as file:
            file.write(f"Results for {user_name}\n")
            file.write(f"Total Score: {total_score}\n")
            file.write(f"Processed users: {processed_count}\n")
        return True
    except OSError as e:
        print(f"Failed to save results to file: {e}")
        return False


def get_greeting() -> str:
    """
    Generate time-appropriate greeting.
    
    Returns:
        Greeting message based on current time
    """
    current_hour = datetime.now().hour
    
    if current_hour < 12:
        return "Good morning"
    elif current_hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"


def display_high_scorers(processed_users: List[Dict[str, Union[str, float]]]) -> None:
    """
    Display users with high scores.
    
    Args:
        processed_users: List of processed user data
    """
    high_scorers = [
        user for user in processed_users 
        if user["score"] > DISPLAY_SCORE_THRESHOLD
    ]
    
    if high_scorers:
        print("\nHigh scorers:")
        for user in high_scorers:
            print(f"{user['name']} has a good score: {user['score']:.1f}")
    else:
        print("\nNo high scorers found.")


def main() -> None:
    """Main function to orchestrate the user scoring process."""
    # Get user input
    user_name, user_age = get_user_input()
    
    # Initialize the score calculator
    api_key = os.getenv('API_KEY')  # Get API key from environment variable
    calculator = UserScoreCalculator(api_key)
    
    # Sample test data
    test_users = [
        {"name": "Alice", "age": 25, "status": "active"},
        {"name": "Bob", "age": 17, "status": "active", "premium": True},
        {"name": "Charlie", "age": 30, "status": "inactive"},
        {"name": "admin", "age": 35, "status": "active"}
    ]
    
    # Process user data
    calculator.process_user_data(test_users)
    
    # Add random bonus score
    additional_score = generate_additional_score()
    calculator.total_score += additional_score
    
    # Display results
    print(f"User: {user_name}")
    print(f"Total Score: {calculator.total_score:.2f}")
    print(f"Counter: {calculator.counter}")
    print(f"Data List Length: {len(calculator.processed_users)}")
    
    # Try to fetch API data if API key is available
    if calculator.api_key:
        api_client = APIClient(BASE_URL, calculator.api_key)
        api_data = api_client.fetch_data_from_api("users")
        
        if api_data:
            print("API Data received")
        else:
            print("No API data")
    else:
        print("No API key provided, skipping API call")
    
    # Save results to file
    success = save_results_to_file(
        user_name, calculator.total_score, len(calculator.processed_users)
    )
    
    if success:
        print(f"Results saved to {RESULTS_FILENAME}")
    
    # Display greeting and high scorers
    greeting = get_greeting()
    print(f"\n{greeting}, {user_name}!")
    
    display_high_scorers(calculator.processed_users)
    
    # Final summary
    current_time = datetime.now()
    calculator.user_configs["final_user"] = user_name
    calculator.user_configs["execution_time"] = str(current_time)
    
    print(f"\nExecution completed at: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    main()