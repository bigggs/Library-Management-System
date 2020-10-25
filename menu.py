########################Loughborough University MSc Artifical Intelligence########################
########################		Written by Leon Masterman Davies		  ########################
########################	This module contains functions that display   ########################
########################		  the GUI and link functionality 		  ########################
########################	  Written between 18/10/2020 - 25/10/2020 	  ########################


from tkinter import * 
from tkinter import scrolledtext
from tkinter.ttk import *
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure 
import db 
import classes
import booksearch
import bookcheckout
import bookreturn
import booklist

	#Search book function, calls functions from db.py 
def importedBookSearch():
	booksearch.searchBook(searchEntry, searchLabel,popularBooksText,idBooksText,availableBooksText)

	#reset button for search, resets views
def importedResetButton():
	booklist.popularBookList(popularBooksText, db.mostPopular())
	booklist.availableBookList(availableBooksText, db.memberGetBookList())
	booklist.idBookList(idBooksText, db.staffGetBookList())


	#checkout button functionality, updates all view, calls function to update db table
def importedCheckoutButton():
	bookcheckout.collectBook(rentBookIDEntry, memIDEntry)
	#refresh booklist and booklog + graph
	booklist.popularBookList(popularBooksText, db.mostPopular())
	booklist.availableBookList(availableBooksText, db.memberGetBookList())
	booklist.idBookList(idBooksText, db.staffGetBookList())
	booklist.printBookLog(bookLogAll, db.allLog())
	booklist.printBookLog(bookLogRented, db.bookRents())
	booklist.printBookLog(bookLogReturned, db.bookReturns())
	graphCanvas()
	#returning books
def importedReturnButton():
	bookreturn.returnBook(bookIDEntry)
	#refresh booklist and booklog + graphCanvas
	#Srolledtext/view, db function
	booklist.popularBookList(popularBooksText, db.mostPopular())
	booklist.availableBookList(availableBooksText, db.memberGetBookList())
	booklist.idBookList(idBooksText, db.staffGetBookList())
	booklist.printBookLog(bookLogAll, db.allLog())
	booklist.printBookLog(bookLogRented, db.bookRents())
	booklist.printBookLog(bookLogReturned, db.bookReturns())
	graphCanvas()
def aboutInfo():
	messagebox.showinfo("Lboro Library", "Writen by Leon Davies for MSc Artificial Intelligence")

	#list views for logs and books 	
	#Srolledtext/view, db function
def importedAvailableList():
	booklist.availableBookList(availableBooksText, db.memberGetBookList())
def importedEntireList():
	booklist.idBookList(idBooksText, db.staffGetBookList())
def importedPopularList():
	booklist.popularBookList(popularBooksText, db.mostPopular())
def importedPrintBookLog():
	booklist.printBookLog(bookLogAll, db.allLog())
def importedRentedList():
	booklist.printBookLog(bookLogRented, db.bookRents())
def importedReturnedList():
	booklist.printBookLog(bookLogReturned, db.bookReturns())

	#Create booklists canvas	
def createCanvas():
	global searchEntry, searchLabel, availableBooksText, idBooksText, popularBooksText
	
	#Book search results
	tabControl = Notebook(window)
	tabControl.grid(column=1, row = 0, rowspan = 10)
	
	popularBooksView = Frame(tabControl)
	avaliableBooksView = Frame(tabControl)
	allBooksView = Frame(tabControl)

	#Shows books in popularity order
	tabControl.add(popularBooksView, text = "Sort by Popularity")
	#Shows only books marked as "AVAILABLE"
	tabControl.add(avaliableBooksView, text="Sort by Availability")
	#Shows all books
	tabControl.add(allBooksView, text ="Sort by ID")


	allBooksFrame = Frame(avaliableBooksView)
	allBooksFrame.grid(column=1, row = 0)

	availableBookView = Frame(allBooksView)
	availableBookView.grid(column=1, row = 0)

	popularBooksFrame = Frame(popularBooksView)
	popularBooksFrame.grid(column=1, row = 0)

	#POPULAR books
	popularBooksText = scrolledtext.ScrolledText(popularBooksFrame, width= 124, height = 20)
	popularBooksText.grid(column=1, row = 0)
	#Displays list of books in popularity order
	importedPopularList()

	#AVAILABLE books
	availableBooksText = scrolledtext.ScrolledText(allBooksFrame, width = 124, height = 20)
	availableBooksText.grid(column=1, row =0)
	#Displays list of availiable books in the frame
	importedAvailableList()

	#ALL books
	idBooksText = scrolledtext.ScrolledText(availableBookView, width = 124, height = 20)
	idBooksText.grid(column=1, row = 0)
	#Displays list of all books with all data
	importedEntireList()


	#Search box/button
	searchEntry = Entry(window)
	searchEntry.grid(column = 0, row = 2)


	searchLabel = Label(window, text = "Search for books")
	searchLabel.grid(column= 0, row = 1)
	searchBtn = Button(window, text = "Search", command = importedBookSearch)
	resetBtn = Button(window, text = "Reset", command= importedResetButton)

	searchBtn.grid(column = 0, row = 3)
	resetBtn.grid(column=0, row =4)

	#frames for rent/return UI
