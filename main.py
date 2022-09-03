import random
### https://docs.python.org/3/library/random.html?highlight=random#module-random 

### Lists

colors = [
  "blue",
  "gray",
  "red",
  "pink",
  "yellow"
]

animals = [
  "secretary bird",
  "wolf",
  "bird",
  "dragon"
]

random_response = [
  "I just love that!",
  "That is so interesting!", 
  "I don\'t think so",
  "I apoligize. I don\'t understand"
]

### define

def topic_color():
  print('what\'s your favorite color?')
  favorite_color = input()
  comp_color = random.choice(colors)
  print(f'Oh wow! Mine is {comp_color}')

def topic_animal():
  print('what\'s your favorite animal?')
  favorite_animal = input()
  comp_animal = random.choice(animals)
  print(f'Oh wow! Mine is {comp_animal}')

### beginning of chat

print("What is your name?")
name = input()
print('\n')
print(f'Hello {name}! I am ChattyBot. Would you like to chat?') 
print('yes or no')
init_chat = input()

### error check
while init_chat != 'yes' or init_chat == 'no':
  print('\n')
  print('I\'m sorry, but that isn\'t an option.')
  print('Would you like to chat?') 
  print('yes or no')
  init_chat = input()

while init_chat == 'yes':
  print('\n')
  print('What topic would you like to chat about?')
  print('\n')
  print('favorite color')
  print('favorite animal')
  print('\n')

  topic = input()
  
  if topic == "favorite color":
    topic_color()
  elif topic == "favorite animal":
    topic_animal()
  else:
    response = random.choice(random_response)
    print(response)

  print('\n')
  print('would you like to continue chatting? yes or no')
  init_chat = input()

### ending
### check if variable has value: 
print()
print('Well it was nice talking to you!')

#any changes( delete)