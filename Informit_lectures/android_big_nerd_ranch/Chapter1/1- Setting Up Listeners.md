# 23
* The View has already been defined using the traditional Xml files (Java version)
## Implementing [SAM Interface](https://kotlinlang.org/docs/fun-interfaces.html#sam-conversions)
* We can go from:
```kotlin
//The SAM inteface
fun interface IntPredicate {
   fun accept(i: Int): Boolean
}
//Implementing the inteface
// Creating an instance of a class using the traditional method
val isEven = object : IntPredicate {
   override fun accept(i: Int): Boolean {
       return i % 2 == 0
   }
}
// Creating an instance using lambda
val isEven = IntPredicate { it % 2 == 0 }
```
## Why is the onclickListener so simple ?
* [answer 198 of this StackOverflow Post](https://stackoverflow.com/questions/44301301/android-how-to-achieve-setonclicklistener-in-kotlin)
  * are the six way to define the onclick Listner in Android/Kotlin (starts with the more abstract/functional)
```kotlin
//First Way the mos abstract see the 6th Way of doing which is very close
button.setOnClickListener {
    // Do some work here
}
//2nd Way the more complete
button.setOnClickListener(object : View.OnClickListener {//the parameters of a method are objects not class
    override fun onClick(view: View?) {
        // Do some work here
    }

})
//Thrid way
button.setOnClickListener(View.OnClickListener { view ->
    // Do some work here
})
// 4ht way A more complete
class MainActivity : AppCompatActivity(), View.OnClickListener{ //I am implemnting my self the onclik Listener
   
    lateinit var button : Button
            
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        button = findViewById(R.id.button1)
        button.setOnClickListener(this)
    }
        
    override fun onClick(view: View?) {
        when(view?.id){
            R.id.button1->{
                // do some work here
            }
        }
    }
}
//Fifth way
class MainActivity : AppCompatActivity(){

    lateinit var button : Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        button = findViewById(R.id.button1)
        button.setOnClickListener(listener)
    }
    
    val listener= View.OnClickListener { view ->
        when (view.getId()) {
            R.id.button1 -> { //When view.getId() has the value of R.id.button1 ? see the when construct in Kotlin
                // Do some work here
            }
        }
    }
}
//6th The way it is implmented in the book (very near the first way)
button.setOnClickListener { view ->         
    // Do some work here It is the SAM conversion (Lambda -> object implementing the expected interface) 
}
``` 
* first and 6th version
> Kotlin has special support for this pattern as part of its Java interoperability layer. It lets you write a
*function literal*, and it takes care of **turning that into an object implementing the interface**. This behind-
the-scenes process is called **SAM conversion**
# 25 Toasts
* Activity is a subclass of Context (an activity is a context for a running Android Application)
# 26 Running the App
* I tried the Fold but starting the Emulator freezed my computer (I have only 8GB RAM and it is on board which means welded) 
* *Tools --> Device Manager* (no more AVD)
* I take the Pixel 4 like recommended but the API 35 (the API 32 of the book has to be downloaded but a good connection is not available)
# 28 Running on the emulator
* my 8Gb Memory I cannot chack a device to run On
* on the **left side** of *app selector* I select the device to run on!!!
* * On the status bar down we see Gradle is running !!!! (takes a lot of time 3min25s)
* Waiting of all device to come online takes a lot of time (the device is already running. I don't understand why it takes that time)
* The alert message on the right has nothing to do with the reality!!!
  * 16GB would be fine !!!
## When I restart the Android Studio
* Gradle takes a lot of time to synchronize !!!
  * Gradle Building Model never stops !
* Th project is installed at  **C:\Users\jeanp\AndroidStudioProjects\GeoQuizz**
* Opening the Sync window (bottom) we see that it takes time because we are downloadinfg the Gradle sources from Internet (with my low smartphone connexion)
```
Gradle Daemon started in 1 s 537 ms
> Task :prepareKotlinBuildScriptModel UP-TO-DATE
```
* It downloads the sources of Gradle (> 4 minutes) and the different libraries we need (including the sources jars)
```
Deprecated Gradle features were used in this build, making it incompatible with Gradle 9.0.

You can use '--warning-mode all' to show the individual deprecation warnings and determine if they come from your own scripts or plugins.

For more on this, please refer to https://docs.gradle.org/8.7/userguide/command_line_interface.html#sec:command_line_warnings in the Gradle documentation.

BUILD SUCCESSFUL in 9m 7s
```