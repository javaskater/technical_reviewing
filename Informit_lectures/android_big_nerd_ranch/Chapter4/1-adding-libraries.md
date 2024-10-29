# 70
* the two libraries to add become in *GeoQuizz\app\build.gradle.kts*
```kotlin
dependencies {
    val lifecycle_version = "2.4.1"
    val ktx_version = "1.4.0"

    implementation(libs.androidx.core.ktx)
    implementation(libs.androidx.appcompat)
    implementation(libs.material)
    implementation(libs.androidx.activity)
    implementation(libs.androidx.constraintlayout)
    implementation(libs.androidx.core.ktx) //
    implementation(libs.androidx.appcompat) //
    // ViewModel
    implementation("androidx.lifecycle:lifecycle-viewmodel-ktx:$lifecycle_version") //
    implementation("androidx.activity:activity-ktx:${ktx_version}") //
    testImplementation(libs.junit)
    androidTestImplementation(libs.androidx.junit)
    androidTestImplementation(libs.androidx.espresso.core)
}
```
* In the Grafle console File /Sync Project With Gradle File I Have a warning but Build is successull