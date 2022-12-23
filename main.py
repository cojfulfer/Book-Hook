library = {} # in the end, there will be multiple “self_key”s and “self_value”s for each book in this dictionary: {
# {
# (book1Title, (book1Author1, book1Author2, …)) : [book1Fiction/Nonfiction, [book1Genre1, book1Genre2, book1Genre3, …], book1Publisher, book1YearPublished,
# book1PageRange, book1Rating],
# (book2Title, (book2Author1, book2Author2, …)) : [book2Fiction/Nonfiction, [book2Genre1, book2Genre2, book2Genre3, …],  book2Publisher, book2YearPublished,
# book2PageRange, book2Rating],
# (book3Title, (book3Author1, book3Author2, …)) : [book3Fiction/Nonfiction, [book3Genre1, book3Genre2, book3Genre3, …], book3Publisher, book3YearPublished,
# book3PageRange, book3Rating],
# ...}

# Example:
# {...,
# (“1984”, (“George Orwell”)) : [“fiction”, [“science fiction”, “social science fiction”, “dystopian fiction”, “political fiction”], “Secker & Warburg”, 1949, “average: (200 - 400 pages)”, 89.0],
# ...}





class library_book():
	def __init__(self, title, authors, fiction_nonfiction, genres, publisher, year_published, page_range, rating):
		self.title = title
		self.author = tuple(authors) # converts list to tuple
		self.fiction_nonfiction = fiction_nonfiction
		self.genre = genres # list
		self.publisher = publisher
		self.year_published = year_published
		self.page_range = page_range
		self.rating = rating
		self_key = (self.title, self.author) # add book title and author(s) tuple as elements to a tuple
		self_value = [self.fiction_nonfiction, self.genre, self.publisher, self.year_published, self.page_range, self.rating] # 2d list of the book’s characteristics
		library[self_key] = self_value





def add():
	# Step 1:  add book to ‘library{}’ dictionary by gathering book info from user and creating an obj of the ‘book()’ class

	# add new book title & list of the book’s author(s) to ‘library{}’ dictionary via ‘self_key[]’ tuple

	add_book = False
	while add_book != True: # prompts user until they add a book that is not within their library
		# title
		title = input("What is the title of the book that you would like to add to your library?:\n")

		# author(s)
		authors = []
		author = 'author'
		multivalued_attribute(authors, author) # when there could be more than 1 value to a book attribute (e.g. author(s), genre(s), etc.)

		# checks whether book is already added to library
		if library: # can’t loop through an empty dictionary
			for book in library: # loops through each key (book) of the ‘library{}’ dictionary
				if title and tuple(authors) in book: # checks whether there is a match
					print("Sorry, looks like that book is already in your library\n")
					welcome()
				else:
					add_book = True # exits while loop
		else:
			add_book = True # exits while loop


	# add book characteristics as elements to ‘self_value[]’ tuple

	# fiction or nonfiction?
	book_fiction = input("Is the book fiction or nonfiction? Enter ‘f’ for fiction or any other key for nonfiction:\n").lower()
	if book_fiction == 'f':
		fiction_nonfiction = 'fiction'
	else:
		fiction_nonfiction = 'nonfiction'

	# genre(s)
	genres = []
	genre = 'genre'
	multivalued_attribute(genres, genre) # when there could be more than 1 value to a book attribute (e.g. author(s), genre(s))

	# publisher
	publisher = input("What is the name of the book’s publisher?:\n")

	# year published
	year_published = 'year_published'
	year_published = numerical_attribute(year_published) # to ensure that user inputs an integer for numerical attributes (e.g. year published, number of pages, rating, etc.)


	# page range: converts the number of pages from a string to an integer to a page range as a string
	num_pages = 'num_pages'
	num_pages = numerical_attribute(num_pages) # to ensure that user inputs an integer for numerical attributes (e.g. year published, number of pages, rating, etc.)
	if num_pages < 200:
		page_range = 'light: (< 200 pages)'
	elif num_pages > 400:
		page_range = 'heavy: (> 400 pages)'
	else:
		page_range = 'average: (200 - 400 pages)'

	# rating %: converts the rating % from a string to an integer
	rating = 'rating'
	rating = numerical_attribute(rating) # to ensure that user inputs an integer for numerical attributes (e.g. year published, number of pages, rating, etc.)


	my_library_book = library_book(title, authors, fiction_nonfiction, genres, publisher, year_published, page_range, rating) # sets the book as an obj of the ‘book()’ class
	print(library)

	welcome()


