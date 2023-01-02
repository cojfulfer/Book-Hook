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
					print("Sorry, looks like that book is already in your library.\n")
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
	publisher = input("What is the name of the book’s publisher?:\n").title()

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
	# print(library)

	print(f"You've successfully added {title} by {authors[0]} to your library!")

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
	removing_title = input("What is the title of the book that you would like to remove from your library?:\n")
	removing_title_author = input("Who is an author of the book that you would like to remove from your library?:\n")
	original_length = len(library)
	for book in library:
		if removing_title in book:  # if book title within key and book author within 'authors' tuple of any book within 'library()' dictionary, remove that book
			authors_tuple = library_contents[library_contents.index(removing_title) + 1]
			for author in authors_tuple:
				if author == removing_title_author:
					library.pop(book)  # or ‘del library[book]’
					print(f"You've successfully removed {removing_title} by {removing_title_author} from your library!")
					break  # to exit for loop once found match in dictionary
		if len(library) != original_length:
			break
	if len(library) == original_length: # if no change was made to dictionary due to no match being found
		print("Sorry, that book is not within your library.\n")
		remove_book = False
		while not remove_book:
			user_choice = input("Do you want to add a book, exit, or return to the main menu ? Enter ‘a’ to add, 'e' to exit, or any other key to return to the main menu:\n")
			if user_choice == 'a':
				add()
			elif user_choice == 'e':
				print("Have a nice day!\n")
				exit()
			elif user_choice != 'a' or 'e':
				welcome()
	welcome()

