const initialState = {
  user: "Stacy",
  weather: { conditions: "Rainy and miserable" },
};

const rootReducer = (state = initialState, action) => {
  switch (action.type) {
    case "GET_USER":
      //when you grab data from redux, you dont have to pass all of state
      return { ...state };
    case "SET_WEATHER":
      return { ...state, weather: { conditions: "Bright and sunny" } };
    default:
      return state;
  }
};

export default rootReducer;
