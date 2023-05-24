"""
This module is responsible for processing the data.  Each function in this module will take a list of reviews,
process it and return the desired result.
"""

"""
Task 16 - 20: Write suitable functions to process the data.

Each of the functions below should follow the pattern:
- Take a list of reviews (where each review is a list of data values) as a parameter.
- Process the list of reviews appropriately.  You may use the module 'tui' to retrieve any additional information 
required from the user to complete the processing.
- Return a suitable result

The required functions are as follows:
- Retrieve the total number of reviews that have been loaded.
- Retrieve the reviews for a hotel where the hotel name is specified by the user.
- Retrieve the reviews for the dates specified by the user.
- Retrieve all the reviews grouped by the reviewer’s nationality.
- Retrieve a summary of all the reviews. This should include the following information for each date in ascending order:
    - the total number of negative reviews on that date
    - the total number of positive reviews on that date
    - the average rating on that date
"""

# TODO: Your code here


from typing import List
from tui import hotel_name, review_dates
from main import read_csv
import csv

filename = 'data/hotel_reviews.csv'
reviews_data = []

def get_total_reviews(reviews: List[List[str]]) -> int:
    """
    Task 16: Retrieve the total number of reviews that have been loaded.

    :param reviews: A list of reviews
    :return: The total number of reviews
    """
    read_csv()
    total_reviews_index = read_csv.header.index('Total_Reviews_By_Reviewer')
    total_reviews_sum = 0

    # Iterate over each row in the CSV file
    for i, row in enumerate(read_csv.csv_reader):
        # Add the value from the "Total_Reviews_By_Reviewer" column to the sum
        total_reviews_sum += int(row[total_reviews_index])

        # Append the entire row to the reviews_data list
        reviews_data.append(row)

        # Print the total sum of the "Total_Reviews_By_Reviewer" column
        print("Total reviews:", total_reviews_sum)

    return len(reviews)


def get_reviews_by_hotel(reviews: List[List[str]]) -> List[List[str]]:
    """
    Task 17: Retrieve the reviews for a hotel where the hotel name is specified by the user.

    :param reviews: A list of reviews
    :return: The reviews for the specified hotel
    """
    hotel_name = hotel_name()
    return [review for review in reviews if review[1] == hotel_name]


def get_reviews_by_dates(reviews: List[List[str]]) -> List[List[str]]:
    """
    Task 18: Retrieve the reviews for the dates specified by the user.

    :param reviews: A list of reviews
    :return: The reviews for the specified dates
    """
    review_dates = review_dates()
    return [review for review in reviews if review[0] in review_dates]


def group_reviews_by_nationality(reviews: List[List[str]]) -> dict:
    """
    Task 19: Retrieve all the reviews grouped by the reviewer's nationality.

    :param reviews: A list of reviews
    :return: A dictionary where the keys are nationalities and the values are lists of reviews for each nationality
    """
    grouped_reviews = {}
    for review in reviews:
        nationality = review[2]
        if nationality in grouped_reviews:
            grouped_reviews[nationality].append(review)
        else:
            grouped_reviews[nationality] = [review]
    return grouped_reviews


def summarize_reviews(reviews: List[List[str]]) -> List[dict]:
    """
    Task 20: Retrieve a summary of all the reviews.

    :param reviews: A list of reviews
    :return: A list of dictionaries containing the summary information for each date
    """
    summary = []
    dates = set(review[0] for review in reviews)
    for date in sorted(dates):
        positive_reviews = 0
        negative_reviews = 0
        total_rating = 0
        num_reviews = 0
        for review in reviews:
            if review[0] == date:
                rating = float(review[5])
                total_rating += rating
                num_reviews += 1
                if rating >= 3.0:
                    positive_reviews += 1
                else:
                    negative_reviews += 1
        average_rating = total_rating / num_reviews if num_reviews > 0 else 0
        summary.append({
            'date': date,
            'positive_reviews': positive_reviews,
            'negative_reviews': negative_reviews,
            'average_rating': average_rating
        })
    return summary
