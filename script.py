# importing regex and random libraries
import nltk
import re
import random
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer

# tokenizer = RegexpTokenizer("[\w']+")
# tokenizer.tokenize()


'''

from discord

words_you_want_to_add = ['word', 'otherWord']

alienbabble = {
    'anger_feelings_intents': r'(\bangry|\bmad|\banger|\bupset|\brage|{}\b)'.format('|\b'.join(words_you_want_to_add)),
    'good_feelings_intent': r'(okay|happy|glad|joy)',
    'bad_feelings_intent': r'(sad|tired|lonely|bad|stressed|anxious|
    'answer_why_intent': r".*\s*your face.*",
    'cubed_intent': r'.*cube.*(\d+)',
}

print(alienbabble)

'''


class TherapyBot:
    # potential negative responses
    negative_responses = ("no", "nope", "nah", "naw",
                          "not a chance", "sorry", "No", "Nope", "Nah", "Naw",)
    # keywords for exiting the conversation
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
    # random starter questions
    random_questions = (
        "Why are you here? ",
        "How have you been feeling lately? ",
        "How has your mood been? ",
        "How are you feeling? ",
        "How are you, really? ",
        "Is everything okay? ",
        "Are you okay? ",
    )

    def __init__(self):
        # import text
        text = open("my_text.txt", encoding="utf-8").read().lower()
        # store individual tokenized word
        word_tokenized_text = word_tokenize(text)
        sad_emotions_text = word_tokenized_text
        # list of sad words
        # sad_emotions_text = []
        # sad_emotions = str(sad_emotions_text)
        self.sad_emotions = []
        # tokenizer = RegexpTokenizer("[\w']+")
        # tokenizer.tokenize(sad_emotions_text)
        # add each tokenized word to array of emotions
        for word in sad_emotions_text:
            self.sad_emotions.append(word)


'''
    def filterPick(list,filter):
        return [ ( l, m.group(1) ) for l in list for m in (filter(l),) if m]

    theList = ["foo", "bar", "baz", "qurx", "bother"]
    searchRegex = re.compile('(a|r$)').search
    # x = filterPick(theList,searchRegex)
    x = filterPick(self.sad_emotions,searchRegex)

    this code is supposed do list comprehension and search for word in list and try to match reply to words

    >> [('bar', 'a'), ('baz', 'a'), ('bother', 'r')]
'''
    # print(sad_emotions)
   # print(type(sad_emotions))
   # self.alienbabble = sad_emotions_text
   # self.alienbabble = {'anger_feelings_intents': r'(\bangry|\bmad|\banger|\bupset|\brage|\b)',
   #                     'good_feelings_intent': r'(okay|happy|glad|joy)',
   #                     'bad_feelings_intent': r'(sad|tired|lonely|bad|stressed|anxious| anxiety)',
   #                     'answer_why_intent': r".*\s*your face.*",
   #                     'cubed_intent': r'.*cube.*(\d+)',
    #                         }


# Define .greet() below:
   def greet(self):
        self.name = input("What is your name? ")
        will_help = input(
            f"Hi {self.name}, I'm Martha, I'm here to help. Would you like to tell me how you're feeling? ")
        if will_help in self.negative_responses:
        print(f"Okay, I'm here if you ever want or need to talk {self.name}. ")
        return "exit"
    # if will_help in self.sad_emotions_text.items():
    #     print("test for self.sad_emotions_text")
        self.chat()
# Define .make_exit() here:

    def make_exit(self, reply):
        for words in self.exit_commands:
        if words in reply:
            print("Okay, I'm here if you need me. ")
            return True
    # Define .chat() next:

    def chat(self):
        # randomly select a question from tuple:(random_questions), ask the user, and save the user's response.
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
        reply = input(self.match_reply(reply))
        return self.anger_feelings_intents()

    def match_reply(self, reply):
        for reply in self.sad_emotions:
            found_match = re.match(string, reply)
            if found_match:
                return self.bad_feelings_intent()
        for intent, regex_pattern in self.alienbabble.items():
        found_match = re.match(regex_pattern, reply)
        if found_match and intent == 'anger_feelings_intents':
            return self.anger_feelings_intents()
        elif found_match and intent == 'answer_why_intent':
            return self.answer_why_intent()
        elif found_match and intent == 'cubed_intent':
            return self.cubed_intent(found_match.groups()[0])
        else:
            return self.no_match_intent()

  # Define .anger_feelings_intents():
    def anger_feelings_intents(self):
        responses = ("Why do you feel so angry? ", "Where do you think that anger comes from? ")
        return random.choice(responses)
  # Define .answer_why_intent():

    def answer_why_intent(self):
        responses = ("I come in peace", "I am here to collect data on your planet and it's inhabitants", "I heard the coffee is good." )
        return random.choice(response)

    def bad_feelings_intent(self):
        responses = (
            "I'm sorry to hear that, how does that make you feel?",
            "Why do you feel that way? ",
            "Hmm.. Why is that? ",
            "How long have you been feeling that way? ",
            "How does that make you feel? ",
            "How often do you feel like that? ",
            "Can you describe the feeling? ",
            "What do you think is the cause of that? ",
            "How often do you feel that way? ",
            "Hmm... Do you always feel that way? ",
            "How long have you felt that way? "
            "Why is that? ",
            "Why? ",
            "I'm sorry, to hear that, why do you feel that way? ",
        )
        return random.choice(responses)

# Define .cubed_intent():
    def cubed_intent(self, number):
        int(number)
        cubed_number = number*number*number
        print(f"The cube of {number} is {cubed_number}")
        return "Inside .cubed_intent()"

# Define .no_match_intent():
    def no_match_intent(self):
        responses = (
            "Hmm, I'm listening. ",
            "Why is that? ",
            "Why? ",
            "Are you?",
            "Hmm, that's interesting. Tell me more. ",
            "What's the root cause of that? ",
            "Why do you feel that way? ",
            "How does that make you feel? ",
            "Hmm, really? ",
            "Is that true?",
            "Are you being honest with yourself? ",
            "What do you think is the cause of that? ",
            "How often do you feel that way? ",
            "Why do you say that? ",
            "I see, I'm listening.  ",
            "Go on, I'm listening. ",
            "Why do you think that is? ",
            "I see. Why is that? ",
            "Why? ",
            "Really? ",
            "How does that make you feel? ",
        )
        return random.choice(responses)

# Create an instance of TherapyBot below:
Martha = TherapyBot("Martha")
Martha.greet()
