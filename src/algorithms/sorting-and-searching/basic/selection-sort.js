function selectionSort(arr) {
  for (let i = 0; i < arr.length; i++) {
    let minValueIndex = i;
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[j] < arr[minValueIndex]) {
        minValueIndex = j;
      }
    }
    [arr[i], arr[minValueIndex]] = [arr[minValueIndex], arr[i]];
  }
  return arr;
}

console.log(selectionSort([27, 5, 4, 18, 1, 23, 36, 3]));
