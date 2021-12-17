import utils
import sorts
import re

pearls_bookshelf = utils.load_books('books-small.csv')

#def by_author_ascending(book_a, book_b):
#  return book_a['author_lower'] > book_b['author_lower']
#Prints list sorted by author first name A-Z
#sort_author = sorts.quicksort(pearls_bookshelf, 0, len(pearls_bookshelf) - 1, by_author_ascending)
#print("Our full list of books available today are:")
#for book in pearls_bookshelf:
#  print(book['title'] + " written by " + book['author'])

def by_rating(book_a, book_b):
    return book_a['rating'] > book_b['rating']

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


print("*********************")
print("****** WELCOME ******")
print("** TO *** PEARL'S ***")
print("***** BOOKSHELF *****")
#User Interaction loop 
print("What are you looking for today?")
selected_books = []
browse_category = ""
short_list = []

if not re.match("^[a-z]*$", browse_category):
    print("Error! Only letters a-z allowed!")

while len(selected_books) == 0:
    browse_category = str(raw_input("Type the beginning of a category you would like to browse. ")).lower()
    
    #matching category
    short_list = check(browse_category, check_categories)
    if len(short_list) == 0:
        print("We couldn't find a matching category.\n")
        select_category = str(raw_input("Type the beginning of another category you would like to browse. ")).lower()
        short_list = check(select_category, check_categories)
        print(short_list)

    elif len(short_list) == 1:
        print(short_list)
        select_category = str(raw_input("One category matches your search. Do you want to take a look at what's inside? (y or n): ")).lower()
        
        if select_category == 'y':
            #print books under that category
            print("Okay, below are the books that match {0}: ".format(short_list[0]))
            for book in pearls_bookshelf:
                if book['category_lower'] == short_list[0]:
                    selected_books.append(book['title'] + " written by " + book['author'])
            for i in selected_books:
                print("{0}\n".format(i))
    
    elif len(short_list) > 1:
        print(short_list)
        select_category = str(raw_input("We found a few categories that could fit your search. Give us a few more letters to narrow down what you're looking for: ")).lower()
        short_list = check(select_category, check_categories)
        print(short_list)
        confirm_category = str(raw_input("Is this what you're looking for? (y or n): ")).lower()

        if confirm_category == 'y':
            print("Okay, below are the books that match {0}: ".format(short_list[0]))
            for book in pearls_bookshelf:
                if book['category_lower'] == short_list[0]:
                    selected_books.append(book['title'] + " written by " + book['author'])
            for i in selected_books:
                print("{0}\n".format(i))

    
    repeat_loop = str(raw_input("Do you want to find other books? Enter y for yes and n for no. ")).lower()
    if repeat_loop == 'y':
        selected_books = []
    else:
        print("Thanks for checking out Pearl's Bookshelf. We hope to see you again soon!")
        break
        

    
   
    

#category_list = check(browse_category,check_categories)
#category_str = " ".join([str(item) for item in category_list])


#def binary_search(sorted_list, left_pointer, right_pointer, target):
#    if left_pointer >= right_pointer:
#       return 'Value not found'
#    mid_idx = (left_pointer + right_pointer) // 2
#    mid_val = sorted_list[mid_idx]
#    if mid_val == target:
#        return mid_idx
#    if mid_val > target:
#        return binary_search(sorted_list, left_pointer, mid_idx, target)
#    if mid_val < target:
#        return binary_search(sorted_list, mid_idx + 1, right_pointer, target)