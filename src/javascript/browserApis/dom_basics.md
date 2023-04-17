## DOM Basics

EventTarget ← Node ← Element

### Async and Defer Scripts

All scripts starts downloading immediately. 
But async and defer scripts don't block HTML parsing and DOM building.

- Async scripts are executed the moment they are downloaded.
- defer scripts are executed once the DOM is built, maintaining their document order. 

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

### Clipboard API

```js
navigator.clipboard
  .writeText("some text!")
  .then(() => {});
```

### Geolocation API