def multivalued_attribute(list, attribute):  # when there could be more than 1 value to a book attribute (e.g. author(s), genre(s), etc.)
	book_multiple_values = input(f"Does the book have more than 1 {attribute}? Enter ‘y’ for yes or any other key for no:\n").lower()
	if book_multiple_values == 'y':
		add_value = 'n'
		while add_value != 'y':
			if attribute == 'author':
				list.append(input(f"Who is an {attribute} of the book?:\n"))
				if len(list) > 1:
					add_value = input(f"Are these all the {attribute}s of the book? Enter ‘y’ for yes or any other key for no:\n").lower()
				else:
					list.append(input(f"Who is another {attribute} of the book?:\n"))
					add_value = input(f"Are these all the {attribute}s of the book? Enter ‘y’ for yes or any other key for no:\n").lower()
			else:
				list.append(input(f"What is a {attribute} of the book?:\n").lower())
				if len(list) > 1:
					add_value = input(f"Are these all the {attribute}s of the book? Enter ‘y’ for yes or any other key for no:\n").lower()
				else:
					list.append(input(f"What is another {attribute} of the book?:\n").lower())
					add_value = input(f"Are these all the {attribute}s of the book? Enter ‘y’ for yes or any other key for no:\n").lower()
	else:
		if attribute == 'author':
			list.append(input(f"Who is the {attribute} of the book?:\n"))
		else:
			list.append(input(f"What is the {attribute} of the book?:\n").lower())
	return list


def numerical_attribute(attribute):  # to ensure that user inputs an integer for numerical attributes (e.g. year published, number of pages, rating %, etc.)
	while isinstance(attribute, str):
		if attribute == 'year_published':
			try:
				attribute = int(input("What year was the book published? Please enter an integer (e.g. 2001, 1890, 1975, etc.):\n"))
			except ValueError:
				print("Sorry, invalid character.\n")
		elif attribute == 'num_pages':
			try:
				attribute = int(input("How many pages is the book? Please enter an integer (e.g. 10, 75, 150, 350, 1000, etc.):\n"))
			except ValueError:
				print("Sorry, invalid character.\n")
		else:
			while '%' not in attribute:
				attribute = input("What is the rating of the book from Google? Please enter a percentage (e.g. 95% liked this book):\n")
				if '%' in attribute == False:
					print("Sorry, invalid character.\n")
			attribute = float(attribute.strip('%'))  # get rid of the percent sign the user inputs and then convert it into a float
	return attribute


def remove():
	# Step 2:  if a key (book) in the ‘library{}’ dictionary contains the title and author user wants to remove, then remove that key (book) from the dictionary
	library_contents = [elem for key in library for elem in key]
	removed = False
	while not removed:
		removing_title = input("What is the title of the book that you would like to remove from your library?:\n")
		removing_title_author = input("Who is an author of the book that you would like to remove from your library?:\n")
		original_length = len(library)
		for book in library:
			if removing_title in book:  # if book title within key and book author within 'authors' tuple of any book within 'library()' dictionary, remove that book
				authors_tuple = library_contents[library_contents.index(removing_title) + 1]
				for author in authors_tuple:
					if author == removing_title_author:
						library.pop(book)  # or ‘del library[book]’
						removed = True  # to exit out of while loop
						break  # to exit for loop once found match in dictionary
			if len(library) != original_length:
				break
		if len(library) == original_length: # if no change was made to dictionary due to no match being found
			print("Sorry, that book is not within your library.\n")
			removed = True
	welcome()



def welcome(): # welcome menu
	print("\nHello there! Welcome to Book Hook, your personal library assistant!\nLet’s find you a book to read.\nDo you have any books that you want to add to or remove from your library?\n")
	user_choice = ''
	while user_choice != ('a' or 'f' or 'r' or 'e'):
		user_choice = input("Enter ‘a’ to add, ‘r’ to remove, ‘f’  to find a book to read, or  ‘e’  to exit:\n").lower()
		if user_choice == 'a':
			add()
		elif user_choice == 'r':
			if len(library) > 0:
				remove()
			else:
				print("Sorry, there are no books to remove in your library.\n")
				print("Let’s add you a book!\n")
				add()
		elif user_choice == 'f':
			if len(library) > 0:
				find()
			else:
				print("Sorry, there are no books to search in your library.\n")
				print("Let’s add you a book!\n")
				add()
		elif user_choice == 'e':
			print("Have a nice day!\n")
			break
		else:
			print("Sorry, that is not a valid option.\n")






















if __name__  == '__main__':
	welcome()
