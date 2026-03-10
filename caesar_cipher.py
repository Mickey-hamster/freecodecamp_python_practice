# This file is used to build a Caesar Cipher 
# A Caesar cipher is one of the simplest and most widely known encryption techniques 
# A type of substitution cipher in which each letter in the plaintext is replaced by a letter from some 
# fixed positions along the alphabet

def caesar(text,shift, encrypt = True):
  if not isinstance(shift, int):
    return "Shift must be an integer value."
  # if not true, return the string
  if shift <1 or shift > 25: 
    return "Shift must be an integer between 1 and 25"
    
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  shift = 5
  shifted_alphabet = alphabet[shift:] +alphabet[:shift]
# create a variable called shifted_alphabet which is made up of characters from alphabet start from position of shift
# , ended at the end of alphabet and the start of alphabet, ended at the characher before shift
  
  translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
# to create a translation table where each character in alphabet is matched to that in shifted_alphabet in the same position

  
  
