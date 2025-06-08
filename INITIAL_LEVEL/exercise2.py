# EJERCICIO 1
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.


new_filenames = []
for filename in filenames:
    if filename.endswith("hpp"):
        new_filenames.append(filename[:-3]+ "h")
    else:
        new_filenames.append(filename)

print(new_filenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]



# EJERCICIO 2
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
new_filenames = []
for filename in filenames:
    if filename.endswith("hpp"):
        new_filenames.append(filename[:-3] + "h")
    else:
        new_filenames.append(filename)


print(new_filenames) 
# Should print ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


# EJERCICIO 3
def pig_latin(text):  
  # Separate the text into words
  words = text.split()
  say = []

  for word in words:
    # Create the pig latin word and add it to the list
    pig_word = word[1:] + word[0] + "ay"
    say.append(pig_word)

    # Turn the list back into a phrase
  return " ".join(say)
    
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"


# EJERCICIO 4
def biography_list(people):
    # Iterate over each "person" in the given "people" list of tuples. 
    for person in people:

        # Separate the 3 items in each tuple into 3 variables:
        # "name", "age", and "profession"   
        name, age, profession = person


        # Format the required sentence and place the 3 variables 
        # in the correct placeholders using the .format() method.
        print("{} is {} years old and works as a {}.".format(name, age, profession))


# Call to the function:
biography_list([("Ira", 30, "a Chef"), ("Raj", 35, "a Lawyer"), ("Maria", 25, "an Engineer")])


# Click Run to submit code


# Output should match:
# Ira is 30 years old and works as a Chef.
# Raj is 35 years old and works as a Lawyer.
# Maria is 25 years old and works as an Engineer.