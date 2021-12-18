// https://www.techiedelight.com/find-pair-with-given-sum-array/

function findPairWithSum(arr, sum) {
  const record = {};

  for (const i of arr) {
    if (record.hasOwnProperty(sum - i)) {
      return [i, sum - i];
    } else {
      record[i] = true;
    }
  }
}

const data = [3, 4, 5, 10, 30];
console.log(findPairWithSum(data, 35));
