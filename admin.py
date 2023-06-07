
# ----------------import required modules---------------------------
import json


# -----------------required data storage ----------------------------
# This is done as a additional work to create the text document containing movie list which
# contains it details as dictionaries
dict1 = [
 {
 "name": "Forrest Gump",
 "year": 1994,
 "duration": 142,
 "genres": ["Drama", "Romance"]
 },
 {
 "name": "Avengers: Endgame",
 "year": 2019,
 "duration": 181,
 "genres": ["Action", "Adventure", "Drama"]
 },
 {
 "name": "Back to the Future",
 "year": 1985,
 "duration": 114,
 "genres": ["Adventure", "Comedy", "Sci-Fi"]
 }
]

string_data = json.dumps(dict1, indent=4)

with open("data.txt", "w") as file1:
    file1.write(string_data)

# -----------------Creating the required functions-------------------------------------------
# This function repeatedly prompts for input until an integer of at least 1 is entered.
# See Point 1 of the "Functions in admin.py" section of the assignment brief.

# This function is build to show an error to the user when they enter another data type,
# for an input which they have to assign an integer value


def input_int(prompt):
    while True:
        try:
            prompt = int(prompt)
        except ValueError:
            prompt = str(prompt)

        else:
            if prompt >= 1:
                return int(prompt)
            break


        if (type(prompt) != type(1)):
            print("Error !!!")
            prompt = str(input("Enter a proper value : "))


# This function repeatedly prompts for input until something other than whitespace is entered.
# See Point 2 of the "Functions in admin.py" section of the assignment brief.

# This function is build to show an error if the user input a white space value.
def input_something(prompt):
    while True:
            prompt = prompt.strip()
            while prompt in ("", " ", None, "\t"):
                print("Error !!!")
                prompt = str(input("Enter a proper value : "))
            else:
                return prompt

# This function opens "data.txt" in write mode and writes data_list to it in JSON format.
# See Point 3 of the "Functions in admin.py" section of the assignment brief.

# This function is build to store the movie details in data.txt


def save_data(data_list):
    string_data3 = json.dumps(data_list, indent=4)
    with open("data.txt", "w") as file3:
        file3.write(string_data3)


# -------------------Main program ------------------------------------------
# printing the welcome massage
print('Welcome to the "Movie Catalogue" Admin Program')

# reading movie details from the data.txt
file2 = open("data.txt", "r")
string_data2 = file2.read()

try:
    data = json.loads(string_data2)
except Exception:
    data = []
except FileNotFoundError:
    data = []
else:
    pass

file2.close()

