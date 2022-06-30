const suits = ["spades", "diamonds", "clubs", "hearts"];
const values = [
  "A",
  "2",
  "3",
  "4",
  "5",
  "6",
  "7",
  "8",
  "9",
  "10",
  "J",
  "Q",
  "K",
];

function makeDeck() {
  let deck = [];
  for (let index = 0; index < suits.length; index++) {
    for (let x = 0; x < values.length; x++) {
      let card = { Value: values[x], Suit: suits[index] };
      deck.push(card);
    }
  }
  return deck;
}

function getCardNumericValue(card) {
  switch (card.value) {
    case "Ace":
      return 1;
      return 11;
    case "Two":
      return 2;
    case "Three":
      return 3;
    case "Four":
      return 4;
    case "Five":
      return 5;
    case "Six":
      return 6;
    case "Seven":
      return 7;
    case "Eight":
      return 8;
    case "Nine":
      return 9;
    default:
      return 10;
  }
}
