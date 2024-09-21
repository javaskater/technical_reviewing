# 34
* [@StrinRes](https://developer.android.com/reference/kotlin/androidx/annotation/StringRes) just tells us that the integer param is in fact a pointer to a String Resource see *res/values/strings.xml*
  * It helps the compiler determines that false String Resources ID are allocated to the resource.
  * It helps the developper while reading the code
* [Data classes](https://kotlinlang.org/docs/data-classes.html) is a kotlin notion for classes which are here only to contain data
  * that makes it easier to automatically define a set of methods like 
  * equals, hashcode, toString, component1, component2, ..., copy
* interesting notion: models are classes that contain the data that the UI will display (MVVM architecture)
# 35
* the Figure 2.3 is interesting
  * the main activity has only an index (the indice of the current Question in the Question Array so called here *Question Bank*)
# 36
* Figure  2.4 is an interesting way to capture the Layout. (Two Linear Layouts the Yes/No Button Layout is embedded in the main layout)
* Koala knows that you have to add the namespace *xmlns:tools* it knows the url for you
* When it does not find the String ressource, Koala (Android Studio) shows the String id instead (effects of tools:text)
* the activity_main display the true text in Gray when you pass a mouse on top of it it explains where all comes from (which String Resource)
# 39
* *listOf* is very practical to create an ArrayList/List of ordered elements
* the variable name *questionBank* is explicit enough
* In Kotlin the constructor is a method and as such creating an object is just like calling the constructor method
# 40
* view binding is very interesting the [official page](https://developer.android.com/topic/libraries/view-binding)
  * links to [Github sample code](https://github.com/android/architecture-components-samples/tree/main/ViewBindingSample)
  * a [Medium long post](https://medium.com/androiddevelopers/use-view-binding-to-replace-findviewbyid-c83942471fc)