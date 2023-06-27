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

class Recipe:
   def __init__(self, ingredients, preparation_time, nutritional_information):
       self.ingredients = ingredients
       self.preparation_time = preparation_time
       self.nutritional_information = nutritional_information


   def display_recipe(self):
       print("Ingredients:", self.ingredients)
       print("Preparation Time:", self.preparation_time)
       print("Nutritional Information:", self.nutritional_information)


   def cooking_method(self):
       print("Add four glasses of water")
       print("Leave it to boil")
        print("Add two spoons of salt")
       print("Add three spoons of cooking oil")
       print("Add half a kilo of rice")
       print("Cover to simmer")




class MoroccanRecipe(Recipe):


   def display_recipe(self):


       super().display_recipe()






   def cooking_method(self):


       print("On a pre-heated pan, add two spoons of cooking oil")


       print("Add two well-sliced onions")


       print("Add five well-chopped tomatoes")


       print("Leave the tomatoes to get heated and create a paste")


       print("Add boiled rice")










class NigerianRecipe(Recipe):


   def display_recipe(self):


       super().display_recipe()






   def cooking_method(self):
        print("On a pre-heated pan, add two spoons of cooking oil")


       print("Leave it to boil")


       print("Add five well-chopped tomatoes")


       print("Leave the tomatoes to get heated and create a paste")


       print("Add boiled rice")







