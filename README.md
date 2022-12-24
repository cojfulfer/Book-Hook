# Book-Hook
This program is a library filter assistant that helps the user decide what to read next based on books they want to read. 

The name of the program is an analogy: the user is the fisher, the program is the fishing pole, the user’s library is the body of water, and the book that the user will read is the caught fish.  

The program will gather information from the user about each book they would like to read: title, author(s), fiction/nonfiction, genre(s), publisher, year published, number of pages, rating percentage. As the user’s library grows, the program can help filter what book the user would want to read by asking hierarchical guiding classification questions from the info the user provided on each book. The program can then recommend a book or a list of books based on the answers to the questions the user provides. 


Basic Version
For now, the basic version of the program will guide the user on what kind of book they would like to read from their library of ‘to-read’ books via the ‘find()’ function. At the start of the program, the ‘welcome()’ function asks the user what they would like to do: add a book, remove a book, find a book, or exit the program. 

The ‘add()’ function will gather book information when the user wants to add a ‘to-read’ book to their library. The library will be a dictionary, the title and author(s) of each book will be a key in the dictionary, and the characteristics (e.g. fiction/nonfiction, genre(s), publisher, year published, number of pages, rating percentage) for each book will be the value of that key. 

The ‘remove()’ function will remove a pre-existing book that the user wants to remove from their library. 

Lastly, the ‘find()’ function will ask the user whether they would want to read fiction or nonfiction. Then the program will prompt the user to choose from a list of the fiction or nonfiction genres within their library. The program will then prompt the user to choose from a list of publishers available for that genre. Next, the program will prompt the user to choose from a list of published dates available for that publisher. Further, the program will prompt the user to choose from a list of page ranges available for that published date. If there are any books remaining at this point, the program will rank them in descending order of rating percentage and display them to the user as the book they will read next. 
	

Bonus Version
add edition to book classification because 2 books may have the same title and author but they are different books 

enable the user to input multiple publishers for one book

enable the user to add or remove multiple books at once

memorize user’s library for future program use 

provide user the option to display the books from greatest rating to least rating that fall into the current classification and ask whether they want to narrow further 

rank books by Google percentage rating AND Goodreads 5-star rating in descending order 

prompt user for the author and title in one input (but then again they could put the author 1st and then the title 2nd and there could be spaces in the title)

provide user the option to randomly select a book from the library at each classification level 

for the ‘find()’ function, consolidate each classification’s code into 1 function and call this same 1 function for each classification 

create a GUI (pictures of each book with buttons to click on and fishing animations, sounds, and music)

scrape web instead of having user input the book characteristics (e.g. Wikipedia for all book characteristics: (if there are multiple genres, can just add those multiple genres to the list, and when asking the user questions, if that book has multiple genres, then as long as it matches one genre the user inputs, then show that book to the user) aside from book rating and use Google for book rating

provide user the option to import a list of books the user would like to add to or remove from their library 

add point-of-view as a book classification
