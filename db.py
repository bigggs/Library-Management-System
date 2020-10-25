########################Loughborough University MSc Artifical Intelligence########################
########################          Written by Leon Masterman Davies        ########################
########################       This module contains all the functions     ########################
########################         relating to querying the database        ########################
########################      Written between 18/10/2020 - 25/10/2020     ########################

import sqlite3
from classes import Book, Member
import numpy as np
from datetime import date
connection = sqlite3.connect('library.db')
sqlCommand = connection.cursor() #use for sql executes




  ###########################################
  ##################BOOK DATA################
  ###########################################




#Create initial library database if not already built
def createBooks():
  sqlCommand.execute("""CREATE TABLE IF NOT EXISTS
                    books(
                        ID integer PRIMARY KEY,
                        ISBN text,
                        Title text,
                        Author text, 
                        Purchase_Date text,
                        Member_ID integer,
                        Status text,
                        Popularity integer
                    )""")
  connection.commit()

def insertTxtBooks():
  #Insert data from /info/book_info.txt into database file: library.db
  bookTxtData = open('info/Book_Info.txt', 'r')
  bookData = [line.strip().split(":") for line in bookTxtData]
  bookTxtData.close()

  #Error handling for repeat data
  try:
    sqlCommand.executemany("""INSERT INTO books(
    ID, ISBN, Title, Author, Purchase_Date, Member_ID, Status, Popularity)
    VALUES(?, ?, ?, ?, ?, ?, ?, 0)""", bookData)

  except Exception as e:
      print(e)

  connection.commit()


#Insert new book
def insert_book(book):
  newBook = book
  with connection:
    try:
      sqlCommand.execute("""INSERT INTO books VALUES (
             :ID, :ISBN, :Title, :Author, 
              :Purchase_Date, :Member_ID, :Status
              )""", 
      {'ID': newBook.ID, 'ISBN': newBook.ISBN, 'Title': newBook.Title, 
      'Author': newBook.Author, 'Purchase_Date': newBook.Purchase_Date, 
      'Member_ID': newBook.Member_ID, 'Status': newBook.Status})
      connection.commit()
    except Exception as e:
      print(e)

#Test function
#testInsert = Book(45, 9783361484100, "test", "Qest", "15/10/2020", 63, "UNAVALIABLE")
#insert_book(testInsert)

#Return a book
def return_book(bookID):
    with connection:
      try:
          sqlCommand.execute("""UPDATE BOOKS
                SET Member_ID = "",
                  Status = "AVAILABLE"
                WHERE ID = ?""", (bookID,))
          connection.commit()
      except Exception as e:
          print(e)

#Test Function
#return_book(45)

# Get booklist by popularity
def mostPopular():
  with connection:
    try:
      sqlCommand.execute("""SELECT Popularity, ID, ISBN, Title, 
                          Author, Purchase_Date, Member_ID, Status 
                          FROM books
                          ORDER BY Popularity desc  """)
      connection.commit()
    except Exception as e:
      print(e)
    finally:
      ans = sqlCommand.fetchall()
      return ans

#Testing most popular      
#mostPopular()

#Get book inventory member view
def memberGetBookList():

  with connection:
    try:  
      sqlCommand.execute("""SELECT Status, ID, ISBN, Title, 
                          Author, Purchase_Date, Member_ID 
                          FROM books
                          ORDER BY status  """)
      connection.commit()

    except Exception as e:
      print(e)
    finally:
      bookList = sqlCommand.fetchall()
      return bookList

#Test Function
#memberGetBookList()


#Get book inventory staff view
def staffGetBookList():

  with connection:
    try: #Returns entire inventory of books
      sqlCommand.execute("SELECT * FROM BOOKS")

    except Exception as e:
      print(e)
    finally:
      bookList = sqlCommand.fetchall()
      
      return(bookList)
# Test function
# staffGetBookList()

