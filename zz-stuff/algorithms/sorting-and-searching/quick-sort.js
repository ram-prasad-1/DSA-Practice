function partition(arr, start, end) {
  let i = start; // index open for swapping

  // pivot = arr[end];
  for (let j = start + 1; j < end; j++) {
    if (arr[j] < arr[end]) {
      [arr[i], arr[j]] = [arr[j], arr[i]];
      i++;
    }
  }

  // swap pivot
  [arr[i], arr[end]] = [arr[end], arr[i]];
  return i;
}

function quickSort(arr, start, end) {
  if (start < end) {
    const pi = partition(arr, start, end);
    quickSort(arr, start, pi - 1);
    quickSort(arr, pi + 1, end);
  }
}

const qsArr = [27, 5, 4, 18, 1, 23, 36, 3];
quickSort(qsArr, 0, qsArr.length - 1);