def rentReturnCanvas():
	global rentBookIDEntry, memIDEntry, bookIDEntry, alertLabel, availableBooksText, popularBooksText
	tabControl = Notebook(window)
	tabControl.grid(column=0, row = 5)
	rentingView = Frame(tabControl)
	returningView = Frame(tabControl)
	#Shows only books marked as "AVAILABLE"
	tabControl.add(rentingView, text="Rent a book")
	#Shows all books
	tabControl.add(returningView, text ="Return a book")
	rentFrame = Frame(rentingView)
	rentFrame.grid(column=0, row = 5)
	returnFrame = Frame(returningView)
	returnFrame.grid(column=0, row = 5)

	####RENT A BOOK####
	memIDEntry = Entry(rentFrame, width = 25)
	rentBookIDEntry = Entry(rentFrame, width = 25)

	memIdLbl = Label(rentFrame, text = "Member ID")
	bookIdLbl = Label(rentFrame, text = "Book ID")

	rentBtn = Button(rentFrame, text = "Checkout", command=importedCheckoutButton)



	#Spacing
	memIDEntry.grid(column = 0, row = 2)
	memIdLbl.grid(column = 0, row = 1)
	rentBookIDEntry.grid(column= 1, row = 2)
	bookIdLbl.grid(column = 1, row = 1)


	rentBtn.grid(ipady = 7, pady = 25)

	####RETURN A BOOK####
	bookIDEntry = Entry(returnFrame, width = 25)

	memIdLbl = Label(returnFrame, text = "Member ID")
	bookIdLbl = Label(returnFrame, text = "Book ID")

	bookIDEntry = Entry(returnFrame, width = 25)
	returnBookID = Label(returnFrame, text = "Book ID")

	confirmReturn = Button(returnFrame, text = "Return", command=importedReturnButton)

	bookIDEntry.grid(column = 2, row = 3, padx = 70)
	returnBookID.grid(column =2, row =2, pady = 15)
	confirmReturn.grid(column = 2, row = 4, ipady = 7, pady = 15)

	#cavnas for book log
def bookLogCanvas():
	global  bookLogAll, bookLogRented, bookLogReturned

	tabControl = Notebook(window)
	tabControl.grid(column=1, row = 10)
	allView = Frame(tabControl)
	rentView = Frame(tabControl)
	returnView = Frame(tabControl)
	#Shows only books marked as "AVAILABLE"
	tabControl.add(allView, text="Book History")
	#Shows only books marked as "AVAILABLE"
	tabControl.add(rentView, text="Sort by Rented")
	#Shows all books
	tabControl.add(returnView, text ="Sort by returned")
	rentFrame = Frame(rentView)
	rentFrame.grid(column=1, row = 10)
	returnFrame = Frame(returnView)
	returnFrame.grid(column=1, row = 10)

	bookLogAll = scrolledtext.ScrolledText(allView, width= 124, height = 20)
	bookLogAll.grid(column=1, row = 10)
	#Displays list of books in popularity order
	importedPrintBookLog()

	bookLogRented = scrolledtext.ScrolledText(rentView, width= 124, height = 20)
	bookLogRented.grid(column=1, row = 10)
	#Displays list of books in popularity order
	importedRentedList()

	#AVAILABLE books
	bookLogReturned = scrolledtext.ScrolledText(returnView, width = 124, height = 20)
	bookLogReturned.grid(column=1, row =10)
	#Displays list of availiable books in the frame
	importedReturnedList()


	#canvas for matplotlib graph
def graphCanvas():
	Titles, Popularity = db.popularitySelect()
	#titlesToday, popularityToday = db.selectPopularityToday()
	global searchEntry, searchLabel, availableBooksText, idBooksText, popularBooksText

	graphControl = Notebook(window)
	graphControl.grid(column=0, row = 10)
	graph1View = Frame(graphControl)
	graph2View = Frame(graphControl)
	#Shows 5 most rented out books
	graphControl.add(graph1View, text="5 Most Popular Books")

	graph1Frame = Frame(graph1View)
	graph1Frame.grid(column=0, row = 10)



	booklist.drawGraph(graph1View, Popularity, Titles)
	#booklist.drawGraph(graph2View, popularityToday, titlesToday)

	#menu bar
def printMenuBar(): 
	menubar = Menu(window)
	#FILE
	filemenu = Menu(menubar, tearoff=0)
	filemenu.add_command(label="Exit", command=window.destroy)
	menubar.add_cascade(label="File", menu=filemenu)

	#HELP
	aboutMenu = Menu(menubar, tearoff=0)
	aboutMenu.add_command(label="About", command= aboutInfo)
	menubar.add_cascade(label="Help", menu=aboutMenu)

	#Displays bar
	window.config(menu=menubar)

	###########################################
	#####################MAIN##################
	###########################################

def main():
	global window
	window = Tk()
	window.title("Loughborough University Library")
	window.geometry('1344x700')
	window.resizable(False, False)

	createCanvas() #Book info
	rentReturnCanvas() # rent/return box
	printMenuBar() # Menu bar
	bookLogCanvas() #Book logs info
	graphCanvas() #Matplotlib graph

	window.mainloop()

if __name__=='__main__':
	main()