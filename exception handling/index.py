try:
    getfile = open("/home/lasya/Documents/text for exception handling/Untitled Document 1","r")
    getfile.write("My file for exception handling.")
except IOError:
    print("unable to open or read the data in the file.")
else:
    print("The file was written successfully")
finally:
    getfile.close()        
