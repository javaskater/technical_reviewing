# 32
* For the Challenge copy the folder of your Project to *${My Project}-Challenge* using your OS Copy Tool
* Open *${My Project}-Challenge* in Android Studio (File/Open...)
  * It takes some time for you to get  the Android view because behind the scene Android Studio / Gradle are rebuilding the Project as Android Project 
## SnackBar instead of Toaster
* [Digital Ocean link to SnackBar](https://www.digitalocean.com/community/tutorials/android-snackbar-example-tutorial)
  * which makes me ask what a [Coordinator LAyout](https://www.digitalocean.com/community/tutorials/android-coordinatorlayout) is 
  * [link download the example project](https://journaldev.nyc3.cdn.digitaloceanspaces.com/android/SnackBar.zip)
### Using the [example after dezipping it](https://journaldev.nyc3.cdn.digitaloceanspaces.com/android/SnackBar.zip)
* the coordinator Layout is at the root of the application layout
```xml
<?xml version="1.0" encoding="utf-8"?>
<android.support.design.widget.CoordinatorLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:fitsSystemWindows="true"
    android:id="@+id/coordinatorLayout"
    tools:context="com.journaldev.snackbar.MainActivity">
```
* The *coordinatorLayout* id makes it easy to access to the root element of the MainActivity's LAuout
* the content_main.xml layout in included inside the *Coordinator Layout*
  * and can be accessed through its ID (which is *layout*) like any button
  * * it is a RElativeLayout containing the 3 buttons
```xml
<include layout="@layout/content_main"
        android:id="@+id/layout"/>
```
* The button **one** just makes the SnackBar shows a simple message
* The button **two** creates a Snckbar whose *UNDO* button just calls another Snackbar.
  * you can call show independently of Make
  * more about the [SnackBar setAction method](https://developer.android.com/develop/ui/views/notifications/snackbar/action)
* The button **three** starts SnacBar with a *RETRY* button which does nothing
  * but we learn how to access to the elements inside the SnacBar (The SnackBar View)
  * just here to change SnackBar's text color to yellow.
### back to the challenge
* In the Challenge we do only the thing *button one* does 
* [playing with String Resources](https://developer.android.com/guide/topics/resources/string-resource) to retrieve the String from the StringID because contrary to Toast SnackBars use real strings
* Running the Device. Don't forget to push the TopLeft Power On Button (just above left of the device). Otherwise the device will be still Off
* Uou have at the top right a windows icon that makes your device appear in a separate window.
* Don't forget the Zoom In and Zoom out button at the right of your device !
### Extends the Challenge
* Find the LogCat window in the Android Studio and write Logs on button clics 
* [How to view Logs with LogCat](https://developer.android.com/studio/debug/logcat)
  * Wiev / ToolWindows / LogCat (Cat's face)
  * or directly the *Cat's face* on down left side
  * proposes by defaut the *package:com.bignerdranch.android.geoquizz* filter
  * the link above explains how to filter
  * filtering by package is not sufficient adding the TAG is better (usefullness of the Tag)
    * which gives *package:com.bignerdranch.android.geoquizz & tag:AWESOME_APP*
* How to write logs on android
  * see [answers 10 and 7 of this StackOverflow Post](https://stackoverflow.com/questions/2364811/how-do-i-write-outputs-to-the-log-in-android)
* It is also useful to think of [String Templates in Kotlin](https://kotlinlang.org/docs/strings.html#string-templates)
### Also how to stop the emulator
* I switched off the device but it does not stop the emulator and my computer is hot
* I go to the device manager icon at the upper right bar.
  * I see my emulator running the button is red to allow me to stop it !!! 