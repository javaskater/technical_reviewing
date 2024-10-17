# I hope the Device Manager 
* Is the same for all projects (Yes it is)
* [Challenges for the 4th Edition of Chapter 2](https://github.com/AxiomeCG/BigNerdRanch-Android-4th-Edition/tree/master/GeoQuiz-Chapter2-Challenge-AddListener-PreviousButton-ButtonToImageButton)
* I Window's copy the preceding Project into a new folder 
```powershell
PS C:\Users\jeanp\AndroidStudioProjects> dir


    Répertoire : C:\Users\jeanp\AndroidStudioProjects


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        22/07/2024     15:32                GeoQuizz
d-----        14/09/2024     17:39                GeoQuizzChallenge
d-----        17/10/2024     16:46                GeoQuizzChallenge Chap2 # It is the new project
d-----        29/06/2024     17:21                MyApplication
```
* I open the
* When Gradle finishes building I Get The Android View and the Run Icon activated and appearing the the MainActivity
# Challenge 1 
* Do click on the text View class for the TextView
  * the id's *question_text_view*
```xml
<TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:padding="24dp"
        android:id="@+id/question_text_view"
        android:gravity="center"
        tools:text="@string/question_australia" />
```
* Which gives on the binding partthe *questionTextView* binding attribute
```kotlin
binding.questionTextView.setOnClickListener { view ->
    currentIndex = (currentIndex + 1) % questionBank.size //easy way to loop in the question bank
    updateQuestion()
}
```
# Challenge 2
* For the second Challenge I need to Download an arrow_prev icon