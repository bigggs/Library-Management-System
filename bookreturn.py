########################Loughborough University MSc Artifical Intelligence########################
########################		Written by Leon Masterman Davies		  ########################
########################	This module contains functions that deal      ########################
########################		 with returning books and updating		  ########################
########################	    	the book_log table through  		  ########################
########################			   functions from db.py 		      ########################
########################	  Written between 18/10/2020 - 25/10/2020 	  ########################




import sqlite3
import db
from classes import Book, Member
from tkinter import * 
from tkinter import messagebox
from datetime import date
from datetime import date
from time import strftime, gmtime, time

formattedTime = strftime("%H:%M:%S", gmtime())
date = date.today()
bookCount = int(db.countBooks())
strBookCount = str(db.countBooks())
	#return a book
def returnBook(bookEntry):
	
	bookID = bookEntry.get()
	if bookID.isdigit():
		intBookID = int(bookID)
	strBookID = str(bookID)
	
	#if empty entry
	if bookID is None:
		messagebox.showinfo("Error", "Please enter a book ID to return")
		return



	#invalid book ID
	if bookID.isdigit() and intBookID > bookCount:
		messagebox.showinfo("Incorrect book ID", "Please enter a valid Book ID")
		return

	availability = db.checkAvailable(bookID)
	if availability is not None:
		messagebox.showinfo("Book Already returned", "Please double check the book ID entered")
		return

		#check if numbers
	if availability is None and strBookID.isdigit():
		db.return_book(bookID)
		messagebox.showinfo("Sucess", "Book " +strBookID + " sucessfully returned")
		db.addToLog(bookID, "", date, formattedTime,  "RETURNED")
		db.bookTransaction()
		#incorrect syntax
	else:
		messagebox.showinfo("Incorrect Syntax", 
						"""Please follow the format (#0000)""" )


		

