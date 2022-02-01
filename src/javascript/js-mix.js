// JS is copy by reference value
let user = { name: 'virat' };
const list = [user];
user = null;

console.log(list); // prints [{name: 'virat'}]
