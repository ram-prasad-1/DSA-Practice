function coinChange(coins, amt) {
  if (amt === 0) return 0;

  const amtArray = Array(amt + 1).fill(-1);

  for (let currAmt = 1; currAmt < amtArray.length; currAmt++) {
    let min = null;
    for (let j = 0; j < coins.length; j++) {
      if (currAmt === coins[j]) {
        min = 1;
        break;
      }
      if (currAmt > coins[j] && amtArray[currAmt - coins[j]] > 0) {
        if (min) {
          min = Math.min(min, amtArray[currAmt - coins[j]] + 1);
        } else {
          min = amtArray[currAmt - coins[j]] + 1;
        }
      }
    }
    amtArray[currAmt] = min || -1;
  }

  console.log(amtArray);
  return amtArray[amt];
}

console.log(coinChange([1, 2, 5], 11));