while True:
    print("Choose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete, [g]enre search or [q]uit.")

    # Creating user choice in to lower case
    user_choice = str(input(">")).lower()

    # Check whether user input is there in the given tuple
    if user_choice in ("a", "l", "s", "v", "d", "q","g", "add", "list", "search", "view", "delete", "quit", "genre search"):
        addition_dict = {"name": "", "year": "", "duration": "", "genre": "[]"}

        if user_choice in ("a", "add"):
            # Add a new movie.
            # See Point 3 of the "Requirements of admin.py" section of the assignment brief.

            # Asking user to add a new movie name.
            movie_name = input_something(str(input("Enter a movie name :")))

            # Asking user to add the released year of the movie.
            release_year = input_int(str(input("Enter release year :")))

            # Check whether the given movie is already exist in the list
            # If it is already exists, print an error and ask user to add a new value
            count = 0
            for index in data:
                if (movie_name == data[count]["name"] and release_year == data[count]["year"]):
                    print("Movie is already exist in the system.")
                    movie_name = input_something(str(input("Enter a movie name :")))
                    release_year = input_int(str(input("Enter release year :")))
                count = count + 1

            addition_dict["name"] = str(movie_name)
            addition_dict["year"] = int(release_year)

            # Ask user to input a value for the movie duration
            movie_duration = input_int(str(input("Enter movie duration in minutes :")))
            addition_dict["duration"] = int(movie_duration)

            # Building up criteria for user to input values for the movie genres.
            addition_list = []
            movie_genre = "1"
            time = 1

            # Creating the exit method for user to exit from entering genre names.
            while movie_genre != "x".title():
                movie_genre = input_something(str(input('Enter movie genre ("x" to end) :')).lower().title())
                if time == 1:
                    pass
                else:
                    # show error massage if the movie already exists
                    count = 0
                    for index in movie_genre:
                        while movie_genre in addition_list:
                            print("Genre already exists !!!")
                            movie_genre = input_something(str(input('Enter movie genre ("x" to end) :')).lower().title())
                        else:
                            pass
                        count = count + 1
                time = time + 1

                # Adding the name of the movie genre if it not equal to x, since it is the exit method., this is done to
                # call the values when the user need to get genre details.
                if movie_genre != "x".title():
                    addition_list.append(movie_genre)
                else:
                    pass
            print("")

            addition_dict["genres"] = list(addition_list)
            data.append(addition_dict)
            addition_list.clear()

            save_data(data_list=data)

        # List the current movies.
        # See Point 4 of the "Requirements of admin.py" section of the assignment brief.

        elif user_choice in ("l", "list"):

            # if there is no movie saved in the list, show a massage to indicate that.
            if len(data) == 0:
                print("No movies saved.")

            # If there are one or more movies saved in the list, show the details of the movie list.
            else:
                print("List of movies :")

                # Building up the criteria to show the list of movies.
                time = 0
                for value in data:
                    index = time + 1
                    print("   " + str(index) + ")", end="")
                    print(data[index - 1]["name"], end="")
                    print("(" + str(data[index - 1]["year"]) + ")")
                    time = time + 1
                print("")

        # Search the current movies.
        # See Point 5 of the "Requirements of admin.py" section of the assignment brief.
        elif user_choice in ("s", "search"):

            while True:
                # Building up the criteria for user to input the search term and get required details.
                status = 0
                search_term = input_something(str(input("Enter a search term :")).lower())
                print("Search results :")

                # If there is no any movies saved, show an error massage.
                if len(data) == 0:
                    print("No movies Saved.")

                # if the list have 1 or movie details building the search method to show the movie details.
                else:
                    time = 0
                    for value in range(len(data)):
                        required_name = data[int(time)]["name"]

                        if search_term in str(required_name).lower():
                            index = time + 1
                            print("   " + str(index) + ")", end="")
                            print(data[index - 1]["name"], end="")
                            print("(" + str(data[index - 1]["year"]) + ")")
                            status = 1
                            break
                        else:
                            pass
                        time = time + 1

                    # Building the status method to show the user if the movie details found or not.
                    if status == 0:
                        print("No results found")
                    else:
                        pass

                if status == 1:
                    break
                else:
                    pass
            print("")

        # View a movie.
        # See Point 6 of the "Requirements of admin.py" section of the assignment brief.

        elif user_choice in ("v", "view"):

            # Building up the criteia to find the movie from its number.
            while True:
                movie_view = input_int(int(input("Movie number to view :")))

                print(" ")

                # if there is no any movie details saved in the list. show the error massage.
                if len(data) == 0:
                    print("No movies Saved.")

                # If the movie number out of range show the required error massage.
                elif movie_view <= 0 or movie_view > len(data):
                    print("Invalid index number.")
                else:
                    count = 0

                    # Building the criteria to display all the details of the viewing movie.
                    for index in range(len(data)):
                        if movie_view == (int(count + 1)):
                            for items in data[count].items():

                                # Displaying the name of the movie.
                                print(data[int(count)]["name"])

                                # Displaying the released year.
                                print("Released :", data[int(count)]["year"])

                                # Displaying the movie duration in minutes.
                                print("Duration in minutes :", data[int(count)]["duration"], "minutes.")

                                # Building the criteria to display the movie duration in hours.
                                hours = int(int(data[int(count)]["duration"]) / 60)
                                minutes = (int(data[int(count)]["duration"]) - (hours * 60))

                                # Display the movie duration in hours.
                                print("Duration in hours :", hours, "hours and", minutes, "minutes.")

                                try:
                                    # Building the criteria to display the genre or genres
                                    # if the dictionary contains more than one genre, display it as genres.
                                    # if the dictionary contains only one genre, display it as genre.

                                    x = list(data[int(count)]["genres"])
                                    if len(x) == 1 or len(x) == 0:
                                        print("Genre :", end="")
                                    else:
                                        print("Genres :", end="")
                                except KeyError:
                                    print(" ")
                                else:
                                    pass

                                # Building up the criteria to print a comma in between genre values.
                                time4 = 0
                                for index in x:
                                    if int(time4) == len(x) - 1:
                                        print(index)

                                    else:
                                        print(index, end=",")
                                    time4 = time4 + 1
                                print("")
                                break
                        else:
                            pass
                        count = count + 1

                given_value = int(movie_view)

                # break the process if there is a miss mach of the type.
                if type(movie_view) == type(1):
                    break
                else:
                    pass
            print("")

        # Delete a movie.
        # See Point 7 of the "Requirements of admin.py" section of the assignment brief.

        elif user_choice in ("d", "delete"):

            # if there is no any movie details in the list show an error.
            if len(data) == 0:
                print("No movies Saved.")
            else:
                # Using exception handling to show errors of the deleting movie.
                try:
                    # Taking the user input of the number of the movie, that they want to delete.
                    movie_delete = input_int(int(input("Movie number to delete : ")))
                    del data[movie_delete - 1]
                except Exception:
                    print("Error deleting the data !!!")
                else:
                    print("Movie deleted")

            # Calling save_data dunction to re-write in the data.txt
            save_data(data_list=data)
            print("")

        # View genre details.
        # Building up the criteria to see the movie details under a certain genre, when genre is selected
        elif user_choice in ("g", "genre"):
            # Taking the user input of the genre type.
            genre_search = str(input(" Enter a search term for genre :")).title()
            count = 0
            status = 0
            for index in data:
                try:
                    # Display the genre details according to the given values.
                    for values in list(data[count]["genres"]):
                        if genre_search == values:
                            index = count + 1
                            print("   " + str(index) + ")", end="")
                            print(data[index - 1]["name"], end="")
                            print("(" + str(data[index - 1]["year"]) + ")")
                            status = 1
                        else:
                            pass
                    count = count + 1
                except KeyError:
                    print("")

            if status == 0:
                print("No results found.")
            else:
                pass
            print(" ")

        # End the program.
        # See Point 8 of the "Requirements of admin.py" section of the assignment brief.
        elif user_choice in ("q", "quit"):
            print("Goodbye!")
            break
    # Print "invalid choice" message.
    # See Point 9 of the "Requirements of admin.py" section of the assignment brief.
    else:
        print("Invalid choice")
        pass

# If you have been paid to write this program, please delete this comment.





















































