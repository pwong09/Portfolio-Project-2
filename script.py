import utils
import sorts

pearls_bookshelf = utils.load_books('books-small.csv')

print("*********************")
print("****** WELCOME ******")
print("** TO *** PEARL'S ***")
print("***** BOOKSHELF *****")

#def by_author_ascending(book_a, book_b):
#  return book_a['author_lower'] > book_b['author_lower']

def by_rating(book_a, book_b):
    return book_a['rating'] > book_b['rating']


#Prints list sorted by author first name A-Z
#sort_author = sorts.quicksort(pearls_bookshelf, 0, len(pearls_bookshelf) - 1, by_author_ascending)
#print("Our full list of books available today are:")
#for book in pearls_bookshelf:
#  print(book['title'] + " written by " + book['author'])

sort_rating = sorts.quicksort(pearls_bookshelf, 0, len(pearls_bookshelf) - 1, by_rating)

categories = []

for book in pearls_bookshelf:
    categories.append(book['category_lower'])

sort_categories = sorts.bubblesort(categories)

#Prints category list sorted A-Z
#print(sort_categories)

#Remove duplicates in sort_categories
check_categories = []
[check_categories.append(x) for x in sort_categories if x not in check_categories] 
print(check_categories)

def check(letter, list):
    list_with_letter = [i for i in list if i.startswith(letter)]
    return list_with_letter

   

print("What are you looking for today?")
browse_category = raw_input("Type the beginning of a category you would like to browse. ")


print(check(browse_category,check_categories))

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




