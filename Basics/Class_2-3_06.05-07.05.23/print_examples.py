print("Text value!")
print("One", 3.2, "Two", 7, "One more.")
# Separates the print with given value "sep="
print("Some value", "Other value", sep=", ")
# Ends the print with given value "end=" ADD \n at the end for new line.
print("Some value", "Other value", sep=", ", end=". \n")

# Formatting methods
title = "Mr."
name = "Tõnis"
# printf
print("\nprintf\nHello there, %s %s" % (title, name))
# str.format()
print("\nstr.format()\nHello there, {} {}".format(title, name))
print("Hello there, {title} {name}".format(title=title, name=name))
print("Hello there, {0} {1}".format(title, name))
# f-string
print(f"\nf-string\nHello there, {title} {name}")
