import settings 

#TIME_DICTIONARY

files = open("settings.py", "w")




for i in range(101):
    data = """
TIME_DICTIONARY  = {
    "Time":%d
}
""" % i
    
files.write(data)
files.close() 

print settings.TIME_DICTIONARY["Time"]
