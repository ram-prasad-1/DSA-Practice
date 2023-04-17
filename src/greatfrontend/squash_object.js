// https://www.greatfrontend.com/questions/javascript/squash-object
function squashObject(obj, prefix = '') {
  let result = {};
  for (const [k, v] of Object.entries(obj)) {
    const newKey = prefix ? `${prefix}.${k}` : k;
    if (Array.isArray(v) || typeof v !== 'object') {
      result[newKey] = v;
    } else {
      result = {
        ...result,
        ...squashObject(v, newKey),
      };
    }
  }

  return result;
}

const object = {
  a: 5,
  b: 6,
  c: {
    f: 9,
    g: {
      m: 17,
      n: 3,
    },
  },
};

console.log(squashObject(object)); // { a: 5, b: 6, 'c.f': 9, 'c.g.m': 17, 'c.g.n': 3 }
