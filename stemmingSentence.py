import re

def stemmingSentence(contents):

  # Lower case
  contents = contents.lower()

  # Looks for any expression that starts with < and ends with > and replace
  # and does not have any < or > in the tag it with a space (' ')
  contents = re.sub('<[^<>]+>', ' ', contents);

  # Replace characters between 0-9 with 'number'
  contents = re.sub('[0-9]+', 'number', contents)


  # Replace $ sign with 'dollar'
  contents = re.sub('[$]+', 'dollar', contents)

  return re.findall("[a-zA-Z]+",contents)