def find():
		# Step 3: ask user hierarchical guiding classification questions ranging from more general to more niche based on book characteristics and provide list of options show far at each level (but don’t show them the book titles with authors until the very end for the last classification)
		print('Let’s find you a book to read!\n')

		# fiction or nonfiction
		fiction_books = {}  # dictionary of fiction books within the ‘library{}’ dictionary
		nonfiction_books = {}  # dictionary of nonfiction books within the ‘library{}’ dictionary
		count = 0
		for book in library: # first, we check to see if there are any fiction books
			if library[book][0] == 'fiction':
					count += 1
		if count == len(library): # if there are only fiction books, so no nonfiction books
			book_type_books = fiction_books
			book_type = 'fiction'
			book_type_books = library_search(book_type, book_type_books)
		elif count == 0: # if there are no fiction books, so only nonfiction books
			book_type_books = nonfiction_books
			book_type = 'nonfiction'
			book_type_books = library_search(book_type, book_type_books)

		else: # if there are both fiction and nonfiction
			fiction_nonfiction_choice = input(("Would you like to read fiction or nonfiction? Enter ‘f’ for fiction or any other key for nonfiction:\n")).lower()
			if fiction_nonfiction_choice == 'f':
				book_type_books = fiction_books
				book_type = 'fiction'
				book_type_books = library_search(book_type, book_type_books)
			else:
				book_type_books = nonfiction_books
				book_type = 'nonfiction'
				book_type_books = library_search(book_type, book_type_books)

		# genre(s)
		genre_exists = False
		while not genre_exists:
			print(f"Here is your list of {book_type} genres:\n")
			book_type_genres = []  # we will create this empty list and then add the unique elements to this list and then print the elements within this list (don’t even have to refer to the list when printing each genre) 1 by 1
			for book in book_type_books:
				for genre in book_type_books[book][1]:
					if genre not in book_type_genres:
						book_type_genres.append(genre)
						print(genre)
			user_choice = input("\nDo you want to return to the main menu? Enter ‘y’ for yes or any other key for no:\n").lower()
			if user_choice == 'y':
				welcome()
			return_list = search_book_attribute_in_library(book_type_genres, book_type,'genre', genre_exists)
			genre_choice = return_list[0]
			genre_exists = return_list[1]
		# for the books that fall under this book type genre, add them to an empty dictionary
		book_type_genre_books = {}
		for book in book_type_books:
			if genre_choice in book_type_books[book][1]:
				book_type_genre_books[book] = book_type_books[book]

		# publisher
		publisher_exists = False
		while not publisher_exists:
			print(f"Here is your list of {genre_choice} publishers:\n")
			book_type_genre_publishers = [] # we will create this empty list and then add the unique elements to this list and then print the elements within this list (don’t even have to refer to the list when printing each publisher) 1 by 1
			for book in book_type_genre_books:  # for each book of the chosen genre,…
				publisher = book_type_genre_books[book][2]
				if publisher not in book_type_genre_publishers:  # if that book’s publisher is not within the list, add it
					book_type_genre_publishers.append(publisher)
					print(publisher)
			user_choice = input("\nDo you want to return to the main menu? Enter ‘y’ for yes or any other key for no:\n").lower()
			if user_choice == 'y':
				welcome()
			return_list = search_book_attribute_in_library(book_type_genre_publishers, genre_choice, 'publisher', publisher_exists)
			publisher_choice = return_list[0]
			publisher_exists = return_list[1]
		# for the books of the chosen book type genre that fall under the chosen publisher, add them to an empty dictionary
		book_type_genre_publisher_books = {}
		for book in book_type_genre_books:
			if book_type_genre_books[book][2] == publisher_choice:
				book_type_genre_publisher_books[book] = book_type_genre_books[book]

		# year published
		year_published_exists = False
		while not year_published_exists:
			print(f"\nHere is your list of {publisher_choice} published dates:\n")
			book_type_genre_publisher_published_dates = []  # we will create this empty list and then add the unique elements to this list and then print the elements within this list (don’t even have to refer to the list when printing each published date) 1 by 1
			for book in book_type_genre_publisher_books:
				published_date = book_type_genre_publisher_books[book][3]
				if published_date not in book_type_genre_publisher_published_dates:
					book_type_genre_publisher_published_dates.append(published_date)
					print(published_date)
			user_choice = input("\nDo you want to return to the main menu? Enter ‘y’ for yes or any other key for no:\n").lower()
			if user_choice == 'y':
				welcome()
			return_list = search_book_attribute_in_library(book_type_genre_publisher_published_dates, publisher_choice, 'published_date', year_published_exists)
			year_published_choice = return_list[0]
			year_published_exists = return_list[1]
			# for the books of the chosen book type genre publisher that fall under the chosen published date, add them to an empty dictionary
			book_type_genre_publisher_published_date_books = {}
			for book in book_type_genre_publisher_books:
				if book_type_genre_publisher_books[book][3] == year_published_choice:
					book_type_genre_publisher_published_date_books[book] = book_type_genre_publisher_books[book]

		# page range
		# ask user whether  they want a light: (> 200) pages, average: (200-400) pages, or heavy: (400+) pages sized book (each classified based on a predetermined page range) instead of number of pages
		page_range_exists = False
		while not page_range_exists:
			print(f"\nHere is your list of {publisher_choice} page ranges for the books published in {year_published_choice}:\n")
			book_type_genre_publisher_published_dates_page_ranges = []  # we will create this empty list and then add the unique elements to this list and then print the elements within this list (don’t even have to refer to the list when printing each page range) 1 by 1
			for book in book_type_genre_publisher_published_date_books:
				page_range = book_type_genre_publisher_published_date_books[book][4]
				if page_range not in book_type_genre_publisher_published_dates_page_ranges:
					book_type_genre_publisher_published_dates_page_ranges.append(page_range)
					print(page_range)
			user_choice = input("\nDo you want to return to the main menu? Enter ‘y’ for yes or any other key for no:\n").lower()
			if user_choice == 'y':
				welcome()
			return_list = search_book_attribute_in_library(book_type_genre_publisher_published_dates_page_ranges, year_published_choice, 'page range', page_range_exists)
			page_range_choice = return_list[0]
			page_range_exists = return_list[1]
		# for the books of the chosen book type genre publisher published date that fall under the chosen page range, add them to an empty dictionary
		book_type_genre_publisher_published_date_page_range_books = {}
		for book in book_type_genre_publisher_published_date_books:
			if book_type_genre_publisher_published_date_books[book][4] == page_range_choice:
				book_type_genre_publisher_published_date_page_range_books[book] = book_type_genre_publisher_published_date_books[book]

		# Step 4: rank the books from best to worst rating
		def rank(dictionary):  # ranks the remaining books via rating % in descending order
			descending_ratings = []  # iterate through each book within the dictionary and get the last element of each key's value which is the rating and add the ratings to this list and then sort this list in descending order
			descending_ratings_books = []  # a list of the corresponding books for the 'descending ratings[]' list
			for book in dictionary:
				if dictionary[book][5] not in descending_ratings:
					descending_ratings.append(dictionary[book][5])
			for rating in sorted(descending_ratings, reverse=True):
				for book in dictionary:  # iterate through each book for each rating in the 'descending ratings[]' list to check whether that book has that rating
					if dictionary[book][5] == rating:
						if len(book[1]) == 1:  # if the 2nd element of the key is a string, that says that there is only 1 author
							sorted_rated_book = book[0] + ' by ' + book[1][0]  # the format for each book before adding to the 'descending_ratings_books[]' list
							descending_ratings_books.append(sorted_rated_book)
						else:
							if len(book[1]) == 2:  # if the 2nd element of the key is not a string but a tuple, that says that there is more than 1 author
								sorted_rated_book = book[0] + ' by ' + ' and '.join(book[1][0:2])  # the format for each book before adding to the 'descending_ratings_books[]' list
								descending_ratings_books.append(sorted_rated_book)
							elif len(book[1]) > 2:
								sorted_rated_book = book[0] + ' by ' + ', '.join(book[1][0: -1]) + ', and ' + book[1][-1]  # the format for each book before adding to the 'descending_ratings_books[]' list
								descending_ratings_books.append(sorted_rated_book)
			return descending_ratings_books

		# Step 5: return book(s) that match(es) classification criteria
		if len(book_type_genre_publisher_published_date_page_range_books) > 1:
			print(f"\nHere is your list of {genre_choice}, {publisher_choice}, {year_published_choice} books that fall into a page range of {page_range_choice} ranked based on rating percentage in descending order:\n")
			descending_ratings_books = rank(book_type_genre_publisher_published_date_page_range_books)
			for book in descending_ratings_books:
				print(book)
			print(f"\nYou’ve caught a book!\nYour book is {descending_ratings_books[0]}, enjoy!")
			welcome()
		else:
			descending_ratings_books = rank(book_type_genre_publisher_published_date_page_range_books)
			print(f"\nYou’ve caught a book!\nYour book is {descending_ratings_books[0]}, enjoy!")
			welcome()

