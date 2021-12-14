import utils

pearls_bookshelf = utils.load_books('books-small.csv')

print("*********************")
print("****** WELCOME ******")
print("** TO *** PEARL'S ***")
print("***** BOOKSHELF *****")

print("What are you looking for today?")
browse_category = input("Type the beginning of a category you would like to browse.")