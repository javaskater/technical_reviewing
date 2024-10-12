# 45 Adding an icon in the asset subfolder
* Contrary to what is described in the Book
* Following [the Android Documentation](https://developer.android.com/studio/write/create-app-icons)
* Go to the res Folder of the Android Perspective
  * Right click
  * New / Vector Asset
  * Click Art Radio Button is selected
* the actual selected icon is a button with a lef label of **Clip art**:
  * In the search input enter *arrow right*
  * let the categories tp all
* We have now a new file *arrow_right.xml* int the existing *res/drawable/* folder 
  * (it contains by defult the application's icon also in SVG format)
# 48
* Koala (Android Studio at that time) helps a lot
  * it adds quasi automatically *xmlns:app="http://schemas.android.com/apk/res-auto"*
  * at the declaration of the LinearLayout in activity_main.xml
  * I just had to enter xml and it completes alone
* for the Button attributes Koal helps partially
  * I have to manually enter the entire left part of the = sign
  * It proposes the right part
*  Note To Myself takes the JP Mini smartphone (My LapTop has only 8 GBytes of RAM)
*  To Run the App Open MainActivity and press the Green Arrow at the right
# 49
* 1 Inch = 2.54 cm so 1dp = 1/160 * 2.54 cm = 0.1 mm
* [From Medium](https://sagar0-0.medium.com/dp-vs-sp-vs-dpi-vs-px-in-android-63cf1ac98f82)
> DP is the same as DP but it just takes care of the User system settings for Font-Sizes and 
> scales the Fonts size if the user decides to increase/decrease the Font size from settings.
