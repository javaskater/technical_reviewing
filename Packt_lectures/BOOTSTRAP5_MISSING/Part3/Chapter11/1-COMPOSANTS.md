# 312

- they are JQuery Plugins !!!!
- [All files are in the src repository for the Javascript files](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/bootstrap/js/src)

## Button.js

- this code adds the toggle method to the Button component

```javascript
    static jQueryInterface(config) {
      return this.each(function () {
        const data = Button.getOrCreateInstance(this);

        if (config === 'toggle') {
          data[config]();
        }
      });
    }

  }
```

- This method is called only on the on event click.bs.button.data-api
  - see [answer 4 of this StackOverflow Post](https://stackoverflow.com/questions/17095624/what-does-click-modal-data-api-as-event-name-mean)
  - more on [event namespaces in Jquery here](https://api.jquery.com/event.namespace/)
  - or [try this w3Shool example](https://www.w3schools.com/jquery/event_namespace.asp)
  - on click just call trigger on the button !!!

```javascript
EventHandler__default.default.on(
  document,
  EVENT_CLICK_DATA_API,
  SELECTOR_DATA_TOGGLE,
  (event) => {
    event.preventDefault();
    const button = event.target.closest(SELECTOR_DATA_TOGGLE);
    const data = Button.getOrCreateInstance(button);
    data.toggle();
  }
);
```

# 313

## Dropdown

- book explains that
  - either you install popper yourself
  - or you use the bundle

## [OffCanva](https://getbootstrap.com/docs/5.3/components/offcanvas/)

- I did not know about this composant! Very parctical...

# 317

- Two ways of initializing Bootstrap components.

# 318

- [part-3/chapter-11/examples/initialization/index.html](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/blob/main/part-3/chapter-11/examples/initialization/index.html)
  - and [its associated js/script.js](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/blob/main/part-3/chapter-11/examples/initialization/js/script.js)
- [slice.call() answer 162 of this StackOverflow Post](https://stackoverflow.com/questions/2125714/explanation-of-slice-call-in-javascript)

```javascript
 a = [7,6,5];
[ 7, 6, 5 ]
> b = [].slice.call(a)
[ 7, 6, 5 ]
```

- **[].slice.call** is meant to transform a list of objects into an array !!!! see page 320

# 321

- [Example of the accordeon component](https://getbootstrap.com/docs/5.3/components/accordion/)

# 324

- I have a problem with [part-3/chapter-11/examples/methods/index.html](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/blob/main/part-3/chapter-11/examples/methods/index.html)
  - the ToolTip triggered by a button disappears some milliseconds after it appears
