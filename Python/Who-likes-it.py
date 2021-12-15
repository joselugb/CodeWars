#Who likes it? -> https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python
##You probably know the "like" system from Facebook and other pages.
##People can "like" blog posts, pictures or other items.
##We want to create the text that should be displayed next to such an item.
##
##Implement the function which takes an array containing the names of people
##that like an item. It must return the display text as shown in the examples:
##
##[]                                -->  "no one likes this"
##["Peter"]                         -->  "Peter likes this"
##["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
##["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
##["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
##
##Note: For 4 or more names, the number in "and 2 others" simply increases.

def likes(names):
    # your code here
    cadena = ""
    if (len(names) == 0):
        cadena = "no one likes this"
    elif (len(names) == 1):
        cadena = names[0]+" likes this"
    elif (len(names) == 2):
        cadena = names[0]+" and "+names[1]+" like this"
    elif (len(names) == 3):
        cadena = names[0]+", "+names[1]+" and "+names[2]+" like this"
    elif (len(names) >= 4):
        cadena = names[0]+", "+names[1]+" and "+str(len(names)-2)+" others like this"
    
    
    return cadena



##import codewars_test as test
##from solution import likes
##
##@test.it('Basic tests')
##def _():
##    test.assert_equals(likes([]), 'no one likes this')
##    test.assert_equals(likes(['Peter']), 'Peter likes this')
##    test.assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
##    test.assert_equals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
##    test.assert_equals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')
## likes(['Sylia Stingray', 'Brian J. Mason', 'Daley Wong', 'Linna Yamazaki', 'Largo', 'Macky Stingray', 'Nigel', 'Quincy Rosenkreutz', 'Galatea'])
## likes(['Priscilla S. Asagiri', 'Anri', 'Leon McNichol', 'Brian J. Mason', 'Sylia Stingray', 'Galatea', 'Quincy Rosenkreutz', 'Macky Stingray', 'Daley Wong', 'Sylvie', 'Nigel', 'Linna Yamazaki'])
## likes(['Nene Romanova', 'Nigel', 'Quincy Rosenkreutz', 'Anri', 'Sylvie', 'Linna Yamazaki', 'Largo', 'Galatea', 'Leon McNichol', 'Macky Stingray', 'Brian J. Mason', 'Priscilla S. Asagiri', 'Sylia Stingray'])
