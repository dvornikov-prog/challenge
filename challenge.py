import re

def add_prefix_un(word):
  return 'un' + word

print(add_prefix_un('hello'))


def make_word_groups (words_group):
  answer = words_group[0] 
  for index in range(len(words_group)):
    if index == 0 : continue
    answer = answer + ' :: ' + words_group[0] + words_group[index]
  return answer

print(make_word_groups(['en', 'close', 'joy', 'lighten']))


def remove_suffix_ness(word):
  return word.replace('ness','')

print(remove_suffix_ness('heaviness'))

def adjective_to_verb(string, position):
  answer = ''
  string_wds = string.split()
  string_wds[position] = re.sub("[^A-Za-z]","",string_wds[position])
  string_wds[position] += 'en'
  answer = string_wds[position]
  return answer
  
print(adjective_to_verb('I need to make that bright.', -1))