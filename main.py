import re

def getString():
    userStr = input('Tell me something: \n')
    return userStr

def findTwoDigits(string):
    allMatches = re.findall('\d{2}',string)
    return allMatches

def findAlphanumeric(string):
    allMatches = re.findall('\w',string)
    return allMatches

def findWhitespace(string):
    allMatches = re.findall('\s',string)
    return allMatches

def findAnyDigit(string):
    allMatches = re.findall('\d',string)
    return allMatches

def findNonWhitespace(string):
    allMatches = re.findall('\S',string)
    return allMatches

def findComplementW(string):
    allMatches = re.findall('\W',string)
    return allMatches

def main():
    s = getString()
    print('\nfindTwoDigits',findTwoDigits(s))
    print('findAlphanumeric',findAlphanumeric(s))
    print('findWhitespace',findWhitespace(s))
    print('findAnyDigit',findAnyDigit(s))
    print('findNonWhitespace',findNonWhitespace(s))
    print('findComplementW',findComplementW(s))


main()
   




#Tell me something: 
#When I went to the store this morning at 6:55AM, I didn't notice anybody in the parking lot which was a blessing because I didn't want to walk more than 15 feet.  As luck would have it, there were about 100 people inside.  I didn't think I would have any room to walk around!  It wasn't too bad, though.  I only spent $85 dollars which was a great price, don't you think you?  By the way, you should visit https://python.org for helpful coding information!!
#
#findTwoDigits ['55', '15', '10', '85']
#findAlphanumeric ['W', 'h', 'e', 'n', 'I', 'w', 'e', 'n', 't', 't', 'o', 't', 'h', 'e', 's', 't', 'o', 'r', 'e', 't', 'h', 'i', 's', 'm', 'o', 'r', 'n', 'i', 'n', 'g', 'a', 't', '6', '5', '5', 'A', 'M', 'I', 'd', 'i', 'd', 'n', 't', 'n', 'o', 't', 'i', 'c', 'e', 'a', 'n', 'y', 'b', 'o', 'd', 'y', 'i', 'n', 't', 'h', 'e', 'p', 'a', 'r', 'k', 'i', 'n', 'g', 'l', 'o', 't', 'w', 'h', 'i', 'c', 'h', 'w', 'a', 's', 'a', 'b', 'l', 'e', 's', 's', 'i', 'n', 'g', 'b', 'e', 'c', 'a', 'u', 's', 'e', 'I', 'd', 'i', 'd', 'n', 't', 'w', 'a', 'n', 't', 't', 'o', 'w', 'a', 'l', 'k', 'm', 'o', 'r', 'e', 't', 'h', 'a', 'n', '1', '5', 'f', 'e', 'e', 't', 'A', 's', 'l', 'u', 'c', 'k', 'w', 'o', 'u', 'l', 'd', 'h', 'a', 'v', 'e', 'i', 't', 't', 'h', 'e', 'r', 'e', 'w', 'e', 'r', 'e', 'a', 'b', 'o', 'u', 't', '1', '0', '0', 'p', 'e', 'o', 'p', 'l', 'e', 'i', 'n', 's', 'i', 'd', 'e', 'I', 'd', 'i', 'd', 'n', 't', 't', 'h', 'i', 'n', 'k', 'I', 'w', 'o', 'u', 'l', 'd', 'h', 'a', 'v', 'e', 'a', 'n', 'y', 'r', 'o', 'o', 'm', 't', 'o', 'w', 'a', 'l', 'k', 'a', 'r', 'o', 'u', 'n', 'd', 'I', 't', 'w', 'a', 's', 'n', 't', 't', 'o', 'o', 'b', 'a', 'd', 't', 'h', 'o', 'u', 'g', 'h', 'I', 'o', 'n', 'l', 'y', 's', 'p', 'e', 'n', 't', '8', '5', 'd', 'o', 'l', 'l', 'a', 'r', 's', 'w', 'h', 'i', 'c', 'h', 'w', 'a', 's', 'a', 'g', 'r', 'e', 'a', 't', 'p', 'r', 'i', 'c', 'e', 'd', 'o', 'n', 't', 'y', 'o', 'u', 't', 'h', 'i', 'n', 'k', 'y', 'o', 'u', 'B', 'y', 't', 'h', 'e', 'w', 'a', 'y', 'y', 'o', 'u', 's', 'h', 'o', 'u', 'l', 'd', 'v', 'i', 's', 'i', 't', 'h', 't', 't', 'p', 's', 'p', 'y', 't', 'h', 'o', 'n', 'o', 'r', 'g', 'f', 'o', 'r', 'h', 'e', 'l', 'p', 'f', 'u', 'l', 'c', 'o', 'd', 'i', 'n', 'g', 'i', 'n', 'f', 'o', 'r', 'm', 'a', 't', 'i', 'o', 'n']
#findWhitespace [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
#findAnyDigit ['6', '5', '5', '1', '5', '1', '0', '0', '8', '5']
#findNonWhitespace ['W', 'h', 'e', 'n', 'I', 'w', 'e', 'n', 't', 't', 'o', 't', 'h', 'e', 's', 't', 'o', 'r', 'e', 't', 'h', 'i', 's', 'm', 'o', 'r', 'n', 'i', 'n', 'g', 'a', 't', '6', ':', '5', '5', 'A', 'M', ',', 'I', 'd', 'i', 'd', 'n', "'", 't', 'n', 'o', 't', 'i', 'c', 'e', 'a', 'n', 'y', 'b', 'o', 'd', 'y', 'i', 'n', 't', 'h', 'e', 'p', 'a', 'r', 'k', 'i', 'n', 'g', 'l', 'o', 't', 'w', 'h', 'i', 'c', 'h', 'w', 'a', 's', 'a', 'b', 'l', 'e', 's', 's', 'i', 'n', 'g', 'b', 'e', 'c', 'a', 'u', 's', 'e', 'I', 'd', 'i', 'd', 'n', "'", 't', 'w', 'a', 'n', 't', 't', 'o', 'w', 'a', 'l', 'k', 'm', 'o', 'r', 'e', 't', 'h', 'a', 'n', '1', '5', 'f', 'e', 'e', 't', '.', 'A', 's', 'l', 'u', 'c', 'k', 'w', 'o', 'u', 'l', 'd', 'h', 'a', 'v', 'e', 'i', 't', ',', 't', 'h', 'e', 'r', 'e', 'w', 'e', 'r', 'e', 'a', 'b', 'o', 'u', 't', '1', '0', '0', 'p', 'e', 'o', 'p', 'l', 'e', 'i', 'n', 's', 'i', 'd', 'e', '.', 'I', 'd', 'i', 'd', 'n', "'", 't', 't', 'h', 'i', 'n', 'k', 'I', 'w', 'o', 'u', 'l', 'd', 'h', 'a', 'v', 'e', 'a', 'n', 'y', 'r', 'o', 'o', 'm', 't', 'o', 'w', 'a', 'l', 'k', 'a', 'r', 'o', 'u', 'n', 'd', '!', 'I', 't', 'w', 'a', 's', 'n', "'", 't', 't', 'o', 'o', 'b', 'a', 'd', ',', 't', 'h', 'o', 'u', 'g', 'h', '.', 'I', 'o', 'n', 'l', 'y', 's', 'p', 'e', 'n', 't', '$', '8', '5', 'd', 'o', 'l', 'l', 'a', 'r', 's', 'w', 'h', 'i', 'c', 'h', 'w', 'a', 's', 'a', 'g', 'r', 'e', 'a', 't', 'p', 'r', 'i', 'c', 'e', ',', 'd', 'o', 'n', "'", 't', 'y', 'o', 'u', 't', 'h', 'i', 'n', 'k', 'y', 'o', 'u', '?', 'B', 'y', 't', 'h', 'e', 'w', 'a', 'y', ',', 'y', 'o', 'u', 's', 'h', 'o', 'u', 'l', 'd', 'v', 'i', 's', 'i', 't', 'h', 't', 't', 'p', 's', ':', '/', '/', 'p', 'y', 't', 'h', 'o', 'n', '.', 'o', 'r', 'g', 'f', 'o', 'r', 'h', 'e', 'l', 'p', 'f', 'u', 'l', 'c', 'o', 'd', 'i', 'n', 'g', 'i', 'n', 'f', 'o', 'r', 'm', 'a', 't', 'i', 'o', 'n', '!', '!']
#findComplementW [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ':', ',', ' ', ' ', "'", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', "'", ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.', ' ', ' ', ' ', ' ', ' ', ' ', ',', ' ', ' ', ' ', ' ', ' ', ' ', '.', ' ', ' ', ' ', "'", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '!', ' ', ' ', ' ', "'", ' ', ' ', ',', ' ', '.', ' ', ' ', ' ', ' ', ' ', '$', ' ', ' ', ' ', ' ', ' ', ' ', ',', ' ', "'", ' ', ' ', ' ', '?', ' ', ' ', ' ', ' ', ',', ' ', ' ', ' ', ' ', ':', '/', '/', '.', ' ', ' ', ' ', ' ', '!', '!']
