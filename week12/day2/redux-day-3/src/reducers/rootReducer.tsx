import { StringLiteral } from "typescript";
import Cart from "../components/Cart";

const listOfProducts = [
  {
    description: "poofy hat",
    price: "20",
  },
  {
    description: "flowy dress",
    price: "100",
  },
  {
    description: "silk tie",
    price: "15",
  },
  {
    description: "high heels",
    price: "55",
  },
  {
    description: "sweatpants",
    price: "30",
  },
  {
    description: "tuxedo",
    price: "1000",
  },
];

export interface ProductDetail {
  description: string;
  price: string;
}

type State = {
  products: ProductDetail[];
  cart: ProductDetail[];
  orders?: {
    name?: string;
    items?: ProductDetail[];
  };
};

const initialState: State = {
  products: listOfProducts,
  cart: [],
  orders: {},
};

type Action = {
  type: string;
  payload?: any;
};

const rootReducer = (state = initialState, action: Action) => {
  switch (action?.type) {
    case "ADD_TO_CART":
      return {
        ...state,
        cart: [...state.cart, action?.payload],
      };
    default:
      return state;
  }
};

export default rootReducer;
