# 39:
## The solutions links
* [Earlier Header Ouput](./3-HeaderOutput.md) we worked adding Google Analytics code in the header of the page
  * the [solution on GitHub](https://github.com/PacktPublishing/WordPress-Plugin-Development-Cookbook-Third-Edition/blob/main/ch2/ch2-page-header-output/ch2-page-header-output.php)
* the [solution of theis exercise is the same link only with the v2 version](https://github.com/PacktPublishing/WordPress-Plugin-Development-Cookbook-Third-Edition/blob/main/ch2/ch2-page-header-output/ch2-page-header-output-v2.php)

# 41:
* The solution uses the fact that previouly we loaded the google Analytics function ga see  [solution on GitHub](https://github.com/PacktPublishing/WordPress-Plugin-Development-Cookbook-Third-Edition/blob/main/ch2/ch2-page-header-output/ch2-page-header-output.php)
* here we add an new action on the footer (wp_footer) to add at the end of page the necessarly javascript.
## The ga Javascript
```javascript
  function recordOutboundLink( link ) {
	ga('send', 'event', 'Outbound Links', 'Click',
		link.href, {
			'transport': 'beacon',
			'hitCallback': function() { 
				document.location = link.href; 
			}
		} );
	}
```
* return false (in the href link after calling this function), makes the normal links action not to be fullfilled
  * but the hitCallback function here does the work of redirecting to the page
* transport: beacon make the request to Google Analytics to be sent through a Post verb and not through a Get verb.
* This output links analytics is useful when I want to have revenues from the websites I recommend... 