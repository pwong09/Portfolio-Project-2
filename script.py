import utils
import sorts

pearls_bookshelf = utils.load_books('books-small.csv')

#def by_author_ascending(book_a, book_b):
#  return book_a['author_lower'] > book_b['author_lower']
#Prints list sorted by author first name A-Z
#sort_author = sorts.quicksort(pearls_bookshelf, 0, len(pearls_bookshelf) - 1, by_author_ascending)
#print("Our full list of books available today are:")
#for book in pearls_bookshelf:
#  print(book['title'] + " written by " + book['author'])

def by_rating(book_a, book_b):
    return book_a['rating'] < book_b['rating']

sort_rating = sorts.quicksort(pearls_bookshelf, 0, len(pearls_bookshelf) - 1, by_rating)

categories = []
for book in pearls_bookshelf:
    categories.append(book['category_lower'])

sort_categories = sorts.bubblesort(categories)

#Remove duplicates in sort_categories
check_categories = []
[check_categories.append(x) for x in sort_categories if x not in check_categories] 

#Prints category list sorted A-Z, no duplicates
#print(check_categories)

def check(letter, list):
    list_with_letter = [i for i in list if i.startswith(letter)]
    return list_with_letter

print("\n")
print("\n")
print("*********************")
print("****** WELCOME ******")
print("** TO *** PEARL'S ***")
print("***** BOOKSHELF *****")
print("*********************")
print("Hiya, friend!")
print("What are you looking for today?")
print("We have a variety of books in many different categories: \n")
for category in check_categories:
    print("{0}".format(category).upper())

selected_books = []
browse_category = ""
short_list = []

#User Interaction loop 
while len(selected_books) == 0:
    browse_category = str(raw_input("Type the beginning of a category you would like to browse. ")).lower()
    
    #matching category
    short_list = check(browse_category, check_categories)
    if len(short_list) == 0:
        print("We couldn't find a matching category.\n")

    elif len(short_list) == 1:
        for category in short_list:
            print(category.upper())
        select_category = str(raw_input("One category matches your search. Do you want to take a look at what's inside? (y or n): ")).lower()
        
        if select_category == 'y':
            #print books under that category
            print("\nOkay, below are the books I have under {0}: \n".format(short_list[0].upper()))
            for book in pearls_bookshelf:
                if book['category_lower'] == short_list[0]:
                    selected_books.append(book['title'] + " written by " + book['author'])
            print("Pearl's favorite book in {0} is: \n {1} \n".format(short_list[0].upper(),selected_books[0]))
            print("Followed by: \n")
            for i in selected_books[1:]:
                print("{0}\n".format(i))
    
    elif len(short_list) > 1:
        for category in short_list:
            print(category.upper())
        select_category = str(raw_input("We found a few categories that could fit your search. Give us a few more letters to narrow down what you're looking for: ")).lower()
        short_list = check(select_category, check_categories)
        for category in short_list:
            print(category.upper())
        confirm_category = str(raw_input("Is this what you're looking for? (y or n): ")).lower()

        if confirm_category == 'y':
            print("\nOkay, below are the books I have under {0}: \n".format(short_list[0].upper()))
            for book in pearls_bookshelf:
                if book['category_lower'] == short_list[0]:
                    selected_books.append(book['title'] + " written by " + book['author'])
            print("Pearl's favorite book in {0} is: \n {1} \n".format(short_list[0].upper(),selected_books[0]))
            print("Followed by: \n")
            for i in selected_books[1:]:
                print("{0}\n".format(i))
    
    repeat_loop = str(raw_input("Do you want to find other books? Enter y for yes and n for no. ")).lower()
    if repeat_loop == 'y':
        selected_books = []
        
    else:
        print("Thanks for checking out Pearl's Bookshelf. We hope to see you again soon!")
        break