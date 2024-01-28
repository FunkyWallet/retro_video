"""
**NOTE: the breezypythongui.py file must be in the same directory as this file for proper functionality
Created by: Ignacio Lopez on Jan 26 2024

This application simulates a retro style video rental platform with weekly rotating movies. Users can play a trailer for the movie before renting
The application will also calculate the total price of the rental based on the user choice
"""
# Import statements.
from breezypythongui import EasyFrame
from tkinter.font import Font
from tkinter import PhotoImage, Canvas
import webbrowser
# Class header
class VideoStore(EasyFrame):
    # Constructor method.
    def __init__(self):
    # Call EasyFrame class constructor
        EasyFrame.__init__(self, title="Long Island Retro Films", width=850, height=625, resizable=False, background="salmon")
    # Add Title label
        self.addLabel(text="This week's rentals;", row=0, column=0, columnspan=5, sticky="SEWN", background="salmon", font=Font(family="Courier", size=28))
    # Define image paths and store PhotoImage objects
        self.platoon_image = PhotoImage(file="platoon.png")
        self.shop_image = PhotoImage(file="shop.png")
        self.amigos_image = PhotoImage(file="amigos.png")
        self.clint_image = PhotoImage(file="clint.png")
        self.aliens_image = PhotoImage(file="aliens.png")
    # Add movie labels with images
        self.add_movie_label(text="Platoon", image=self.platoon_image, row=2, column=0)
        self.add_movie_label(text="Little Shop of Horrors", image=self.shop_image, row=2, column=1)
        self.add_movie_label(text="Three Amigos", image=self.amigos_image, row=2, column=2)
        self.add_movie_label(text="Heartbreak Ridge", image=self.clint_image, row=2, column=3)
        self.add_movie_label(text="Aliens", image=self.aliens_image, row=2, column=4)
    # Initialize total price variable
        self.total_price=0
    # Add Label for order total
        self.outputLabel = self.addLabel(text = "", row = 7, column = 0, sticky = "SEWN", columnspan = 5, background = "salmon", foreground = "dark slate gray", font = Font(family="Courier", size = 20))
    # Add checkboxes under each movie label
        self.betamaxP = self.addCheckbutton(text="Betamax", row=3, column=0, sticky="S")
        self.vhsP = self.addCheckbutton(text="VHS", row=4, column=0, sticky="N")
        self.betamaxS = self.addCheckbutton(text="Betamax", row=3, column=1, sticky="S")
        self.vhsS = self.addCheckbutton(text="VHS", row=4, column=1, sticky="N")
        self.betamaxA = self.addCheckbutton(text="Betamax", row=3, column=2, sticky="S")
        self.vhsA = self.addCheckbutton(text="VHS", row=4, column=2, sticky="N")
        self.betamaxC = self.addCheckbutton(text="Betamax", row=3, column=3, sticky="S")
        self.vhsC = self.addCheckbutton(text="VHS", row=4, column=3, sticky="N")
        self.betamaxAl = self.addCheckbutton(text="Betamax", row=3, column=4, sticky="S")
        self.vhsAl = self.addCheckbutton(text="VHS", row=4, column=4, sticky="N")
    # Change color of checkboxes
        checkboxes = [self.betamaxP, self.vhsP, self.betamaxS, self.vhsS, self.betamaxA, self.vhsA, self.betamaxC, self.vhsC, self.betamaxAl, self.vhsAl]
        for checkbox in checkboxes:
            checkbox["background"] = "salmon"
            checkbox["foreground"] = "black"
    # Add Trailer buttons
        self.trailerP = self.addButton(text="Play Trailer", row= 5, column= 0, command=lambda: self.playTrailer("Platoon"))
        self.trailerS = self.addButton(text="Play Trailer", row= 5, column= 1, command=lambda: self.playTrailer("Shop"))
        self.trailerA = self.addButton(text="Play Trailer", row= 5, column= 2, command=lambda: self.playTrailer("Amigos"))
        self.trailerC = self.addButton(text="Play Trailer", row= 5, column= 3, command=lambda: self.playTrailer("Clint"))
        self.trailerAl = self.addButton(text="Play Trailer", row= 5, column= 4, command=lambda: self.playTrailer("Aliens"))
    # Change color of Play buttons
        playButtons = [self.trailerP, self.trailerS, self.trailerA, self.trailerC, self.trailerAl]
        for button in playButtons:
            button["background"] = "salmon"
            button["foreground"] = "black"
    # Add Order Total button
        self.total_button = self.addButton(text="Rental total", row=6, column=0, columnspan=6, command=self.totalButton)
        self.total_button["bg"] = "black"
        self.total_button["fg"] = "salmon"
        self.total_button["width"] = 18
        self.total_button["height"] = 2
# Method to add movie label with image. Not supported with breezypythongui so we make our own.
    def add_movie_label(self, text, image, row, column):
    # Create canvas for image
        canvas = Canvas(self, width=image.width(), height=image.height(), bg="salmon", highlightthickness=0)
        canvas.create_image(0, 0, anchor="nw", image=image)
        canvas.grid(row=row, column=column, padx=5, pady=5)
        self.addLabel(text=text, row=row+1, column=column, foreground="dark slate gray", background="salmon", sticky="NEW", font=Font(size=16, weight="bold"))
    # Method to play trailers
    def playTrailer(self, movie_title):
        trailer_urls = {
            "Platoon": "https://www.youtube.com/watch?v=R8weLPF4qBQ",
            "Shop": "https://www.youtube.com/watch?v=QqFZuR6UzjA",
            "Amigos": "https://www.youtube.com/watch?v=g9OAjqs6dOo",
            "Clint": "https://www.youtube.com/watch?v=ZOo4ir1MtoI",
            "Aliens": "https://www.youtube.com/watch?v=bTCaVjQ8nU4"
        }
        trailer_url = trailer_urls.get(movie_title)
        if trailer_url:
            webbrowser.open(trailer_url)
        else:
            print("Trailer not available.")
# Definition of Total()
    def totalButton(self):
    # Make sure a movie is selected
        if (not self.betamaxP.isChecked() and not self.vhsP.isChecked() and
                not self.betamaxS.isChecked() and not self.vhsS.isChecked() and
                not self.betamaxA.isChecked() and not self.vhsA.isChecked() and
                not self.betamaxC.isChecked() and not self.vhsC.isChecked() and
                not self.betamaxAl.isChecked() and not self.vhsAl.isChecked()):
            self.outputLabel["text"] = "Please select a movie to rent!"
            return
        self.total_price = 0
        if self.betamaxP.isChecked():
            self.total_price += 2
        if self.vhsP.isChecked():
            self.total_price += 3.5
        if self.betamaxS.isChecked():
            self.total_price += 2
        if self.vhsS.isChecked():
            self.total_price += 3.5
        if self.betamaxA.isChecked():
            self.total_price += 2
        if self.vhsA.isChecked():
            self.total_price += 3.5
        if self.betamaxC.isChecked():
            self.total_price += 2
        if self.vhsC.isChecked():
            self.total_price += 3.5
        if self.betamaxAl.isChecked():
            self.total_price += 2
        if self.vhsAl.isChecked():
            self.total_price += 3.5
    # Now update the total label
        self.outputLabel["text"] = "Total price: $%0.2f" % self.total_price
# Global definition of main().
def main():
# Instantiate an object from the class into mainloop()
    VideoStore().mainloop()
# Global call to main()
if __name__ == "__main__":
    main()
