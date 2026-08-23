// https://stackoverflow.com/a/8949433/3565194
function mergeSortedArrays(arr1, arr2) {
  let i = 0;
  let j = 0;
  let sorted = [];
  while (i < arr1.length && j < arr2.length) {
    if (arr1[i] <= arr2[j]) {
      sorted.push(arr1[i]);
      i++;
    } else {
      sorted.push(arr2[j]);
      j++;
    }
  }

  while (i < arr1.length) {
    sorted.push(arr1[i]);
    i++;
  }

  while (j < arr2.length) {
    sorted.push(arr2[j]);
    j++;
  }

  return sorted;
}

console.log(mergeSortedArrays([1, 3, 9], [2, 5, 6, 7]));
