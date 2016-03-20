#!/usr/bin/env python

import ConfigParser
from   telegram import Updater
import logging
import pos
import nltk
from   nltk.tokenize import word_tokenize 
import sys
import markov
import time 
from   random import randint

maxStringLen = 20
debug = True 

#Create class instances
nouns = pos.Noun()
adjectives = pos.Adjective()
verbs = pos.Verb()
adverbs = pos.Adverb()
numbers = pos.Number()
pronouns = pos.Pronoun()
prepositions = pos.Preposition()
conjunctions = pos.Conjunction()
vowels = pos.Vowels()
garbage = pos.Garbage()
apologies = pos.Apologies()

def apologize(bot, update):
  bot.sendMessage(update.message.chat_id, text=apologies.getPart())

def parseMessage(bot, update):

  print "parse"
  msg = update.message.text
  msgTokens = word_tokenize(msg)
  tags = nltk.pos_tag(msgTokens)
  print "done parsing"
  print tags

  #Add parts of speech to appropriate lists.
  for t in tags:
    ltag = (t[0].lower(), t[1])
    #nltk seems to not like contractions
    #also, don't store unreasonable length strings
    if "'" in ltag[0] or len(ltag[0]) > maxStringLen or len(ltag[0]) < 3:
      continue
    elif ltag[1] in {'NN', 'NNS', 'NNP', 'NNPS'}:
      nouns.values.append(ltag)
    elif ltag[1] in {'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'}:
      verbs.values.append(ltag)
    elif ltag[1] in {'JJ', 'JJR', 'JJS'}:
      adjectives.values.append(ltag)
    elif ltag[1] in {'RB', 'RBR', 'RBS', 'WRB'}:
      adverbs.values.append(ltag)
    elif t[1] in {'CD'}:
      numbers.values.append(ltag)
    else:
      garbage.values.append(ltag)

  #If we have enough values and it's been at least 20 messages, 1/n chance of posting.
  if randint(0, 7) == 0 and len(nouns.values) > 5 and len(verbs.values) > 3 and len(adjectives.values) > 1:
    m = markov.Markov(nouns, adjectives, verbs, adverbs, numbers, pronouns, prepositions, conjunctions, vowels, garbage)
    bot.sendMessage(update.message.chat_id, text=m.string)
    nouns.values = []
    verbs.values = []
    adverbs.values = []
    garbage.values = []
    adjectives.values = []

def main():

  #Get bot token.
  Config = ConfigParser.ConfigParser()
  Config.read("./jabberwocky.cfg")

  #Create event handler
  updater = Updater(Config.get("BotApi", "Token"))

  dp = updater.dispatcher

  #Add handlers
  dp.addTelegramMessageHandler(parseMessage)
  dp.addTelegramCommandHandler("apologize", apologize)

  #Start up bot.
  updater.start_polling()

  while True: 
    if debug:
      cmd = raw_input("Enter command...\n")

      if cmd == 'list':
        print 'Nouns:'
        print nouns.values

        print 'Verbs:'
        print verbs.values

        print 'Adverbs:'
        print adverbs.values

        print 'Numbers:'
        print numbers.values

        print 'Adjectives:'
        print adjectives.values

        print 'Garbage:'
        print garbage.values

      #Force generation of a random sentence.
      elif cmd == 'forceprint':
        m = markov.Markov(nouns, adjectives, verbs, adverbs, numbers, pronouns, prepositions, conjunctions, vowels, garbage)
        print m.string

      #Shutdown bot.
      elif cmd == 'quit':
        updater.stop()
        sys.exit()

      elif cmd == 'help':
        print 'Commands are: list, forceprint, quit.'

      else:
        print 'Commmand not recognized.'

    else:
      time.sleep(1)


if __name__ == '__main__':
  main()