#Get book inventory member view
def getUnavailableList():

  with connection:
    try: #Only returns relevant entities for members 
      sqlCommand.execute("""SELECT * FROM BOOKS
                          WHERE Status = "UNAVAILABLE" """)
      connection.commit()

    except Exception as e:
      print(e)
    finally:
      bookList = sqlCommand.fetchall()
      return bookList

#Test Function
#memberGetBookList()


#Return specific books matching search criteria of TITLE/AUTHOR/ISBN -
#Sorted by popularity
def searchBookPopular(bookSearch):
  
  with connection:
    try:
          sqlCommand.execute("""SELECT Popularity, ID, ISBN, Title, 
                              Author, Purchase_Date, Member_ID, Status 
                              FROM books
                      WHERE Title LIKE ? or Author LIKE ? or ISBN LIKE ? 
                      ORDER BY Popularity DESC""",
                       ('%'+bookSearch+'%','%'+bookSearch+'%','%'+bookSearch+'%',))
          ans = sqlCommand.fetchall()
          return ans
    except Exception as e:
          print(e)
#Test function
#viewBook("CS")


#Return specific books matching search criteria of TITLE/AUTHOR/ISBN
def viewBook(bookSearch):
  
  with connection:
    try:
          sqlCommand.execute("""SELECT * FROM books
                      WHERE Title LIKE ? or Author LIKE ? or ISBN LIKE ? """,
                       ('%'+bookSearch+'%','%'+bookSearch+'%','%'+bookSearch+'%',))
          ans = sqlCommand.fetchall()
          return ans
    except Exception as e:
          print(e)
#Test function
#viewBook("CS")
#Return specific books matching search criteria of TITLE/AUTHOR/ISBN
def viewBookAvailable(bookSearch):
  
  with connection:
    try:
          sqlCommand.execute("""SELECT Status, ID, ISBN, Title, 
                              Author, Purchase_Date, Member_ID 
                      FROM BOOKS
                      WHERE Title LIKE ? or Author LIKE ? or ISBN LIKE ? 
                      AND STATUS = "AVAILABLE"
                      ORDER BY status 
                      """,
                       ('%'+bookSearch+'%','%'+bookSearch+'%','%'+bookSearch+'%',))
          ans = sqlCommand.fetchall()
          return ans
    except Exception as e:
          print(e)
#Test function
#viewBook("CS")


#Checkout a book
def checkout_book(bookID, memberID):
    with connection:
      try:
          sqlCommand.execute("""UPDATE BOOKS
                SET Member_ID = ?,
                  Status = "UNAVAILABLE",
                  Popularity = Popularity + 1
                WHERE ID = ?""", (memberID, bookID))
          connection.commit()
      except Exception as e:
          print(e)

# Test Function
#checkout_book(45, 100)

#Count total amount of books
def countBooks():
  with connection:
    try:
      sqlCommand.execute("SELECT count(ID) FROM books")
      ans = sqlCommand.fetchone()
      output = ans
      return (ans[0])


    except Exception as e:
      print(e)


#Check if a book is available
def checkAvailable(AvailID):
  with connection:
    try:
          sqlCommand.execute("""SELECT * FROM books
                      WHERE ID = ? and Status = 'AVAILABLE' """,
                       (AvailID,))
          ans = sqlCommand.fetchone()
          return(ans)
    except Exception as e:
          print(e)

#Test function
#print(checkAvailable(20))



  ###########################################
  ##################BOOK LOGS################
  ###########################################




#Creates book_log table if not exists
def createLogs():
  sqlCommand.execute("""CREATE TABLE IF NOT EXISTS
                    book_log(
                        Transaction_ID integer PRIMARY KEY,
                        Member_Id integer,
                        ID integer,
                        Date_Completed text,
                        Time_Completed text,
                        Action text
                    )""")
  connection.commit()
  #Adds a book to the log table in the DB
