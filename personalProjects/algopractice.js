//write a function that takes in an array of positive integers and returns maximum sum of non-adjacent elements in the array
//if array is empty, function return zero

const maxSubsetSumNoAdjacent = () => {
  let array = [75, 105, 120, 75, 90, 135];
  let nums = 0;
  if (array === []) {
    return 0;
  } else {
    for (let i = 1; i < array.length + 1; i += 2) {
      nums += array[i - 1];
      console.log(nums);
    }
    console.log(nums);
  }
};

maxSubsetSumNoAdjacent();
