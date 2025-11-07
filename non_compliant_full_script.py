"""
Simple user scoring script.

This module provides basic user scoring functionality with
file output capabilities.
"""

import json
import random
from datetime import datetime

# Constants
SCORE_MULTIPLIER = 2.5
BASE_BONUS = 7
ADULT_AGE_THRESHOLD = 18
ADMIN_MULTIPLIER = 2
RANDOM_ITERATIONS = 5
RESULTS_FILENAME = 'results.txt'


def calculate_user_score(user_name: str, user_age: int) -> dict:
    """
    Calculate user score based on age and name.

    Args:
        user_name: The user's name
        user_age: The user's age

    Returns:
        Dictionary containing user data and calculated score
    """
    user_data = {
        'name': user_name,
        'score': user_age * SCORE_MULTIPLIER + BASE_BONUS,
        'timestamp': datetime.now().strftime('%d-%m-%Y %H:%M')
    }

    # Apply admin bonus
    if user_name == "admin":
        user_data['score'] *= ADMIN_MULTIPLIER
        print('Admin bonus applied!')

    return user_data


def main() -> None:
    """Main function to execute user scoring workflow."""
    # Get user input
    user_name = input('Enter name: ')

    try:
        user_age = int(input('Enter age: '))
    except ValueError:
        user_age = 0
        print('Invalid age input, using default value: 0')

    # Calculate score
    user_data = calculate_user_score(user_name, user_age)

    # Display results
    print(f'User: {user_name}, Score: {user_data["score"]}')

    # Age category
    if user_age > ADULT_AGE_THRESHOLD:
        print('Category: Adult')
    else:
        print('Category: Minor')

    # Save results
    try:
        with open(RESULTS_FILENAME, 'w', encoding='utf-8') as results_file:
            results_file.write(json.dumps(user_data, indent=2))
        print(f'Results saved to {RESULTS_FILENAME}')
    except OSError as e:
        print(f'Failed to save results: {e}')

    # Generate random numbers
    print('Random numbers:')
    for i in range(RANDOM_ITERATIONS):
        print(f'Random {i+1}: {random.randint(1, 100)}')


if __name__ == "__main__":
    main()