def library_search(attribute, new_dictionary): # loop through ‘library{}’ dictionary to check what books have the attribute and create new dictionary of the books that do
	for book in library:
		if library[book][0] == attribute:
			new_dictionary[book] = library[book] # adding each key value pair (the whole book) to a new dictionary
	return new_dictionary


def search_book_attribute_in_library(list, attribute_type, attribute, attribute_exists):  # checks attribute quantity and then checks whether user selects one of those
	if len(list) > 1 and attribute == 'publisher':
		attribute_choice = input(f"What {attribute_type} {attribute} do you want to read?:\n").title()
		if attribute_choice not in list:
			print(f"Sorry, that {attribute} does not exist in your library.\n")
			user_choice = input("Do you want to return to the main menu? Enter ‘y’ for yes or any other key for no:\n").lower()
			if user_choice == 'y':
				welcome() # returns user to welcome menu if not then keep going
		else:
			attribute_exists = True
	elif len(list) > 1:
		attribute_choice = input(f"What {attribute_type} {attribute} do you want to read?:\n").lower()
		if attribute_choice not in list:
			print(f"Sorry, that {attribute} does not exist in your library.\n")
			user_choice = input("Do you want to return to the main menu? Enter ‘y’ for yes or any other key for no:\n").lower()
			if user_choice == 'y':
				welcome() # returns user to welcome menu if not then keep going
		else:
			attribute_exists = True
	else:  # no need to prompt user if there’s only 1 option to choose from
		attribute_choice = list[0]
		attribute_exists = True
	return [attribute_choice, attribute_exists]



def welcome(): # welcome menu
	print("\nHello there! Welcome to Book Hook, your personal library assistant!\nLet’s find you a book to read.\nDo you have any books that you want to add to or remove from your library?\n")
	user_choice = input("Enter ‘a’ to add, ‘r’ to remove, ‘f’ to find a book to read, or  ‘e’ to exit:\n").lower()
	if user_choice == 'a':
		add()
	elif user_choice == 'r':
		if len(library) > 0:
			remove()
		else:
			print("Sorry, there are no books to remove in your library.\n")
			remove_book = False
			while not remove_book:
				user_choice2 = input("Do you want to add a book, or exit? Enter ‘a’ to add or 'e' to exit:\n")
				if user_choice2 == 'a':
					add()
				elif user_choice2 == 'e':
					print("Have a nice day!\n")
					exit()
				elif user_choice2 != 'a' or 'e':
					print("Sorry, that is not a valid option.\n")
	elif user_choice == 'f':
		if len(library) > 0:
			find()
		else:
			print("Sorry, there are no books to search in your library.\n")
			print("Let’s add you a book!\n")
			add()
	elif user_choice == 'e':
		print("Have a nice day!\n")
		exit()
	else:
		print("Sorry, that is not a valid option.\n")
		welcome()






















if __name__  == '__main__':
	welcome()
