//
const calcTotal = (total, tipPercent) => {
  let mealTotal = total * tipPercent;
  return mealTotal + total;
};

//console.log(calcTotal(12, 0.53).toFixed(2));

//total of bill, if above 100, add 30% grat
//if between 50 and 99, add 25%
//if below 50 add 20% grat

const calcTotal1 = (total) => {
  if (total > 100) {
    return total * 1.3;
  }
  if (total >= 50 && total <= 99) {
    return total * 1.25;
  }
  if (total < 50) {
    return total * 1.2;
  }
};
//console.log(calcTotal1(10.00).toFixed(2));

//function that recieves a number
//guaranteed to be between 1 and 5
//time slot as a string "7:30PM"
//number range
//if vip = 4 or 5
//if vip = 3 placed second
//if lower than 3, placed last
// 5, 3, 1
// expected output return array [{vipStatus 5, timeslot: 7:30},  ]

//this does not work, need to reset
//how you grab the data is what matters/ how you sort it afterwards
const makeAReservation = (vipStatus, timeslot) => {
  const reservationOrder = [];
  if (vipStatus >= 4) {
    reservationOrder.push(vipStatus, timeslot);
  }
  let reservationGuest = {
    status: vipStatus,
    time: timeslot,
  };
  if (vipStatus == 3) {
    reservationOrder.push(vipStatus, timeslot);
  }
  if (vipStatus < 3) {
    reservationOrder.push(vipStatus, timeslot);
  }
  return reservationOrder;
};

console.log(makeAReservation(5, "7:30"));
console.log(makeAReservation(3, "7:30"));
console.log(makeAReservation(1, "7:30"));
