class User(object):
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.books = {}

	def get_email(self):
		return "The email associated with {} is {}.".format(self.name, self.email)

	def change_email(self, new_email):
		self.email = new_email
		return "Email for Username {} has been updated.".format(self.name)

	def __repr__(self):
		return "Username: {}, Email: {}, Books Read: {}.".format(self.name, self.email, len(self.books))

	def __eq__(self, other_user):
		if (self.name == other_user.name) and (self.email == other_user.email):
			other_user = self
		return other_user

	def read_book(self, book, rating=None):
		if rating != None:
			self.books[book] = rating

	def get_average_rating(self):
		rating_sum = 0
		for value in self.books.values():
			rating_sum += value
		return average / len(self.books.keys())

class Book(object):
	def __init__(self, title, isbn):
		self.title = title
		self.isbn = isbn
		self.ratings = []

	def get_title(self):
		return "The title of this book is {}.".format(self.title)

	def get_isbn(self):
		return "The ISBN of this book is {}".format(self.isbn)

	def set_isbn(self, new_isbn):
		self.isbn = new_isbn
		return "ISBN for for book {} has been updated.".format(self.title)

	def add_rating(self, rating):
		if rating >= 0 and rating <= 4:
			self.ratings.append(rating)
		else:
			print("Invalid Rating entered")

	def __eq__(self, other_book):
		if (self.title == other_book.title) and (self.isbn == other_book.isbn):
			other_book = self
			return other_book

	def get_average_rating(self):
		""" Method to get Average Rating on
		the book ratings.
		Could use an if/else for error handling
		but decided to use try/except """

		rating_sum = 0
		for value in self.ratings:
			rating_sum += value
		try:
			return rating_sum / len(self.ratings)
		except (ZeroDivisionError):
			return 0

	def __hash__(self):
		return hash((self.title, self.isbn))

class Fiction(Book):
	def __init__(self, title, author, isbn):
		super().__init__(title, isbn)
		self.author = author

	def __repr__(self):
		return "{title} by {author}".format(title=self.title, author=self.author)

class Non_Fiction(Book):
	def __init__(self, title,  isbn, subject, level):
		super().__init__(title, isbn)
		self.subject = subject
		self.level = level

	def get_subject(self):
		return self.subject

	def get_level(self):
		return self.level

	def __repr__(self):
		return "{title}, a {level} manual on {subject}.".format(title=self.title, level=self.level, subject=self.subject)

# Main TomeRater

class TomeRater:
	def __init__(self):
		self.users = {}
		self.books = {}

	def create_book(self, title, isbn):
		book = Book(title, isbn)
		return book

	def create_novel(self, title, author, isbn):
		fiction = Fiction(title, author, isbn)
		return fiction

	def create_non_fiction(self, title, subject, level, isbn):
		non_fiction = Non_Fiction(title, subject, level, subject)
		return non_fiction

	def add_book_to_user(self, book, email, rating=None):
		if email in self.users:
			self.users[email].read_book(book, email)
			if rating == None:
				rating = 0
			book.add_rating(rating)
			if book not in self.books:
				self.books[book] = 1
			else:
				self.books[book] += 1
		else:
			print("No user with email {email}!".format(email=email))

	def add_user(self, name, email, user_books=None):
		user = User(name, email)
		self.users[email] = user
		if user_books != None:
			for book in user_books:
				self.add_book_to_user(book, email)



##########################
#    Analysis Methods    #
#          for           #
#     TomeRater Class    #


	def print_catalog(self):
		print("<---->    Catalog of Books are:    <---->")
		for book in self.books:
			print("--> %s.\n" % (book.title))

	def print_users(self):
		print("<---->    Users in the System are:    <---->")
		for users in self.users.values():
			print(users)
