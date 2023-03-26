`
Promises are a pattern for delivering results asynchronously.

Promise-based functions start synchronously, settle asynchronously.

Every call to a .then()/.catch() returns a new promise.

.catch() handles both rejected promises and errors thrown.

A handler, used in .then(handler) may create and return a promise.
In that case further handlers wait until it settles, and then get its result.
`;

const p = new Promise((resolve, reject) => {});

p.then((value) => {})
  .catch((err) => {})
  .finally(() => {});

Promise.resolve(4).then(() => {});

`
Promise combinators
Promise.all() is interested in fulfillment of all.
Promise.any() is interested in the first fulfillment.
Promise.race() is interested in settlements.

Trick: Promise.race is interested in rest.
and Promise.all and Promise.any are interested in accomplishment.
`;
let p1 = Promise.resolve(1);
let p2 = Promise.resolve(1);
const p3 = Promise.all([p1, p2]); // return all results or first error
const p4 = Promise.any([p1, p2]); // return first result
const p5 = Promise.race([p1, p2]); // return first settled

// promisified timeout
function asyncTimeout(cb, wait) {
  return new Promise((resolve) => {
    setTimeout(() => {
      cb();
      resolve();
    }, wait);
  });
}

`
Async-await
async function always returns a promise.

await always resolves to a value. In case of
chained multiple promises it waits for all of them to complete.
`;

const fn = async () => {
  try {
    const promise = Promise.resolve(99);

    // if promise is rejected, the rejected value is thrown.
    const value = await promise;
  } catch (e) {}
};
