#Used in db.py

class Book:
	#Book class, contains book attributes

	def __init__(self, ID, ISBN, Title, Author, Purchase_Date, Member_ID, Status):
		self.ID = ID
		self.ISBN = ISBN
		self.Title = Title
		self.Author = Author
		self.Purchase_Date = Purchase_Date
		self.Member_ID = Member_ID
		self.Status = Status
	
class Member:

	def __init__(self, Member_ID, ID, Date_Completed, Action):
		self.Member_ID = Member_ID
		self.ID = ID
		self.Date_Completed = Date_Completed
		self.Action = Action