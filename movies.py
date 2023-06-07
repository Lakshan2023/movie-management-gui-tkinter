# ----------------------------- Import Modules ------------------------------------------------------------------------
# Import the necessary module(s).
from tkinter import *
import tkinter
import tkinter.messagebox
import json
import random
import webbrowser
from operator import itemgetter


# -----------------------------Building up the Gui program------------------------------------------------------------


class ProgramGUI:

    # ------------------------------- Building up the Constructor ----------------------------------------------------------

    def __init__(self):

        try:
            # Calling the data in data.txt
            with open("data.txt", "r") as fo:
                self.data = json.loads(fo.read())
        except FileExistsError:
            print("Missing file")
        except ValueError:
            print("Invalid file")
        else:
            print()

        while True:
            if len(self.data) == 0:
                print()
            else:
                break

        self.main = tkinter.Tk()

        # Mentioning the geometry of the opening file.
        self.main.geometry("580x470")

        # Giving the name of the gui program.
        self.main.title("Movie Catalogue")

        # Giving the background colour to the Gui.
        self.main.config(background="#6ED0D1")

        # Assigned the first button to go to previous page.
        self.first_button = tkinter.Button(self.main, text="Previous", font=('Comic Sans', 20)
                                           , fg="#ECFE7F", bg="black", activeforeground="#FFC300",
                                           activebackground="black", height=1,
                                           width=8,
                                           relief='raised', bd=10, command=self.previous)
        self.first_button.place(x=10, y=300)

        # Assigned the second button to see the statistics tab.
        self.second_button = tkinter.Button(self.main, text="Statistics", font=('Comic Sans', 20)
                                            , fg="#ECFE7F", bg="black", activeforeground="#FFC300",
                                            activebackground="black", height=1,
                                            width=8,
                                            relief='raised', bd=10, command=self.show_statistics)
        self.second_button.place(x=210, y=300)

        # Assigned the third button to go to the next page.
        self.third_button = tkinter.Button(self.main, text="Next", font=('Comic Sans', 20)
                                           , fg="#ECFE7F", bg="black", activeforeground="#FFC300",
                                           activebackground="black", height=1,
                                           width=8,
                                           relief='raised', bd=10, command=self.next)
        self.third_button.place(x=410, y=300)

        # Assigned the first label in position x = 10, y=70 to create the user interface with colored boxes.
        self.label_1 = tkinter.Label(self.main, text="", font=('Arial', 20, 'bold'),
                                     fg='black', bg='#091838', height=2, width=32)
        self.label_1.place(x=10, y=70)

        # Assigned the second label in position x = 10, y=150 to create the user interface with colored boxes.
        self.label_2 = tkinter.Label(self.main, text="", font=('Arial', 20, 'bold'),
                                     fg='#7FFE90', bg='black', height=4, width=32)
        self.label_2.place(x=10, y=150)

        # Assigned the third label in position x = 10, y = 150 to show the box which contains the released value.
        self.label_3 = tkinter.Label(self.main, text="Released:", font=('Arial', 20, 'bold'),
                                     fg='#FFFFFF', bg='black', height=1, width=8)
        self.label_3.place(x=10, y=150)

        # Assigned the fourth label in position x = 10, y = 195 to show the box which contains the Duration value.
        self.label_4 = tkinter.Label(self.main, text="Duration:", font=('Arial', 20, 'bold'),
                                     fg='#FFFFFF', bg='black', height=1, width=8)
        self.label_4.place(x=10, y=195)

        # Assigned the fifth label in position x = 10, y = 240 to show the box which contains the Duration value.
        self.label_5 = tkinter.Label(self.main, text="Genre(s):", font=('Arial', 20, 'bold'),
                                     fg='#FFFFFF', bg='black', height=1, width=8)
        self.label_5.place(x=10, y=240)

        # Assigned the 11th label in position x = 15, y = 380 to show a colored boxx in the position.
        self.label_11 = tkinter.Label(self.main, text="", font=('Arial', 37, 'bold'),
                                      fg='#FFFFFF', bg='#091838', height=1, width=18)
        self.label_11.place(x=15, y=380)

        # Assigned the fourth button to go to the first page.
        self.fourth_button = tkinter.Button(self.main, text="First", font=('Comic Sans', 16)
                                            , fg="#ECFE7F", bg="black", activeforeground="#FFC300",
                                            activebackground="black", height=1,
                                            width=8,
                                            relief='raised', bd=10, command=self.first_movie)
        self.fourth_button.place(x=16, y=380)

        # Assigned the fifth button to go to the last page.
        self.fifth_button = tkinter.Button(self.main, text="Last", font=('Comic Sans', 16)
                                           , fg="#ECFE7F", bg="black", activeforeground="#FFC300",
                                           activebackground="black", height=1,
                                           width=8,
                                           relief='raised', bd=10, command=self.last_movie)
        self.fifth_button.place(x=151, y=380)

        # Assigned the sixth button to go to a random page.
        self.sixth_button = tkinter.Button(self.main, text="Random", font=('Comic Sans', 16)
                                           , fg="#ECFE7F", bg="black", activeforeground="#FFC300",
                                           activebackground="black", height=1,
                                           width=8,
                                           relief='raised', bd=10, command=self.random_movie)
        self.sixth_button.place(x=285, y=380)

        # Assigned the seventh button(IMBd) to go to the imbd website.
        self.seventh_button = tkinter.Button(self.main, text="IMDb", font=('Comic Sans', 16)
                                             , fg="#ECFE7F", bg="black", activeforeground="#FFC300",
                                             activebackground="black", height=1,
                                             width=8,
                                             relief='raised', bd=10, command=self.imbd_webbrowser)
        self.seventh_button.place(x=426, y=380)

        # Criteria used to create the dro-down list.
        self.option_list = ["Name", "Released", "Duration", "Genre"]

        self.value_inside = tkinter.StringVar(self.main)

        # Giving the Heading name to the dro- down list.
        self.value_inside.set("Select an Option")

        # Assigning the drop-down  values.
        self.question_menu = tkinter.OptionMenu(self.main, self.value_inside, *self.option_list)

        # Make Changes of the design in the drop-down list.
        self.question_menu.config(font=("Comic Sans", 10, "bold"), relief="raised", activebackground="#C3EFEA",
                                  bg="#BFFFF9")

        self.question_menu.place(x=400, y=160)

        # Assigned the submit button to submit the selected method.
        submit_button = tkinter.Button(self.main, text='Submit', font=('Comic Sans', 13, 'bold'),
                                       command=self.print_answers, width=6, height=1, bg="#FBFFE1",
                                       activeforeground="#414523", bd=8, activebackground="#DBF676")
        submit_button.place(x=430, y=190)

        # Stating self.currrent movie as one to see the number of the current page.
        self.current_movie = 0

        self.current_movie = self.show_movie()

        tkinter.mainloop()

        # This is the constructor of the class.
        # It is responsible for loading the data from the text file and creating the user interface.
        # See the "Constructor of the GUI Class of movies.py" section of the assignment brief.          

    # show_movie method is used to return the current movie with self.data to the constructor.
    def show_movie(self):
        # This method displays the details of the current movie in the GUI.
        # See Point 1 of the "Methods in the GUI class of movies.py" section of the assignment brief.

        try:
            # Assigned the label to display the current year in a label.
            self.label_6 = tkinter.Label(self.main, text=self.data[self.current_movie]["year"],
                                         font=('Arial', 20, 'bold'),
                                         fg='#FFFFFF', bg='black', height=1, width=5)
            self.label_6.place(x=160, y=150)

            # Assigned the label to display the duration in a label.
            self.label_7 = tkinter.Label(self.main,
                                         text=" {} minutes".format(self.data[self.current_movie]["duration"]),
                                         font=('Arial', 20, 'bold'),
                                         fg='#FFFFFF', bg='black', height=1, width=10)
            self.label_7.place(x=160, y=195)

            # Assigned the genre list to show the genres with comma values
            self.genre_list = []
            self.time = 0
            for index in self.data[self.current_movie]["genres"]:
                if int(self.time) == len(self.data[self.current_movie]["genres"]) - 1:
                    self.genre_list.append(index)

                else:
                    self.genre_list.append(index)
                    self.genre_list.append(",")

                self.time = self.time + 1

            # Assigned the label 8 to display the genres
            self.label_8 = tkinter.Label(self.main, text=self.genre_list,
                                         font=('Arial', 17, 'bold'),
                                         fg='#FFFFFF', bg='black', height=1, width=25, justify=LEFT)
            self.label_8.place(x=145, y=245)

            #  Assigned the label 9 to display the current movie name.
            self.label_9 = tkinter.Label(self.main, text=self.data[self.current_movie]["name"],
                                         font=('Arial', 20, 'bold'),
                                         fg='#FFFFFF', bg='#091838', height=1, width=16)
            self.label_9.place(x=120, y=80)

            # Assigned the label 10 to display the 'Movie currrent movie of length of movie'
            self.label_10 = tkinter.Label(self.main,
                                          text="Movie {0} of {1}".format(self.current_movie + 1, len(self.data)),
                                          font=('Arial', 16, 'bold'),
                                          fg='#FFFFFF', bg='black', height=2, width=42)
            self.label_10.place(x=10, y=12)

        # Used exception handelling to return the current movie.
        except IndexError:
            print()

        else:
            return self.current_movie

    def previous(self):
        # This method is called when the user clicks the "Previous" button.
        # See Point 2 of the "Methods in the GUI class of movies.py" section of the assignment brief.

        if self.current_movie != 0:
            self.current_movie = self.current_movie - 1
            self.show_movie()

        else:
            tkinter.messagebox.showwarning("End of File", "No previous movie.")

    def next(self):
        # This method is called when the user clicks the "Next" button.
        # See Point 3 of the "Methods in the GUI class of movies.py" section of the assignment brief.
        if self.current_movie < len(self.data) - 1:
            self.current_movie = self.current_movie + 1
            self.show_movie()

        else:
            tkinter.messagebox.showwarning("End of File", "No next movie.")

    def show_statistics(self):
        # This method is called when the user clicks the "Statistics" button.
        # See Point 4 of the "Methods in the GUI class of movies.py" section of the assignment brief.

        self.number_of_movies = len(self.data)
        self.min_released_year = 50000
        self.max_released_year = 0
        self.genre_set = set()

        self.total_duration = 0
        # Build up the criteria to find the latest movie released year and the oldest movie released year
        count = 0
        while count < len(self.data):
            if int(self.data[count]["year"]) > self.max_released_year:
                self.max_released_year = int(self.data[count]["year"])
            else:
                print()

            if int(self.data[count]["year"]) < self.min_released_year:
                self.min_released_year = int(self.data[count]["year"])
            else:
                print()

            # build the criteria to find the total duration of the movies.
            count_2 = 0
            while count_2 < len(self.data[count]["genres"]):
                try:
                    self.genre_set.add(self.data[count]["genres"][count_2])
                except Exception:
                    print()
                else:
                    print()
                count_2 = count_2 + 1

            self.total_duration += self.data[count]["duration"]

            count = count + 1

        # Show the latest and the oldest movie released year range.
        self.year_range = "{0} - {1}".format(self.min_released_year, self.max_released_year)

        # Calculate the average movie duration by considering the total duration of movies.
        self.average_duration = self.total_duration / len(self.data)
        self.length_genre = len(self.genre_set)

        # Rounding the average movie duration to its nearest int without considering the ceil and floor methods.
        if (self.average_duration - int(self.average_duration)) > 0.5:
            self.nearest_average_duration = int(self.average_duration) + 1
        else:
            self.nearest_average_duration = int(self.average_duration)

        # Show all of the above calculated details in a massage box called Statistics.
        tkinter.messagebox.showinfo('Statistics', 'Number of movies : {0}\n\nRelease year range : {1}\n\n'
                                                  'Average duration : {2} minutes\n\nNumber of different genres : {3}'.format(
            self.number_of_movies, self.year_range, self.nearest_average_duration, self.length_genre))

    # Built another function to find the first movie and display it.
    def first_movie(self):
        self.current_movie = 0
        self.show_movie()

    # Built another function to find the last movie and display it.
    def last_movie(self):
        self.current_movie = len(self.data) - 1
        self.show_movie()

    # Built another function to find a random movie and display it.
    def random_movie(self):
        self.current_movie = random.randint(0, len(self.data))
        self.show_movie()

    # Used the following function to direct to the IMBd website which contains the current gui movie details.
    def imbd_webbrowser(self):
        try:
            webbrowser.open('https://www.google.com/search?sourceid=navclient&gfns=1&q=imdb%20{0} {1}'.format(
                self.data[self.current_movie]["name"], self.data[self.current_movie]["year"]))

        except IndexError:
            print()
        else:
            print()

    # Used the following function to sort the movie details according to the selected value from the drop down list.
    def print_answers(self):
        # When user select name
        if self.value_inside.get() == self.option_list[0]:
            self.newlist = sorted(self.data, key=itemgetter("name"))
            self.data = self.newlist
            self.show_movie()

        # When user select year
        elif self.value_inside.get() == self.option_list[1]:
            self.newlist = sorted(self.data, key=itemgetter("year"))
            self.data = self.newlist
            self.show_movie()

        # When user select duration
        elif self.value_inside.get() == self.option_list[2]:
            self.newlist = sorted(self.data, key=itemgetter("duration"))
            self.data = self.newlist
            self.show_movie()

        # When user select genres
        elif self.value_inside.get() == self.option_list[3]:
            self.newlist = sorted(self.data, key=itemgetter("genres"))
            self.data = self.newlist
            self.show_movie()

        else:
            print()


# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()

# If you have been paid to write this program, please delete this comment.
