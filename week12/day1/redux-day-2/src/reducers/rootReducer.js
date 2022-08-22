const initialState = {
  user: "Stacy",
  weather: {
    weather: [
      {
        description: "Weather Conditions",
        icon: "01d",
      },
    ],
    main: { temp: "", feels_like: "", humidity: "" },
    name: "City",
  },
  location: "",
  changeMe: "",
};

const rootReducer = (state = initialState, action) => {
  switch (action.type) {
    case "GET_USER":
      //when you grab data from redux, you dont have to pass all of state
      return { ...state };
    case "SET_LOCATION":
      return { ...state, location: action.payload };
    case "SET_CHANGEME":
      return { ...state, changeMe: action.payload };
    case "SET_WEATHER":
      return { ...state, weather: action.payload };
    default:
      return state;
  }
};

export default rootReducer;
