########################Loughborough University MSc Artifical Intelligence########################
########################		Written by Leon Masterman Davies		  ########################
########################	This module contains functions that deal      ########################
########################	  with checking out books and updating		  ########################
########################	   the books and book_log table through  	  ########################
########################			   functions from db.py 		      ########################
########################	  Written between 18/10/2020 - 25/10/2020 	  ########################



import sqlite3
import db
from classes import Book, Member
from tkinter import * 
from tkinter import messagebox
from datetime import date
from time import strftime, gmtime, time
import booklist

date = date.today()

formattedTime = strftime("%H:%M:%S", gmtime())

bookCount = int(db.countBooks())
strBookCount = str(db.countBooks())
		#Entry field for book ID and member ID
def collectBook(bookEntry, memberEntry):

	

	memID = memberEntry.get()
	bookID = bookEntry.get()
	#member ID must be 4 digits 
	if bookID.isdigit() and len(memID) == 4 and memID.isdigit():
		intBookID = int(bookID)
			#Fail
	else: 
		messagebox.showinfo("Incorrect Syntax", 
						"""Please follow the format (#0000)""" )
		memberEntry.delete(0, "end")
		bookEntry.delete(0, "end")
		return
	#If no values are entered
	if memID is None or bookID is None:
		messagebox.showinfo("Error", "Please enter values into both fields")
		return
	#Check if book ID is out of range
	if intBookID > bookCount: 
		messagebox.showinfo("Book out of range", "Please input a ID within the range of 1 and " + strBookCount)
		return

	availability = db.checkAvailable(bookID)

	#Checking if book is available
	if availability is None:
		messagebox.showinfo("Book Unavailable" , "Sorry, book: " + bookID + " is not available")
		return

	#Sucess - check if ID format is correct
	if availability is not None and len(memID) == 4 and memID.isdigit() and bookID.isdigit():
		db.checkout_book(bookID, memID)
		messagebox.showinfo("Sucess", "Book " +bookID + " checked out by user ID: " + memID)
		#Insert data into db log
		#Creates log in txt file
		db.addToLog(bookID, memID, date, formattedTime, "RENTED")
		#updates book to UNAVAILABLE
		db.bookTransaction()






