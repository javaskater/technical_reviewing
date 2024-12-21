# 24
* creating the structure
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/technical_reviewing/Packt_lectures/WP_PLUGIN_DEVELOPMENT/Chap1/Docker$ mkdir wordpress/wp-content/plugins/ch2-page-header-output
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/technical_reviewing/Packt_lectures/WP_PLUGIN_DEVELOPMENT/Chap1/Docker$ touch wordpress/wp-content/plugins/
ch2-page-header-output/ch2-page-header-output.php
```
* see the code on [the accompanying GitHub repository](https://github.com/PacktPublishing/WordPress-Plugin-Development-Cookbook-Third-Edition/blob/main/ch2/ch2-page-header-output/ch2-page-header-output.php)
  * don't forget the comment header, otherwise you won't be have access to the plugin admin
* Note that when you want in php to write output without using *echo* just put it outside of php code **?> <script> xxxxxx </script> <?php**
## I see the script in the <head> part
```html
<script> <!-- The script brought by the plugin -->
		(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;
		i[r]=i[r]||function(){
		(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();
		a=s.createElement(o),
		m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;
		m.parentNode.insertBefore(a,m)})(window,document,'script',
		'https://www.google-analytics.com/analytics.js','ga');


		ga( 'create', 'UA-0000000-0', 'auto' );
		ga( 'send', 'pageview' );
	</script>

<script type="importmap" id="wp-importmap">
{"imports":{"@wordpress\/interactivity":"http:\/\/localhost:8080\/wp-includes\/js\/dist\/script-modules\/interactivity\/index.min.js?ver=06b8f695ef48ab2d9277"}}
</script>
<script type="module" src="http://localhost:8080/wp-includes/js/dist/script-modules/block-library/navigation/view.min.js?ver=8ff192874fc8910a284c" id="@wordpress/block-library/navigation/view-js-module"></script>
<link rel="modulepreload" href="http://localhost:8080/wp-includes/js/dist/script-modules/interactivity/index.min.js?ver=06b8f695ef48ab2d9277" id="@wordpress/interactivity-js-modulepreload"><style class='wp-fonts-local'>
@font-face{font-family:Manrope;font-style:normal;font-weight:200 800;font-display:fallback;src:url('http://localhost:8080/wp-content/themes/twentytwentyfive/assets/fonts/manrope/Manrope-VariableFont_wght.woff2') format('woff2');}
@font-face{font-family:"Fira Code";font-style:normal;font-weight:300 700;font-display:fallback;src:url('http://localhost:8080/wp-content/themes/twentytwentyfive/assets/fonts/fira-code/FiraCode-VariableFont_wght.woff2') format('woff2');}
</style>
</head>
```
# 27
* [Action plogin reference](https://developer.wordpress.org/apis/hooks/action-reference/)
# 28
* finding the 2700 hooks in the Wordpress Code
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/technical_reviewing/Packt_lectures/WP_PLUGIN_DEVELOPMENT/Chap1/Docker/wordpress$ grep -Rin 'do_action' .
# 2700 hooks
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/technical_reviewing/Packt_lectures/WP_PLUGIN_DEVELOPMENT/Chap1/Docker/wordpress$ egrep -Rin "do_action\( 'wp_head' \)" .
./wp-includes/general-template.php:3064:        do_action( 'wp_head' );
```