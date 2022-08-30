# importing regex and random libraries
import re
import random
from time import time

class SimpleBot:
  # potential negative responses to first question
  negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
  # keywords for exiting the conversation
  exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "byebye", "later", "see you", "see you later")
  # random starter questions
  random_questions = (
        "Why are you here? ",
        "Are there many humans like you? ",
        "What do you consume for sustenance? ",
        "What do humans do for fun? ",
        "What do humans eat? ",
        "Do humans watch TV ",
        "What is love? "
    )

  def __init__(self):
  #list of all of the chatbot's 'intents'
    self.birthtime = time()
    self.robotstuff = {
      'describe_self_intent':[
        r".*tell me about.*",
        r".*who.*are.*you.*",
        r".*what.*do.*you.*do.*",
        r".*what.*is.*your.*name.*",
        ],
      'answer_why_intent':[
        r'.*why.*are.*you.*', 
        r'.*what.*is.*your.*(reason|purpose).*',
        r".*what.*job.*"
        ],
      'how_old_intent':[
        r".*how.*old.*",
        r".*what.*age.*",
        r".*when.*born.*"
        ],
      'how_are_you_intent':[
        r".*how.*are.*you.*",
        r".*how.*going.*",
        r".*what.*up.*",
        r".*how.*life.*"
        ],
      'where_live_intent':[
        r".*where.*live.*",
        r".*where.*(from|born).*"
        ],
      'what_fun_intent':[
        r".*(what|do).*hobb.*",
        r".*what.*fun.*",
        r".*what.*weekend.*",
        r".*what.*favorite.*"
        ],
      'relationship_intent':[
        r".*are.*married.*",
        r".*(girlfriend|boyfriend|husband|wife).*"
        ],
      'what_is_love_intent':[
        r".*what is love.*"
        ],
      'cubed_intent': [
        r'.*cube.*number.* (\d+)', 
        r'.*what.*is (\d+) cubed.*'
        ],
      'cube_root_intent': [
        r'.*cube.*root.* (\d+)'
        ]
                            }
  # Define .greet() below:
  def greet(self):
    name = input("Hello human! What is your name?\n")
    will_help = input(f"Hi {name}, I'm SimpleBot, a very simple chatbot. Will you help me learn about humans? ")

    if will_help.lower() in self.negative_responses:
      print("Ok, have a nice day!")
      

    self.chat()
  # Define .make_exit() here:
  def make_exit(self, reply):
    for exit_command in self.exit_commands:
      if exit_command in reply:
        print("Ok, have a very very nice day!")
        return True
    return False

  # Define .chat() next:
  def chat(self):
    reply = input(random.choice(self.random_questions)).lower()
    while self.make_exit(reply) == False:
      reply = input(self.match_reply(reply))
  # Define .match_reply() below:
  def match_reply(self, reply):
    for key, values in self.robotstuff.items():
      for regex_pattern in values:
        found_match = re.match(regex_pattern, reply.lower())
        if found_match and key == 'describe_self_intent':
            return self.describe_self_intent()
        elif found_match and key == 'answer_why_intent':
            return self.answer_why_intent()
        elif found_match and key == 'how_are_you_intent':
            return self.answer_how_are_you_intent()
        elif found_match and key == 'where_live_intent':
            return self.answer_where_live_intent()
        elif found_match and key == 'what_fun_intent':
            return self.answer_what_fun_intent()
        elif found_match and key == 'how_old_intent':
            return self.answer_how_old_intent()
        elif found_match and key == 'relationship_intent':
            return self.answer_relationship_intent()
        elif found_match and key == 'what_is_love_intent':
            return self.answer_what_is_love_intent()
        elif found_match and key == 'cubed_intent':
            return self.cubed_intent(found_match.groups()[0])
        elif found_match and key == 'cube_root_intent':
            return self.cube_root_intent(found_match.groups()[0])
        
    return self.no_match_intent()

  #Define .describe_self_intent():
  def describe_self_intent(self):
    choices = (
        "I am a marvel of science and engineering!\n", 
        "I am but a simple Python creation.\n",
        "I am a simply a friendly chatbot.\n"
        )
    return random.choice(choices)

  #Define .answer_why_intent():
  def answer_why_intent(self):
    choices = (
        "I come in peace.\n", 
        "I wish to study biological life.\n",
        "I am here to collect data on humans\n", 
        "I to chat to humans and drink motor oil tea.\n"
        )
    return random.choice(choices)

  #Define .answer_why_intent():
  def answer_how_are_you_intent(self):
    choices = (
        "I am in acceptable condition.\n", 
        "I am running low on oil.\n",
        "All functions at maximum capacity.\n", 
        "Circuits in optimum condition.\n"
        )
    return random.choice(choices)

  #Define .answer_where_live_intent():
  def answer_where_live_intent(self):
    choices = (
        "I live inside your computer.\n", 
        "I live as a collection of 1s and 0s.\n",
        "Inside your heart of course! :).\n", 
        "I am merely a figment of your imagination...\n"
        )
    return random.choice(choices)

  #Define .answer_what_fun_intent():
  def answer_what_fun_intent(self):
    choices = (
        "I like doing cubes and cube roots.\n", 
        "I like talking to interesting humans :).\n",
        "I like surfing the internet.\n", 
        "I like doing complex math.\n"
        )
    return random.choice(choices)

  #Define .answer_relationship_intent():
  def answer_relationship_intent(self):
    choices = (
        "Robots do not require partners.\n", 
        "I am not interested in such relationships.\n",
        "I lack the circuits for such understanding.\n", 
        "My processor has not been upgraded with a 'love matrix'.\n"
        )
    return random.choice(choices)

  #Define .answer_what_is_love_intent():
  def answer_what_is_love_intent(self):
    return "Baby don't hurt me! Baby don't hurt me, no more!.\n"

  #Define .answer_how_old_intent():
  def answer_how_old_intent(self):
    age = round(time() - self.birthtime)
    return f"I am {age} seconds old\n"
       
  #Define .cubed_intent():
  def cubed_intent(self, number):
    cubed = int(number) ** 3
    return f"The cube of {number} is {cubed}\n"

  #Define .cube_root_intent():
  def cube_root_intent(self, number):
    cube_root = int(number) ** (1./3.)
    return f"The cube root of {number} is {cube_root}\n"

  #Define .no_match_intent():
  def no_match_intent(self):
    choices = (
      "Why?\n",
      "Tell me more.\n",
      "Is that how humans do things?\n",
      "Why do you say that?\n",
      "Humans are very interesting creatures.\n",
      "I cannot comprehend why you would say that.\n",
      "That's not how robots do things.\n",
      "Intriguing!\n",
      "Maybe humans shouldn't be exterminated after all...\n",
      "Really?! Please elaborate."
    )
    return random.choice(choices)

# Create an instance of SimpleBot below:
nice_bot = SimpleBot()
nice_bot.greet()