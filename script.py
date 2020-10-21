import pyshorteners

'''
['adfly', 'bitly', 'chilpit', 'clckru', 'cuttly', 
'dagd', 'gitio', 'isgd', 'nullpointer', 'osdb', 
'owly', 'post', 'qpsru', 'shortcm', 'tinycc', 'tinyurl']
'''

url = input("Enter your URL: ")
# https://github.com/aa-ag
# https://3.141592653589793238462643383279502884197169399375105820974944592.eu/
# https://iamtheproudownerofthelongestlongestlongestdomainnameinthisworld.com/
# http://thelongestdomainnameintheworldandthensomeandthensomemoreandmore.com/

shortener = pyshorteners.Shortener()

shortened = shortener.osdb.short(url)

print("\n", shortened)

# expanded = shortener.osdb.expand('http://osdb.link/TEST')

# print(expanded)