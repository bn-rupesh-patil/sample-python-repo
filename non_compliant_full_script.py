"""
User scoring system with basic input processing.

This module calculates user scores based on age, applies bonuses for admin users,
and saves results to a file. It demonstrates proper Python coding standards
including naming conventions, documentation, and error handling.
"""

import json
import random
from datetime import datetime

# Constants following UPPER_SNAKE_CASE convention
SCORE_MULTIPLIER = 2.5
BASE_BONUS = 7
ADMIN_MULTIPLIER = 2
ADULT_AGE_THRESHOLD = 18
RANDOM_SAMPLE_SIZE = 5
RANDOM_MIN_VALUE = 1
RANDOM_MAX_VALUE = 100
RESULTS_FILENAME = 'results.txt'


def get_user_input():
    """
    Get user name and age from input.
    
    Returns:
        tuple: A tuple containing user_name (str) and user_age (int)
    """
    user_name = input('Enter your name: ')
    user_age_input = input('Enter your age: ')
    
    try:
        user_age = int(user_age_input)
    except ValueError:
        print("Invalid age input. Using default value: 0")
        user_age = 0
    
    return user_name, user_age


def calculate_score(age, is_admin=False):
    """
    Calculate user score based on age and admin status.
    
    Args:
        age (int): User's age
        is_admin (bool): Whether user has admin privileges
        
    Returns:
        float: Calculated score
    """
    score = age * SCORE_MULTIPLIER + BASE_BONUS
    
    if is_admin:
        score *= ADMIN_MULTIPLIER
    
    return score


def determine_age_category(age):
    """
    Determine if user is an adult or minor based on age.
    
    Args:
        age (int): User's age
        
    Returns:
        str: Age category ('adult' or 'minor')
    """
    if age > ADULT_AGE_THRESHOLD:
        return 'adult'
    else:
        return 'minor'


def save_user_data(user_data):
    """
    Save user data to a file.
    
    Args:
        user_data (dict): Dictionary containing user information
        
    Returns:
        bool: True if save was successful, False otherwise
    """
    try:
        with open(RESULTS_FILENAME, 'w', encoding='utf-8') as result_file:
            result_file.write(str(user_data))
        return True
    except OSError as error:
        print(f"Error saving file: {error}")
        return False


def generate_random_numbers():
    """
    Generate a list of random numbers.
    
    Returns:
        list: List of random integers
    """
    random_numbers = [
        random.randint(RANDOM_MIN_VALUE, RANDOM_MAX_VALUE)
        for _ in range(RANDOM_SAMPLE_SIZE)
    ]
    return random_numbers


def main():
    """Main function to process user input and calculate scores."""
    # Get user input
    user_name, user_age = get_user_input()
    
    # Check if user is admin
    is_admin = user_name == "admin"
    
    # Calculate score
    user_score = calculate_score(user_age, is_admin)
    
    # Create user data dictionary
    user_data = {
        'name': user_name,
        'score': user_score,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M')
    }
    
    # Display results
    print(f'User: {user_name}, Score: {user_score}')
    
    # Determine and display age category
    age_category = determine_age_category(user_age)
    print(f'Age category: {age_category}')
    
    # Display admin bonus message
    if is_admin:
        print('Admin bonus applied!')
    
    # Save user data to file
    save_success = save_user_data(user_data)
    if save_success:
        print(f'Results saved to {RESULTS_FILENAME}')
    
    # Generate and display random numbers
    random_numbers = generate_random_numbers()
    for number in random_numbers:
        print(f'Random number: {number}')


if __name__ == "__main__":
    main()
