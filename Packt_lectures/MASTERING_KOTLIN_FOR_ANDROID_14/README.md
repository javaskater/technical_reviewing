# The Book 
* Written in 2024 about one of the latest version of Android.
* The Packt Link [Mastering Kotlin for Android 14: Build powerful Android apps from scratch using Jetpack libraries and Jetpack Compose ](https://www.packtpub.com/en-us/product/mastering-kotlin-for-android-14-9781837631131)
# The [example code on GitHub](https://github.com/PacktPublishing/Mastering-Kotlin-for-Android)
* All the [Book's code is on Github](https://github.com/PacktPublishing/Mastering-Kotlin-for-Android)
# Gradle Behind a corporate proxy
* evertything happens in *~/IdeaProjects/chpaterone/gradle.properties*
## gradle.properties at the root of my project
* For the Chapter One testing a simple Main.kt application Gradle needs to download everything (ktolin and its standard libraries)
* I had to add the Corporate proxy 
  * Proxy's hostname  proxy.mycompany.mydomain for example adjust it to your company's proxy's host
    * if the proxy's url starts with *http://* just skip that part
  * Proxy's port in my case 3128 adjust it to your company's proxy's port
    * I made a mistake I wrote 3125 instead of 3128 and nothing worked 
```bash
kotlin.code.style=official

systemProp.http.proxyHost=proxy.mycompany.mydomain # the hostname is without http 
systemProp.http.proxyPort=3128 # Be careful in my case it is 3128 and not 3125 
systemProp.http.nonProxyHosts=localhost|127.0.0.1|.mydomain|.myotherdomain
systemProp.https.proxyHost=proxy.mycompany.mydomain # the hostname is without http 
systemProp.https.proxyPort=3128 # Be careful in my case it is 3128 and not 3125
systemProp.https.nonProxyHosts=localhost|127.0.0.1|.mydomain|.myotherdomain
```






