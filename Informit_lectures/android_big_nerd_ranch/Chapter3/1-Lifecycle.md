# If I rotate
* The actual currentIndex goes back to 0
* The Figure 3.3 p 55 is very interesting
  * using dotted border we can differentiate between
    * In Memory
    * In Memory and partially visible
    * In Memory and in the Foreground (user interacting with the Activity)
  * The table 3.1 is a good summary  (p 56)
## 56
* [dialog themed activity](https://developer.android.com/develop/ui/views/components/dialogs)
  * means an activity that is a dialog Box
  * It does not occupate the entire screen
  * so the other activity is started but not resumed
## Logging p 57
* Use The filter is *package:com.bignerdranch.android.geoquizz & tag:AWESOME_APP*
  * see [part 2 of Chapter 1](../Chapter2/2-DataBinding.md) 
## p 58
* the hook function are called in the order of the Lifecycle
  * onCreate
  * onStart
  * onResume
  * onPause
  * onStop
  * onDestroy
* it is only onCreate which takes on or two parameters