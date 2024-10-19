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
* To see in LogCat the diffrent states, I put the following Filter: *package:com.bignerdranch.android.geoquizz & tag:MainActivity & level:debug*
# 59
* To store the LogCat Filters ? I don't find the Menu in Koala (Android Studio at that time)
  * I find a star at the top right of the LogCat Window
  * [more on the LogCat Query Parameters](https://developer.android.com/studio/debug/logcat#key-value-search)
  * on the right of the filter input zone you can star your actual filter to find it in your favorites
  * on the left of the filter input zone the funnel icon let you access your filter history with as firsts the filter you put in your favorites
# 61
* Above The Emulator Screen you have a simulation of the Back (left arrow), Home (circle)  and Recents (square) Buttons
* I am working on Visual Studio Code on WSL + Koala (Android Studio with Emulator on) 8GB RAM are not sufficients
# 65
* When rotating the Device destroy the Activity and recreates it because it has to find if there is a correponding Layout or what configiration to adapt
