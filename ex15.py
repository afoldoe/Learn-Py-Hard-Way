from sys import argv

script, filename = argv

#open() opens a file 
txt = open(filename)

print "Here's your file %r:" % filename
#read() to read the file's contents'
print txt.read()
#you should always close files after you open them
txt.close()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()