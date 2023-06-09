"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done using the appropriate functions in the module 'tui'
        any processing should be done using the appropriate functions in the module 'process'
        any visualisation should be done using the appropriate functions in the module 'visual'
"""

# Task 11: Import required modules and create an empty list named 'reviews_data'.
# This will be used to store the data read from the source data file.
# TODO: Your code here
import tui
import csv


filename = 'data/hotel_reviews.csv'
reviews_data = []

def read_csv():
       # Open the CSV file and read its contents
    with open(filename, 'r', newline='') as file:
            csv_reader = csv.reader(file)

    try:
        with open(filename, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader, None)

                # Iterate over each row in the CSV file
        for i, row in enumerate(csv_reader):
                    reviews_data.append(row)


    except FileNotFoundError:
        print("Error: File not found.")

    except Exception as e:
        print("Error: Failed to load data from file.")
        print(f"Exception: {str(e)}")


def run():
    # Task 12: Call the function welcome of the module 'tui'.
    # This will display our welcome message when the program is executed.
    # TODO: Your code here
    tui.welcome()

    # Task 13: Load the data.
    # - Use the appropriate function in the module 'tui' to display a message to indicate that the data loading
    # operation has started.
    # - Load the data. Each line in the file should represent a review in the list 'reviews_data'.
    # You should appropriately handle the case where the file cannot be found or loaded.
    # - Use the appropriate functions in the module 'tui' to display a message to indicate how many reviews have
    # been loaded and that the data loading operation has completed.

    # TODO: Your code here

    filename = 'data/hotel_reviews.csv'
    reviews_data = []

    def read_csv():
        # Open the CSV file and read its contents
        with open(filename, 'r', newline='') as file:
            csv_reader = csv.reader(file)

        tui.progress("loading", 0)

        try:
            with open(filename, 'r', newline='') as file:
                csv_reader = csv.reader(file)

                # Read the header row
                header = next(csv_reader, None)

                # Iterate over each row in the CSV file
                for i, row in enumerate(csv_reader):
                    reviews_data.append(row)
                    # Calculate the progress percentage
                    progress = (i + 1) / 500 * 100
                    # Update progress message
                    tui.progress("Data Loading", int(progress))

        except FileNotFoundError:
            print("Error: File not found.")

        except Exception as e:
            print("Error: Failed to load data from file.")
            print(f"Exception: {str(e)}")

    while True:
        # Task 14: Using the appropriate function in the module 'tui', display the main menu
        # Assign the value returned from calling the function to a suitable local variable
        # TODO: Your code here
        main_menu_choice = tui.main_menu()
        # print(main_menu_choice)
        choice = int(main_menu_choice)

        # Task 15: Check if the user selected the option for processing data.  If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has started.
        # - Process the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has completed.

        if choice == 1:
            tui.progress("Stared", 0)
            print("You have choose 1")
            read_csv()
            tui.sub_menu(choice)
            return choice

        elif choice == 2:
            tui.progress("Stared", 0)
            print("You have choose 2")
            read_csv()
            tui.sub_menu(choice)
            return choice

        elif choice == 3:
            tui.progress("Stared", 0)
            print("You have choose 3")
            read_csv()
            tui.sub_menu(choice)
            return choice

        elif choice == 4:
            tui.progress("Stared", 0)
            print("You have choose 4")
            read_csv()
            tui.sub_menu(choice)
            return choice

        # To process the data, do the following:
        # - Use the appropriate function in the module 'tui' to display a sub-menu of options for processing the data
        # (menu variant 1).
        # - Check what option has been selected
        #
        #   - If the user selected the option to retrieve reviews by hotel name then
        #       - Use the appropriate function in the module 'tui' to indicate that the review retrieval process
        #       has started.
        #       - Use the appropriate function in the module 'process' to retrieve the review and then appropriately
        #       display it.
        #       - Use the appropriate function in the module 'tui' to indicate that the review retrieval process has
        #       completed.
        #
        #   - If the user selected the option to retrieve reviews by review dates then
        #       - Use the appropriate function in the module 'tui' to indicate that the reviews retrieval
        #       process has started.
        #       - Use the appropriate function in the module 'process' to retrieve the reviews
        #       - Use the appropriate function in the module 'tui' to display the retrieved reviews.
        #       - Use the appropriate function in the module 'tui' to indicate that the reviews retrieval
        #       process has completed.
        #
        #   - If the user selected the option to group reviews by nationality then
        #       - Use the appropriate function in the module 'tui' to indicate that the grouping
        #       process has started.
        #       - Use the appropriate function in the module 'process' to group the reviews
        #       - Use the appropriate function in the module 'tui' to display the groupings.
        #       - If required, you may add a suitable function to the module 'tui' to display the groupings
        #       - Use the appropriate function in the module 'tui' to indicate that the grouping
        #       process has completed.
        #
        #   - If the user selected the option to summarise the reviews then
        #       - Use the appropriate function in the module 'tui' to indicate that the summary
        #       process has started.
        #       - Use the appropriate function in the module 'process' to summarise the reviews.
        #       - Add a suitable function to the module 'tui' to display the summary
        #       - Use your function in the module 'tui' to display the summary
        #       - Use the appropriate function in the module 'tui' to indicate that the summary
        #       process has completed.
        # TODO: Your code here

        # Task 21: Check if the user selected the option for visualising data.
        # If so, then do the following:
        # - Use the appropriate function in the module 'tui' to indicate that the data visualisation operation
        # has started.
        # - Visualise the data by doing the following:
        #   - call the appropriate function in the module 'tui' to determine what visualisation is to be done.
        #   - call the appropriate function in the module 'visual' to display the visual
        # - Use the appropriate function in the module 'tui' to display a message to indicate that the
        # data visualisation operation has completed.
        # TODO: Your code here

        # Task 25: Check if the user selected the option for exporting reviews.  If so, then do the following:
        # - Use the appropriate function in the module 'tui' to retrieve what reviews are to be exported.
        # - Check what option has been selected
        #
        # - Use the appropriate function in the module 'tui' to indicate that the export operation has started.
        # - Export the reviews (see below)
        # - Use the appropriate function in the module 'tui' to indicate that the export operation has completed.
        #
        # To export the reviews, you should demonstrate the application of OOP principles including the concepts of
        # abstraction and inheritance.  You should create suitable classes with appropriate methods.
        # You should use these to write the reviews (either all or only those for a specific country/region) to a JSON file.
        # TODO: Your code here

        # Task 26: Check if the user selected the option for exiting the program.
        # If so, then break out of the loop
        # TODO: Your code here

        # Task 27: If the user selected an invalid option then use the appropriate function of the
        # module tui to display an error message
        # TODO: Your code here

        pass  # can remove


if __name__ == "__main__":
    run()
