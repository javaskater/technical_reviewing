# 18 Reactvity
* I cannot test the code in the node.js REPL
* I have to create a vue project
# 19 The Lifecycle
* Three main stp
  * creating the component's HTML
  * gathering all the dynamic values
  * displayng these values (with the HTML) in the DOM
# p 20 The diagram
* Figure 2.3 see also [option Lifecycle official page](https://vuejs.org/api/options-lifecycle)
# 21
* before-mount means the template has already been compiled. It is about to be appended to the DOM
# 22
* [beforeUpdate](https://vuejs.org/api/options-lifecycle#beforeupdate): clearly explained. concerns the Ref values which depends on a values that is to be changed, the value is changed the DOM has still not been changed
  * You don't need theses lifecylces as VueJs rovides other features like computed values and watchers 
* [beforeUnmount](https://vuejs.org/api/options-lifecycle#beforeunmount) the component is still functional
  * ideal for unsubscribing to events for performance reasons (do not let subscribers when the event source does not exist anymore)