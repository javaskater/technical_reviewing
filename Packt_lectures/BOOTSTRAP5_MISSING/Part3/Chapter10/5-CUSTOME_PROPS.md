# p 297

- the prefix variable corresponds to **bs-**
- in the bootstrap.scss I added

```scss
@import "root";
:root {
  --bs-primary: red;
  --bs-secondary: green;
  --bs-success: blue;
  --bs-primary-rgb: #{to-rgb(red)};
  --bs-secondary-rgb: #{to-rgb(green)};
  --bs-success-rgb: #{to-rgb(blue)};
}
```

- I gave a title a new class: **primaire**

```html
<h2 class="primaire">Colors</h2>
<ul class="timeline">
  <li class="timeline-item timeline-item-primary">
    <div class="timeline-time">2022</div>
    <p class="timeline-text">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis convallis
      velit quis sapien sollicitudin ultrices.
    </p>
  </li>
</ul>
```

- and in the style.scss

```scss
.primaire {
  color: var(--bs-primary);
}
```

- it works, the title becomes red

# pro component

- _bootstrap/scss/\_variables.scss_ we have for example for the badge

```scss
// scss-docs-start badge-variables
$badge-font-size: 0.75em !default;
$badge-font-weight: $font-weight-bold !default;
$badge-color: $white !default;
$badge-padding-y: 0.35em !default;
$badge-padding-x: 0.65em !default;
$badge-border-radius: $border-radius !default;
// scss-docs-end badge-variables
```

# p 305

- I cannot test the ratio on my workplace because
  - the proxy does not let the map thhough
    - the iframe is then a line

# 306

- rfs _bootstrap/scss/vendor/\_rfs.scss_ is an independent GitHb project developped by the Bootstrap Team
