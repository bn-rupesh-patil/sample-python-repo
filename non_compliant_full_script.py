"""
User scoring system.

This module provides basic functionality for calculating user scores,
applying admin bonuses, determining age categories, and storing results
to a file following Python coding standards.
"""

import json
import random
from datetime import datetime


# Constants following UPPER_SNAKE_CASE convention
ADULT_AGE_THRESHOLD = 18
BASE_SCORE_MULTIPLIER = 2.5
BASE_BONUS = 7
ADMIN_MULTIPLIER = 2
RESULTS_FILENAME = 'results.txt'
RANDOM_ITERATIONS = 5
RANDOM_MIN = 1
RANDOM_MAX = 100


def get_user_input() -> tuple[str, int]:
    """
    Get user name and age from console input.
    
    Returns:
        Tuple containing user name (str) and age (int)
        
    Note:
        If age input is invalid, defaults to 0
    """
    user_name = input('name:')
    user_age_input = input('age:')
    
    try:
        user_age = int(user_age_input)
    except ValueError:
        user_age = 0
    
    return user_name, user_age


def calculate_user_score(user_age: int, is_admin: bool = False) -> float:
    """
    Calculate user score based on age and admin status.
    
    Args:
        user_age: User's age in years
        is_admin: Whether the user has admin privileges
        
    Returns:
        Calculated score as a float
    """
    score = user_age * BASE_SCORE_MULTIPLIER + BASE_BONUS
    
    if is_admin:
        score *= ADMIN_MULTIPLIER
    
    return score


def determine_age_category(user_age: int) -> str:
    """
    Determine if user is an adult or minor based on age.
    
    Args:
        user_age: User's age in years
        
    Returns:
        String indicating 'adult' or 'minor'
    """
    if user_age > ADULT_AGE_THRESHOLD:
        return 'adult'
    else:
        return 'minor'


def save_results_to_file(user_data: dict, filename: str) -> bool:
    """
    Save user data dictionary to a file.
    
    Args:
        user_data: Dictionary containing user information
        filename: Path to the output file
        
    Returns:
        True if file was saved successfully, False otherwise
    """
    try:
        with open(filename, 'w', encoding='utf-8') as results_file:
            results_file.write(str(user_data))
        return True
    except OSError as e:
        print(f"Error saving results to file: {e}")
        return False


def generate_random_numbers(iterations: int) -> None:
    """
    Generate and print random numbers.
    
    Args:
        iterations: Number of random numbers to generate
    """
    for _ in range(iterations):
        random_number = random.randint(RANDOM_MIN, RANDOM_MAX)
        print('rand:', random_number)


def main() -> None:
    """
    Main function to calculate user scores.
    
    Prompts user for name and age, calculates a score with optional
    admin bonus, determines age category, saves results to a file,
    and generates random numbers.
    """
    # Get user input
    user_name, user_age = get_user_input()
    
    # Check if user is admin
    is_admin = user_name == "admin"
    
    # Calculate score
    user_score = calculate_user_score(user_age, is_admin)
    
    # Prepare user data
    user_data = {
        'name': user_name,
        'score': user_score,
        'timestamp': datetime.now().strftime('%d-%m-%Y %H:%M')
    }
    
    # Display results
    print('user:', user_name, 'score:', user_score)
    
    # Determine and display age category
    age_category = determine_age_category(user_age)
    print(age_category)
    
    # Display admin bonus message if applicable
    if is_admin:
        print('admin bonus!')
    
    # Save results to file
    save_results_to_file(user_data, RESULTS_FILENAME)
    
    # Generate random numbers
    generate_random_numbers(RANDOM_ITERATIONS)


if __name__ == "__main__":
    main()