def addToLog(bookID, memberID, date_completed, time_completed, action):
  #Calulcates the transcation ID
    with connection:
            sqlCommand.execute("""SELECT count(ID)
                                FROM book_log""")
            output = sqlCommand.fetchone()
            transID = output[0] + 1
            #Inserts new log
    try:
      sqlCommand.execute("""INSERT INTO book_log VALUES(
                             ?,?, ?, ?, ?, ?)""", (transID, bookID, memberID, date_completed, time_completed, action))
      connection.commit()
    except Exception as e:
      print(e)
#Test add to log
#addToLog(1, 1, 10-10-2015, "RENTED")     




#Test insert 
# testInsert = (2006, 2, "12/10/2020", "Returned")
# addToLog(testInsert)

  #Join tables to get data for txt file
def bookTransaction():
  with connection:
    try:
      sqlCommand.execute("""SELECT book_log.Transaction_ID, books.ID, books.Title, 
                  book_log.Date_Completed, book_log.Action,
                  books.Member_ID 
                  
                  FROM books INNER JOIN book_log using(ID)
                  
                  """)
              #Write data to txt log
      output = sqlCommand.fetchall()
      with open("info/Loan_History.txt", "w") as fileWrite:
        fileWrite.write("\n".join(str(item) for item in output))
      #Test book Transaction
      #print(output)
    except Exception as e:
      print(e)

  #Returns book values from book_log that have been RETURNED
def bookReturns():
  with connection:
    try:
      sqlCommand.execute("""SELECT Date_Completed, Time_Completed, ID, Member_ID, Action
                                FROM book_log 
                                WHERE action ='RETURNED' 
                                ORDER BY Date_Completed ASC
                                """)
      output = sqlCommand.fetchall()
      return output
    except Exception as e:
      print(e)
    #test book returns
# bookReturns()

  #returns book values from book_log that have been RENTED
def bookRents():
  with connection:
    try:
      sqlCommand.execute("""SELECT Date_Completed, Time_Completed, ID, Member_ID, Action
                                FROM book_log 
                                WHERE action ='RENTED' 
                                ORDER BY Date_Completed ASC
                                """)
      output = sqlCommand.fetchall()
      return output
    except Exception as e:
      print(e)
    #test book rents
# bookRents()

  #returns entire book_log
def allLog():
  with connection:
    try:
      sqlCommand.execute("""SELECT Date_Completed, Time_Completed, ID, Member_ID, Action
                                   FROM book_log 
                                   ORDER BY Date_Completed ASC
                                """)
      output = sqlCommand.fetchall()
      return output
    except Exception as e:
      print(e)
    #test book rents
# allLog()

  ###########################################
  ##################GRAPHS###################
  ###########################################


#Returns 5th most popular books
def popularitySelect():
  with connection:
    try:
      sqlCommand.execute("""SELECT ID AS Titles, Popularity AS Popularity 
                            FROM books
                            WHERE popularity > 0
                            GROUP BY Title
                            ORDER BY popularity desc
                            LIMIT 20
        """)
      output = sqlCommand.fetchall()
      Titles = []
      Popularity = []
      for out in output:
        Titles.append(out[0])
        Popularity.append(out[1])
      return  Titles, Popularity
    except Exception as e:
      print(e)
#test function
#popularitySelect()


#Returns 5th most popular books
def selectPopularityToday():

  with connection:
    try:
      sqlCommand.execute("""SELECT books.Title AS Titles, books.Popularity AS Popularity 
                            FROM books, book_log
                            WHERE popularity > 0 and book_log.date_completed = ?
                            GROUP BY Title
                            ORDER BY popularity desc
                            LIMIT 5
        """), ("22-10-2020")
      output = sqlCommand.fetchall()
      Titles = []
      Popularity = []
      for out in output:
        Titles.append(out[0])
        Popularity.append(out[1])
      return  Titles, Popularity
    except Exception as e:
      print(e)
#test function
#popularitySelect()

  ###########################################
  ##################MAIN#####################
  ###########################################

def main():
    #books
  createBooks()
  insertTxtBooks()
    #logs
  createLogs()

if __name__=='__main__':
  main()
