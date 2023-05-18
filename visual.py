"""
This module is responsible for visualising the data using Matplotlib.
"""

"""
Task 22 - 24: Write suitable functions to visualise the data as follows:

- Display a pie chart showing the total number of positive and negative reviews for a specified hotel.
- Display the number of reviews per the nationality of a reviewer. This should by ordered by the number of reviews, highest first, and should show the top 15 + “Other” nationalities.
- Display a suitable animated visualisation to show how the number of positive reviews, negative reviews and the average rating change over time.

Each function should visualise the data using Matplotlib.
"""

# TODO: Your code here

import matplotlib.pyplot as plt
import matplotlib.animation as animation

def display_review_sentiment_pie_chart(hotel_name, positive_reviews_count, negative_reviews_count):
    """
    Display a pie chart showing the total number of positive and negative reviews for a specified hotel.

    :param hotel_name: The name of the hotel
    :param positive_reviews_count: The total number of positive reviews
    :param negative_reviews_count: The total number of negative reviews
    :return: Does not return anything
    """
    labels = ['Positive Reviews', 'Negative Reviews']
    sizes = [positive_reviews_count, negative_reviews_count]
    colors = ['#5cb85c', '#d9534f']  # Green for positive reviews, Red for negative reviews

    plt.figure(figsize=(6, 6))  # Set the size of the pie chart
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.title(f'Review Sentiment for Hotel {hotel_name}')

    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.show()


def display_reviews_by_nationality_bar_chart(nationalities, review_counts):
    """
    Display a bar chart showing the number of reviews per nationality of a reviewer.

    :param nationalities: A list of nationalities
    :param review_counts: A list of review counts corresponding to each nationality
    :return: Does not return anything
    """
    # Sort the nationalities and review counts based on the review counts in descending order
    sorted_data = sorted(zip(nationalities, review_counts), key=lambda x: x[1], reverse=True)
    sorted_nationalities, sorted_review_counts = zip(*sorted_data)

    # Select the top 15 nationalities and combine the rest into "Other" category
    top_nationalities = sorted_nationalities[:15]
    top_review_counts = sorted_review_counts[:15]
    other_reviews_count = sum(sorted_review_counts[15:])

    # Add "Other" category to the top nationalities and review counts
    top_nationalities = list(top_nationalities) + ["Other"]
    top_review_counts = list(top_review_counts) + [other_reviews_count]

    # Create a bar chart
    plt.figure(figsize=(10, 6))  # Set the size of the bar chart
    plt.barh(range(len(top_nationalities)), top_review_counts, align='center')
    plt.yticks(range(len(top_nationalities)), top_nationalities)
    plt.xlabel('Number of Reviews')
    plt.ylabel('Nationality')
    plt.title('Number of Reviews by Nationality')

    plt.show()



def animate_reviews_over_time(dates, positive_counts, negative_counts, average_ratings):
    """
    Display an animated visualization showing how the number of positive reviews, negative reviews,
    and the average rating change over time.

    :param dates: A list of dates
    :param positive_counts: A list of positive review counts corresponding to each date
    :param negative_counts: A list of negative review counts corresponding to each date
    :param average_ratings: A list of average ratings corresponding to each date
    :return: Does not return anything
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    # Initialize empty plots for positive reviews, negative reviews, and average ratings
    positive_plot, = ax.plot([], [], 'g-', label='Positive Reviews')
    negative_plot, = ax.plot([], [], 'r-', label='Negative Reviews')
    average_rating_plot, = ax.plot([], [], 'b-', label='Average Rating')

    # Set up the axis labels, title, and legend
    ax.set_xlabel('Date')
    ax.set_ylabel('Count / Rating')
    ax.set_title('Reviews Over Time')
    ax.legend()

    def animate(frame):
        # Update the data for positive reviews, negative reviews, and average ratings
        positive_plot.set_data(dates[:frame+1], positive_counts[:frame+1])
        negative_plot.set_data(dates[:frame+1], negative_counts[:frame+1])
        average_rating_plot.set_data(dates[:frame+1], average_ratings[:frame+1])

        # Set the x-axis limits based on the current frame
        ax.set_xlim(dates[0], dates[frame])

    # Create the animation
    anim = animation.FuncAnimation(fig, animate, frames=len(dates), interval=500, blit=False)

    plt.show()


