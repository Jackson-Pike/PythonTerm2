import random
class Human(object):

    questions = ["What is 2 + 2?", "Who is the president of the United States?"]

    def __init__(self, name, hair_color, eye_color, height, weight, iq, gender, race):
        self.name = name
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.height = height
        self.weight = weight
        self.iq = iq
        self.gender = gender
        self.race = race
    def intro_self(self):
        print("Hello, my name is " + self.name)
    def describe_self(self):
        print("I have", self.hair_color, "hair.")
        print("I have", self.eye_color, "eyes.")
        print("I am", self.height, "tall.")
        print("I weigh", self.weight, "lbs. ")
        print("I am a", self.race, self.gender, "with an iq of", self.iq)
    def learn(self, questions):
        c_question = random.randrange(1, 3)
        if c_question == 1:
            question = questions[0]
            answers = [4, 3, 5, 6]








jack = Human("Jack", "Brown", "Brown", "5'6\"", "186", "100", "Male", "Caucasian")
jack.intro_self()
jack.describe_self()