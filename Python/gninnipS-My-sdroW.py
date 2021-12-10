##https://www.codewars.com/kata/5264d2b162488dc400000001/train/python

##Write a function that takes in a string of one or more words,
##and returns the same string, but with all five or more letter words
##reversed (Just like the name of this Kata).
##Strings passed in will consist of only letters and spaces.
##Spaces will be included only when more than one word is present.
##
##Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
##spin_words( "This is a test") => returns "This is a test"
##spin_words( "This is another test" )=> returns "This is rehtona test"
##spin_words("Welcome")
##spin_words("to")
##spin_words("CodeWars")
##spin_words("Hey fellow warriors")
##spin_words("This sentence is a sentence")

def spin_words(sentence):
    cc = 0    
    auxlista = []
    lista = sentence.split()    
    for salida in lista:
        if (len(salida) >= 5):
            auxcad =""
            for i in reversed(range(len(salida))):
                auxcad+=salida[i]
            auxlista.append(auxcad)
        else:
            auxlista.append(salida)
    listacambiada = ' '.join(auxlista)

    return listacambiada

##Solucion mas sencilla
##def spin_words(sentence):
##    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
























##import codewars_test as test
##from solution import spin_words
##
##@test.describe("Stop gninnipS My sdroW!")
##def fixed_tests():
##    @test.it("Single word")
##    def _():
##        test.assert_equals(spin_words("Welcome"), "emocleW")
##        test.assert_equals(spin_words("to"), "to")
##        test.assert_equals(spin_words("CodeWars"), "sraWedoC")
##
##    @test.it("Multiple words")
##    def _():
##        test.assert_equals(spin_words("Hey fellow warriors"), "Hey wollef sroirraw")
##        test.assert_equals(spin_words("This sentence is a sentence"), "This ecnetnes is a ecnetnes")
