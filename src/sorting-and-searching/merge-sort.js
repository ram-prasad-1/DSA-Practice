
// Trick:
// divide recursively till array length remain 1 or 2.  now start merging.

// Merging sorted array:
// Method-1: Copy arr1 in arr3 and iterate over arr2 to insert them in arr3 at right position.
// Method-2: Traverse both arr1 and arr2 simultaneously and insert smaller to arr3
// https://www.geeksforgeeks.org/merge-two-sorted-arrays/

function mergeSort(arr) {
    if (arr.length === 1) return arr;
    if (arr.length === 2) {
        return arr[0] <= arr[1] ? arr : [arr[1], arr[0]];
    }

    let arr1 = mergeSort(arr.slice(0, Math.trunc(arr.length / 2)));
    let arr2 = mergeSort(arr.slice(Math.trunc(arr.length / 2)));

    let arrSorted = [];
    let i = 0;
    let j = 0;

    while (i < arr1.length && j < arr2.length) {
        if (arr1[i] <= arr2[j]) {
            arrSorted.push(arr1[i]);
            i++;
        } else {
            arrSorted.push(arr2[j]);
            j++;
        }
    }

    while (i < arr1.length) {
        arrSorted.push(arr1[i]);
        i++;
    }

    while (j < arr2.length) {
        arrSorted.push(arr2[j]);
        j++;
    }
    return arrSorted;
}

console.log(mergeSort([27, 5, 4, 18, 1, 23, 36, 3]));
