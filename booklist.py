########################Loughborough University MSc Artifical Intelligence########################
########################		Written by Leon Masterman Davies		  ########################
########################	This module contains functions that list      ########################
########################		 the books data and book log data 		  ########################
########################	    into the scrolledtexts on the GUI 		  ########################
########################	  Written between 18/10/2020 - 25/10/2020 	  ########################


import sqlite3
import db
from classes import Book
import tkinter as Tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.ticker as ticker
import numpy 

bookCount = db.countBooks()

			##########BOOKS##########
#Popular list
	#scrolledText view, db function
def popularBookList(searchView, dbList):
	#clear list for refresh
	searchView.delete('1.0', str(bookCount + 5) + ".0")
	bookList = dbList
	#format column names
	columns = ["Popularity", "ID", "ISBN", "Title", "Author", "Date Aquired", "Mem ID", "Status"]
	spacedColumns="{0:10} | {1:3} | {2:13} | {3:22} | {4:18} | {5:14} | {6:8} | {7:11} |  \n".format(
		columns[0], columns[1], columns[2], columns[3], 
		columns[4], columns[5], columns[6], columns[7])

	searchView.insert('1.0', (spacedColumns) + "\n" )
	searchView.insert("2.0", "-"*122 + "\n")
	counter = 3
	#format items in list
	for item in bookList:
		item = [str(elem) for elem in item]
		spacedList = "{0:10} | {1:3} | {2:13} | {3:22} | {4:18} | {5:14} | {6:8} | {7:11} |  \n".format(
			item[0], item[1], item[2], item[3], 
			item[4], item[5], item[6], item[7])
		searchView.insert(str(counter) + ".0", spacedList)

		counter += 1


#Available list		
def availableBookList(searchView, dbList):
	searchView.delete('1.0', str(bookCount + 5) + ".0")
	#cannot re-use (only 7 columns)
	bookList = dbList
	#format column names
	columns = ["Status", "ID", "ISBN", "Title", "Author", "Date Aquired", "Mem ID", ]
	spacedColumns="{0:11} | {1:3} | {2:13} | {3:22} | {4:18} | {5:14} | {6:8} | \n".format(
		columns[0], columns[1], columns[2], columns[3], 
		columns[4], columns[5], columns[6])

	searchView.insert('1.0', (spacedColumns) + "\n" )
	searchView.insert("2.0", "-"*109 + "\n")
	counter = 3
	#format items in list
	for item in bookList:
		item = [str(elem) for elem in item]
		spacedList = "{0:11} | {1:3} | {2:13} | {3:22} | {4:18} | {5:14} | {6:8} | \n".format(
			item[0], item[1], item[2], item[3], 
			item[4], item[5], item[6])
		searchView.insert(str(counter) + ".0", spacedList)

		counter += 1


#IDlist
def idBookList(searchView, dbList):
	searchView.delete('1.0', str(bookCount + 5) + ".0")
	bookList = dbList
	#format column names
	columns = ["ID",  "ISBN", "Title", "Author", "Date Aquired", "Mem ID", "Status" ]
	spacedColumns=" {0:3} | {1:12} | {2:22} | {3:18} | {4:14} | {5:8} | {6:11} | \n".format(
		columns[0], columns[1], columns[2], columns[3], 
		columns[4], columns[5], columns[6])

	searchView.insert('1.0', (spacedColumns) + "\n" )
	searchView.insert("2.0", "-"*109 + "\n")
	counter = 3
	#format items in list
	for item in bookList:
		item = [str(elem) for elem in item]
		spacedList = "{0:3} | {1:13} | {2:22} | {3:18} | {4:14} | {5:8} | {6:11} | \n".format(
			item[0], item[1], item[2], item[3], 
			item[4], item[5], item[6])
		searchView.insert(str(counter) + ".0", spacedList)

		counter += 1
		##########BOOK_LOG##########
def printBookLog(searchView, dbLog):
		searchView.delete('1.0', '50.0')


		logList = dbLog

		columns = ["Date", "Time", "Member ID", "Book ID", "Action"]
		spacedColumns = "{0:10} | {1:10} | {2:9} | {3:7} | {4:10} | \n".format(
			columns[0], columns[1], columns[2], 
			columns[3], columns[4])
		searchView.insert('1.0', (spacedColumns) + "\n")
		searchView.insert('2.0', "-"*60 + "\n")
		counter = 3
		for item in logList:
			item = [str(elem) for elem in item]
			spacedList = "{0:10} | {1:10} | {2:9} | {3:7} | {4:10} | \n".format(
				item[0], item[1], item[2], 
				item[3], item[4])
			searchView.insert(str(counter) + ".0", spacedList)
			counter += 1




#############GRAPHS#############

#Draws a graph in a view
#View, x axis, y axis
def drawGraph(view, x, y):
	#Size

	plt.rcParams.update({'font.size': 11})
	f = Figure(figsize=(5,5), dpi=65)
	ax = f.add_subplot(111)

	#Limits ranges to whole numbers
	xpos = x[0:4]
	ypos = y[0:4]

	#Titles and labels
	ax.set_title('Most Popular Books')
	ax.set_xlabel('ID')
	ax.set_ylabel('Times Rented')

	#Print bar graph
	rects1 = ax.bar(ypos,xpos)

	#Place in Tkinter window
	canvas = FigureCanvasTkAgg(f, master=view)

	canvas.get_tk_widget().grid(column = 0, row = 0)

	Tk.mainloop()
