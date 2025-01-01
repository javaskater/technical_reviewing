# 32
* Here is the solution to the [Generator Filter of chapter 2](https://github.com/PacktPublishing/WordPress-Plugin-Development-Cookbook-Third-Edition/blob/main/ch2/ch2-generator-filter/ch2-generator-filter.php)

## preg_replace 
* Note the use of simple quotes and double quotes for the rexexp pattern
* same thing for the replacement string
```php
$html = preg_replace('("Wordpress.*")', '"Jean-Pierre MENA"', $html);
```
* The double quote is part of the pattern, also part of the replacement string.
## the_generator hook
* [This blog](https://weplugins.com/wordpress/how-to-use-get_the_generator_type-filter-in-wordpress/)
  * tells us that the_generator only concerns wp-head
* to have in wp_head the html (line 144 in *Twenty twenty three* theme)
```html
<meta name="generator" content="WordPress 6.7.1" />
```  
* I had to switch back to WP2023 Official Theme
## ERRATUM: Now there is no more *xhtml* but html (html 5) instead
* And it is *WordPress* (with upper P) and not *Wordpress* to be replaced (personal mistake) 
* my function becomes
```php
add_filter('the_generator', 'ch2gf_generator_filter', 10, 2);

function ch2gf_generator_filter($html, $type){
    if ($type="html"){ //html and not xhtml
        $html = preg_replace('("WordPress.*")', '"Jean-Pierre MENA"', $html); //WordPress with upper P
    }
    return $html;
}
```
# 34
* [Official list of filter hooks](https://developer.wordpress.org/apis/hooks/filter-reference/)
* find all filters in my wordpress:
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/technical_reviewing/Packt_lectures/WP_PLUGIN_DEVELOPMENT/Chap1/Docker/wordpress$ grep -rin apply_filter .
##########################################
./wp-content/plugins/akismet/class.akismet-admin.php:1097:                              $link_text = apply_filters( 'akismet_spam_check_warning_link_text', sprintf( __( 'Please check your <a href="%s">Akismet configuration</a> and contact your web host if problems persist.', 'akismet' ), esc_url( self::get_page_url() ) ) );
```
