# 1.**Ancestral Stories:** In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that
# records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think about how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.


class Story:
   def __init__(self, title, length, moralLesson, ageGroup):
       self.title = title
       self.length = length
       self.moralLesson = moralLesson
       self.ageGroup = ageGroup


   def displayDetails(self):
       print(f"Title: {self.title}")
       print(f"Length: {self.length}")
       print(f"Moral Lesson: {self.moralLesson}")
       print(f"Age Group: {self.ageGroup}")


   def tellStory(self, storyTeller):
       print(f"{storyTeller.name} is telling a story in {storyTeller.language}:")
       self.displayDetails()




class Translator(Story):
   def __init__(self, title, length, moralLesson, ageGroup, name, language, targetLanguage):
       super().__init__(title, length, moralLesson, ageGroup)
       self.name = name
       self.language = language
       self.targetLanguage = targetLanguage


   def translateAndTell(self):
       print(f"{self.name} is translating and telling a story in {self.targetLanguage}:")
       translatedStory = Story(self.title, self.length, self.moralLesson, self.ageGroup)
       print("Translated Story:")
       translatedStory.displayDetails()


story1 = Story("The Lion and the Mouse", "Short", "Helping others is important", "Children")
story2 = Story("The Tortoise and the Hare", "Medium", "Slow and steady wins the race", "Children")


translator1 = Translator("The Lion and the Mouse", "Short", "Helping others is important", "Children", "Emma", "English", "French")
translator2 = Translator("The Tortoise and the Hare", "Medium", "Slow and steady wins the race", "Children", "Luis", "Spanish", "English")


translator1.translateAndTell()
translator2.translateAndTell()

