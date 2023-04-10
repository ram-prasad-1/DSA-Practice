// page load
// <script src="myScript.js" defer></script> // will execute when dom is ready. put anywhere
// <link rel="stylesheet" href="css/style.css">  (for reference)
window.addEventListener('DOMContentLoaded', () => {});
window.onload = () => {};

// query
document.querySelector('.hero');
document.querySelectorAll('');

// style
el.style.display = 'none';
el.style.width = '400px';

// classes
el.classList.add('anotherclass');
el.classList.remove('foo');
el.classList.toggle('visible');

// events
el.addEventListener('click', (e) => {
  e.target.classList.remove('foo');
});

// Manipulate DOM
const newDiv = document.createElement('div');
const newContent = document.createTextNode('Hi there!');
newDiv.appendChild(newContent);
newDiv.remove();
newDiv.parentNode;
