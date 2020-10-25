########################Loughborough University MSc Artifical Intelligence########################
########################		Written by Leon Masterman Davies		  ########################
########################	This module contains functions that call      ########################
########################	functions from db.py to query the database    ########################
########################	      for books via name,id,isbn  	          ########################
########################			   functions from db.py 		      ########################
########################	  Written between 18/10/2020 - 25/10/2020 	  ########################


import sqlite3
import db
from classes import Book
import booklist
global cleanAvailableList, cleanEntireList, cleanSearch

#count of amount of books
bookCount = db.countBooks()


def searchBook(srchEntry, srchLbl, popBks, IDBks, AvailBks):

	searchStr=srchEntry.get()
	res = "Searching for " + searchStr

	#clear list for refresh
	popBks.delete('1.0', str(bookCount + 5) + ".0")
	IDBks.delete('1.0', str(bookCount + 5) + ".0")
	AvailBks.delete('1.0', str(bookCount + 5) + ".0")

	popularList = db.searchBookPopular(searchStr)
	IDList = db.viewBook(searchStr)
	AvailList = db.viewBookAvailable(searchStr)
	#format column names

	#POPULAR 
	popularColumns = ["Popularity", "ID", "ISBN", "Title", "Author", "Date Aquired", "Mem ID", "Status"]
	popularColumns="{0:10} | {1:3} | {2:13} | {3:22} | {4:18} | {5:14} | {6:8} | {7:11} |  \n".format(
		popularColumns[0], popularColumns[1], popularColumns[2], 
		popularColumns[3], popularColumns[4], popularColumns[5], 
		popularColumns[6], popularColumns[7])

	#ID
	IDColumns = ["ID",  "ISBN", "Title", "Author", "Date Aquired", "Mem ID", "Status" ]
	IDColumns =" {0:3} | {1:13} | {2:22} | {3:18} | {4:14} | {5:8} | {6:11} | \n".format(
		IDColumns[0], IDColumns[1], IDColumns[2], 
		IDColumns[3], IDColumns[4], IDColumns[5], 
		IDColumns[6])

	#AVAILABLE
	AvailColumns  = ["Status", "ID", "ISBN", "Title", "Author", "Date Aquired", "Mem ID", ]
	AvailColumns  ="{0:11} | {1:3} | {2:13} | {3:22} | {4:18} | {5:14} | {6:8} |".format(
		AvailColumns[0], AvailColumns[1], AvailColumns[2], 
		AvailColumns[3], AvailColumns[4], AvailColumns[5], 
		AvailColumns[6])

	#INSERTS into scrolledtext's
	popBks.insert('1.0', (popularColumns) + "\n" )
	popBks.insert("2.0", "-"*122 + "\n")

	IDBks.insert('1.0', (IDColumns) + "\n" )
	IDBks.insert("2.0", "-"*109 + "\n")

	AvailBks.insert('1.0', (AvailColumns) + "\n" )
	AvailBks.insert("2.0", "-"*109 + "\n")


	counter = 3
	#format items in list
	for item in popularList:
		item = [str(elem) for elem in item]
		popSpacedList = "{0:10} | {1:3} | {2:13} | {3:22} | {4:18} | {5:14} | {6:8} | {7:11} |  \n".format(
			item[0], item[1], item[2], item[3], 
			item[4], item[5], item[6], item[7])
		popBks.insert(str(counter) + ".0", popSpacedList)

		counter += 1

	counter = 3
	#format items in list
	for item in IDList:
		item = [str(elem) for elem in item]
		iDSpacedList = " {0:3} | {1:12} | {2:22} | {3:18} | {4:14} | {5:8} | {6:11} | \n".format(
			item[0], item[1], item[2], item[3], 
			item[4], item[5], item[6])
		IDBks.insert(str(counter) + ".0", iDSpacedList)

		counter += 1

	for item in AvailList:
		item = [str(elem) for elem in item]
		availSpacedList = "{0:11} | {1:3} | {2:13} | {3:22} | {4:18} | {5:14} | {6:8} | \n".format(
			item[0], item[1], item[2], item[3], 
			item[4], item[5], item[6])
		AvailBks.insert(str(counter) + ".0", availSpacedList)

		counter += 1
		srchLbl.configure(text= res)

	





 	
