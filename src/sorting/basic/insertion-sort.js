function insertionSort(arr) {
    for (let i = 1; i < arr.length; i++) {
        for (let j = i - 1; j >= 0; j--) {
            if (arr[j] > arr[j + 1]) {
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
            } else {
                break;
            }
        }
    }
    return arr;
}

console.log(insertionSort([27, 5, 4, 18, 1, 23, 36, 3]));
