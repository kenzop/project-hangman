secret_word = ""
def get_secret_word(secret_word):
  import random
  word_bank = ['apple', 'banana', 'orange', 'pear', 'mango', 'grapes']
  secret_word = random.choice(word_bank)
  return secret_word
