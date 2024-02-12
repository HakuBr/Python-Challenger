import re
def valid_palindrome(string):
  return re.sub('[^a-zA-Z0-9]','',string.lower()) == re.sub('[^a-zA-Z0-9]','',string.lower())[::-1]


valid_palindrome("A man, a plan, a canal: Panama")