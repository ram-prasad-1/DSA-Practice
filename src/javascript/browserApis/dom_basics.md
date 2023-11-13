## DOM Basics

EventTarget ← Node ← Element

`new DOMParser().parseFromString('<div>...</div>');`

### Async and Defer Scripts
All scripts starts downloading immediately.
But async and defer scripts don't block HTML parsing and DOM building.

- Async scripts are executed the moment they are downloaded.
- defer scripts are executed once the DOM is built, maintaining their document order.

### URLSearchParams
Defines utility methods to work with the query string of a URL.
- The URLSearchParams constructor does not parse full URLs.
  However, it will strip an initial leading ? off of a string, if present.
- For full URLs use `new URL()`.
- use encodeURIComponent() to avoid some parsing issues

```js
const searchParams = new URLSearchParams('foo=bar&foo=baz');
```

### Web Worker API
Use for performance heavy operations. You can't directly manipulate DOM via workers.
- Service Worker is kind of a worker only. It basically acts as proxy server.

```js
// main.js
const myWorker = new Worker("worker.js");
myWorker.postMessage('something');

// worker.js
onmessage = (e) => {
  postMessage('hi from worker');
};
```

### Broadcast Channel API
The Broadcast Channel API allows basic communication between browsing contexts
(that is, windows, tabs, frames, or iframes) and workers on the same origin.

```js
const bc = new BroadcastChannel("test_channel");
bc.postMessage("This is a test message.");
bc.onmessage = (event) => {
  console.log(event);
};
bc.close();
```

### Page Visibility API
[https://developer.mozilla.org/en-US/docs/Web/API/Document/visibilityState](https://developer.mozilla.org/en-US/docs/Web/API/Document/visibilityState)
```js
document.addEventListener("visibilitychange", () => {
  console.log(document.visibilityState);
  // Modify behavior…
});
```

### Intersection Observer API
observe changes in the intersection of a target element with a scrollable ancestor element.
```js
let options = {
  root: document.querySelector("#scrollArea"),
  rootMargin: "0px",
  threshold: 1.0,
};

let observer = new IntersectionObserver(callback, options);
```

### MutationObserver API
MutationObserver can react to changes in DOM
– attributes, text content and adding/removing elements.

### Clipboard API

```js
navigator.clipboard
  .writeText("some text!")
  .then(() => {});
```

### Geolocation API

### isOnline

```js
navigator.onLine;
window.addEventListener("online", () => {});
```


