const classPhoto = () => {
  let isTrue = true;
  let redShirtHeights = [5, 8, 1, 3, 4];
  let blueShirtHeights = [6, 9, 2, 4, 5];
  let frontLine = [];

  redShirtHeights.sort(function (a, b) {
    return a - b;
  });
  blueShirtHeights.sort(function (a, b) {
    return a - b;
  });

  if (blueShirtHeights[0] < redShirtHeights[0]) {
    frontLine = blueShirtHeights;
  }
  if (redShirtHeights[0] < blueShirtHeights[0]) {
    frontLine = redShirtHeights;
  }

  for (let i = 0; i < frontLine.length; i++) {
    if (
      blueShirtHeights[i] < redShirtHeights[i] &&
      frontLine === blueShirtHeights
    ) {
      isTrue = true;
    } else if (
      blueShirtHeights[i] > redShirtHeights[i] &&
      frontLine === redShirtHeights
    ) {
      isTrue = true;
    } else {
      isTrue = false;
    }
  }
  console.log(isTrue);
  return isTrue;
};

classPhoto();
