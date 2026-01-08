# p 211
```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/bootstrap/scss$ grep -rin \$border-radius .
./_root.scss:59:  --#{$prefix}border-radius: #{$border-radius};
./_root.scss:60:  --#{$prefix}border-radius-sm: #{$border-radius-sm};
./_root.scss:61:  --#{$prefix}border-radius-lg: #{$border-radius-lg};
./_root.scss:62:  --#{$prefix}border-radius-xl: #{$border-radius-xl};
./_root.scss:63:  --#{$prefix}border-radius-2xl: #{$border-radius-2xl};
./_root.scss:64:  --#{$prefix}border-radius-pill: #{$border-radius-pill};
./_variables.scss:495:$border-radius:               .375rem !default;
./_variables.scss:496:$border-radius-sm:            .25rem !default;
./_variables.scss:497:$border-radius-lg:            .5rem !default;
./_variables.scss:498:$border-radius-xl:            1rem !default;
./_variables.scss:499:$border-radius-2xl:           2rem !default;
./_variables.scss:500:$border-radius-pill:          50rem !default;
./_variables.scss:776:$btn-border-radius:           $border-radius !default;
./_variables.scss:777:$btn-border-radius-sm:        $border-radius-sm !default;
./_variables.scss:778:$btn-border-radius-lg:        $border-radius-lg !default;
./_variables.scss:837:$input-border-radius:                   $border-radius !default;
./_variables.scss:838:$input-border-radius-sm:                $border-radius-sm !default;
./_variables.scss:839:$input-border-radius-lg:                $border-radius-lg !default;
./_variables.scss:1070:$nav-tabs-border-radius:            $border-radius !default;
./_variables.scss:1076:$nav-pills-border-radius:           $border-radius !default;
./_variables.scss:1140:$dropdown-border-radius:            $border-radius !default;
./_variables.scss:1197:$pagination-border-radius:          $border-radius !default;
./_variables.scss:1221:$pagination-border-radius-sm:       $border-radius-sm !default;
./_variables.scss:1222:$pagination-border-radius-lg:       $border-radius-lg !default;
./_variables.scss:1241:$card-border-radius:                $border-radius !default;
./_variables.scss:1264:$accordion-border-radius:                 $border-radius !default;
./_variables.scss:1298:$tooltip-border-radius:             $border-radius !default;
./_variables.scss:1330:$popover-border-radius:             $border-radius-lg !default;
./_variables.scss:1366:$toast-border-radius:               $border-radius !default;
./_variables.scss:1384:$badge-border-radius:               $border-radius !default;
./_variables.scss:1404:$modal-content-border-radius:       $border-radius-lg !default;
./_variables.scss:1442:$alert-border-radius:           $border-radius !default;
./_variables.scss:1458:$progress-border-radius:            $border-radius !default;
./_variables.scss:1474:$list-group-border-radius:          $border-radius !default;
./_variables.scss:1504:$thumbnail-border-radius:           $border-radius !default;
./_reboot.scss:313:  @include border-radius($border-radius-sm);
./mixins/_border-radius.scss:18:@mixin border-radius($radius: $border-radius, $fallback-border-radius: false) {
./mixins/_border-radius.scss:27:@mixin border-top-radius($radius: $border-radius) {
./mixins/_border-radius.scss:34:@mixin border-end-radius($radius: $border-radius) {
./mixins/_border-radius.scss:41:@mixin border-bottom-radius($radius: $border-radius) {
./mixins/_border-radius.scss:48:@mixin border-start-radius($radius: $border-radius) {
./mixins/_border-radius.scss:55:@mixin border-top-start-radius($radius: $border-radius) {
./mixins/_border-radius.scss:61:@mixin border-top-end-radius($radius: $border-radius) {
./mixins/_border-radius.scss:67:@mixin border-bottom-end-radius($radius: $border-radius) {
./mixins/_border-radius.scss:73:@mixin border-bottom-start-radius($radius: $border-radius) {
./mixins/_pagination.scss:4:@mixin pagination-size($padding-y, $padding-x, $font-size, $border-radius) {
./mixins/_pagination.scss:8:  --#{$prefix}pagination-border-radius: #{$border-radius};
./mixins/_buttons.scss:64:@mixin button-size($padding-y, $padding-x, $font-size, $border-radius) {
./mixins/_buttons.scss:68:  --#{$prefix}btn-border-radius: #{$border-radius};
```
# 217
* before in _variables.scss (Bootstrap) the display font_size where defined as
```scss
$display-font-sizes: (
  1: 5rem,
  2: 4.5rem,
  3: 4rem,
  4: 3.5rem,
  5: 3rem,
  6: 2.5rem
) !default;
```
* in variable_using_variables.scss we change it to
  * for that we are using $h{i}-font-size also defined in variables.scss
```scss
$display-font-sizes: (
1: $h1-font-size * 1.5,
2: $h2-font-size * 1.5,
3: $h3-font-size * 1.5,
4: $h4-font-size * 1.5,
5: $h5-font-size * 1.5,
6: $h6-font-size * 1.5
);
```
* And it is used in _type.scss (Bootstrap) as
```scss
// Type display classes
@each $display, $font-size in $display-font-sizes {
  .display-#{$display} {
    @include font-size($font-size);
    font-family: $display-font-family;
    font-style: $display-font-style;
    font-weight: $display-font-weight;
    line-height: $display-line-height;
  }
}
```