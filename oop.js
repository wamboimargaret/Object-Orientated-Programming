class Story {
    constructor(title, length, moralLesson, ageGroup) {
      this.title = title;
      this.length = length;
      this.moralLesson = moralLesson;
      this.ageGroup = ageGroup;
    }
    displayDetails() {
      console.log(`Title: ${this.title}`);
      console.log(`Length: ${this.length}`);
      console.log(`Moral Lesson: ${this.moralLesson}`);
      console.log(`Age Group: ${this.ageGroup}`);
    }
     tellStory(storyTeller) {
      console.log(`${storyTeller.name} is telling a story in ${storyTeller.language}:`);
      this.displayDetails();
    }
}


class Translator extends Story {
    constructor(title, length, moralLesson, ageGroup, name, language, targetLanguage) {
      super(title, length, moralLesson, ageGroup);
      this.name = name;
      this.language = language;
      this.targetLanguage = targetLanguage;
    }



   translateAndTell() {
  console.log(`${this.name} is translating and telling a story in ${this.targetLanguage}:`);
 
  const translatedStory = new Story(this.title, this.length, this.moralLesson, this.ageGroup);
  console.log(`Translated Story:`);
  translatedStory.displayDetails();

}
} 
const story1 = new Story("The Lion and the Mouse", "Short", "Helping others is important", "Children");
const story2 = new Story("The Tortoise and the Hare", "Medium", "Slow and steady wins the race", "Children");


const translator1 = new Translator("The Lion and the Mouse", "Short", "Helping others is important", "Children", "Emma", "English", "French");
const translator2 = new Translator("The Tortoise and the Hare", "Medium", "Slow and steady wins the race", "Children", "Luis", "Spanish", "English");


story1.tellStory({ name: "John", language: "English" });
story2.tellStory({ name: "Maria", language: "Spanish" });


translator1.translateAndTell();
translator2.translateAndTell(); 

//  Question 2
class Recepie{
 constructor(ingredients,preparationTime,nutritionalInformation){
   this.ingredients= ingredients;
   this.preparationTime= preparationTime;
   this.nutritionalInformation=nutritionalInformation
 }
 cookingMethod(){
   console.log("Add  four glasses of water")
   console.log("Leave it to boil")
   console.log("Add two spoon of salt ")
   console.log("Add three spoons of cooking oil ")
   console.log("Add half a kilo of rice ")
   console.log("Cover to simmer ")


 }
 }
 class MoroccanRecpie extends Recepie{
    constructor (ingredients, preperationTime)
    {
     super(ingredients, preperationTime );
    }
   displayRecipie(){
     super.displayRecipie()
   }
   cookingMethod(){
     super.cookingMethod()
   }


  }


  class Nigerian extends Recepie{
   constructor (ingredients, preperationTime)
   {
    super(ingredients, preperationTime );
   }
  displayRecipie(){
    super.displayRecipie()
  }
  cookingMethod(){
    super.cookingMethod()
  }


 }
  
 
  
  let receipe1 = new Recepie('tomatoes','3 hours')
   receipe1.cookingMethod()
   console.log(receipe1.ingredients)
   let receipe2=new MoroccanRecpie("Tomatoes","6 hours")
   receipe2.cookingMethod()
   console.log(receipe2.ingredients)


