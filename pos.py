from random import randint

#Superclass for parts of speech
class Partofspeech:
  values = []
  
#Return a random value from the list.
  def getPart(self):

    if len(self.values) > 0:
      index = randint(0, (len(self.values) - 1))  
      return self.values[index]
    else:
      return False 
    
#Reset values
def flush(self):
    self.values = []

#More interesting parts of speech, filled from user chat.
class Noun(Partofspeech):
  values = []

  def __init__(self):
    pass

class Verb(Partofspeech):
  values = []

  def __init__(self):
    pass


class Adverb(Partofspeech):
  values = []

  def __init__(self):
    pass


class Number(Partofspeech):
  values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

  def __init__(self):
    pass

#Holds speech values not implemented or unrecognized.
class Garbage(Partofspeech):
  values = []

  def __init__(self):
    pass

#Basic parts of speech, with little variation below.
class Pronoun(Partofspeech):
  values = ['he', 'she', 'it', 'I', 'we', 'they']

  def __init__(self):
    pass


class Preposition(Partofspeech):
  values = ['in', 'out', 'on', 'over', 'under', 'above', 'below', 'outside', 'inside',
    'around', 'from', 'after', 'adjacent', 'abreast', 'aboard', 'between', 'down', 'up',
    'near', 'like', 'via', 'astride', 'behind', 'in front of', 'across', 'of', 'onto',
    'within', 'against', 'as', 'at', 'during', 'through', 'sans', 'post', 'per', 'past',
    'except', 'beyond', 'betwixt'
    ]


  def __init__(self):
    pass

class Adjective(Partofspeech):
  values = []

  def __init__(self):
    pass

class Conjunction(Partofspeech):
  values = ['after', 'although', 'and', 'as', 'because', 'before', 'but', 'if', 'since', 'than', 'unless', 'until', 'when', 'while']
 
  def __init__(self):
    pass


class Vowels(Partofspeech):
  values = ['a', 'e', 'i', 'o', 'u']

  def __init__(self):
    pass

class Apologies(Partofspeech):
  values = ["I am very sorry.",
    "Calm down, dude. It's just a prank.",
    "My bad."]

  def __init__(self):
    pass

