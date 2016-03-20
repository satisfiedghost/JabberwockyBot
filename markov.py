import pos
from random import randint

#Indicates if last noun added was singluar.
sflag = False

#Generate a random number from 0 to top
def chance(top):
  return randint(0, top) 

#Return noun with correct article and possibly some adjectives.
def correctArticle(noun, adj):
  global sflag
  string = "" 
  
  for i in range(0, 2):
     if chance(2) == 0 and len(adj.values) > i + 1:
      string += adj.getPart()[0] + " "

  newNoun = noun.getPart()
  string += newNoun[0] + " " 
  
#If plural. Or by chance...
  if chance(3) == 0 or newNoun[1] in {'NNS', 'NNPS'}:
    string = "the " + string
  elif string[0] in pos.Vowels.values:
    string = "an " + string
  else:
    string = "a " + string

  if newNoun[1] in {'NN', 'NNP'}:
    sflag = True
  else:
    sflag = False

  return string

#Attempt to get correct pluraliztion of noun. 
def correctVerb(verb, vowels):
  global sflag
  v = verb.getPart()
  newVerb = v[0] 
  vFlag = v[1]

  if sflag and newVerb[-1:] != 's' and vFlag not in {'VBN', 'VBD'} and newVerb[-3:] != 'ing':
    if newVerb[-1:] != 'e' and newVerb[-1:] in vowels.values:
      newVerb += 'es'
    else:
      newVerb += 's'
  else:
    if newVerb[-2:] == 'es':
      newVerb = newVerb[:-2]
    elif newVerb[-1:] == 's':
      newVerb = newVerb[:-1]

  return newVerb + " "

class Markov:
  string = ""
  maxWords = 50
  punc = ['.', '!', '?']

  def __init__(self, nouns, adjectives, verbs, adverbs, numbers, pronouns, prepositions, conjunctions, vowels, garbage):
    global sflag
    self.string = ""
    if chance(1) == 1:
      self.string += nouns.getPart()[0]
    else:
      p = pronouns.getPart()
      self.string += p
      if p in {'he', 'she', 'it'}:
        sflag = True
      else:
        sflag = False

    self.string = self.string.capitalize() + " "
    self.string += correctVerb(verbs, vowels) 

    if chance(1) == 1:
      self.string += "and "
      self.string += correctVerb(verbs, vowels)  
    
    if chance(1) == 1 and len(adverbs.values) > 1:
      self.string += adverbs.getPart()[0] + " " 

    self.string += correctArticle(nouns, adjectives)

    if chance(1) == 1:
      self.string = self.string[:-1]
      self.string += self.punc[chance(2)]
      return
    
    self.string += conjunctions.getPart() + " "
    self.string += correctArticle(nouns, adjectives)
    self.string += correctVerb(verbs, vowels)

    if chance(1) == 1 and len(adverbs.values) > 1:
      self.string += adverbs.getPart()[0]
      self.string += " "

    self.string += prepositions.getPart() + " "
    self.string += correctArticle(nouns, adjectives)
    self.string = self.string[:-1]
    self.string += self.punc[chance(2)]
