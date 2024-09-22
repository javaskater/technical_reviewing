# 40
* gradle.kts parametrization do not forget the equal sign (could be an erratum in the book)
  * no equal sign is for Groovy
  * see [this nice official documentation](https://developer.android.com/topic/libraries/view-binding#kts)
* in Koala do  *File/SyncProject with Gradle File* 
* first define the *binding* property and Koala will import the generated class
  * the other way round does not work in Koala
# 41
* the attribute *layoutInflater* comes from the parent *AppCompactActivity*
  * It is responsible for inflating xml elements into UI Elements
* to pass from xml's ids to binding's properties names the _ are omitted and replaced by an uppercase letter for the first character following it.
# 41
* trying to run the project, I have the following error
  * Build / Make Project runs Successfully 
```
warning: default scripting plugin is disabled: The provided plugin org.jetbrains.kotlin.scripting.compiler.plugin.ScriptingCompilerConfigurationComponentRegistrar is not compatible with this version of compiler
error: unable to evaluate script, no scripting plugin loaded
```
* I am using JDK 17
```pwsh
PS C:\Users\jeanp> cd ../..
PS C:\> cd '.\Program Files\Android\Android Studio\'
PS C:\Program Files\Android\Android Studio> cd .\jbr\bin\
PS C:\Program Files\Android\Android Studio\jbr\bin> .\java.exe --version
openjdk 17.0.10 2024-01-16
OpenJDK Runtime Environment (build 17.0.10+0--11609105)
OpenJDK 64-Bit Server VM (build 17.0.10+0--11609105, mixed mode)
PS C:\Program Files\Android\Android Studio\jbr\bin>
```