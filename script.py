import pyshorteners

url = input("Enter your URL: ")

shortener = pyshorteners.Shortener()

shortened = shortener.tinyurl.short(url)

print(shortened)