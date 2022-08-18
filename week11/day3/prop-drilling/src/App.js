import "./App.css";
import Prop1 from "./components/Prop1";
import { useEffect, useState } from "react";
import PokeCard from "./components/PokeCard";

function App() {
  const state = {
    pokemon: [
      {
        pokemon: [
          {
            id: 1,
            name: "bulbasaur",
            hp: 45,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/1.png",
            },
          },
          {
            id: 2,
            name: "ivysaur",
            hp: 60,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/2.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/2.png",
            },
          },
          {
            id: 3,
            name: "venusaur",
            hp: 80,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/3.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/3.png",
            },
          },
          {
            id: 4,
            name: "charmander",
            hp: 39,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/4.png",
            },
          },
          {
            id: 5,
            name: "charmeleon",
            hp: 58,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/5.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/5.png",
            },
          },
          {
            id: 6,
            name: "charizard",
            hp: 78,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/6.png",
            },
          },
          {
            id: 7,
            name: "squirtle",
            hp: 44,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/7.png",
            },
          },
          {
            id: 8,
            name: "wartortle",
            hp: 59,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/8.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/8.png",
            },
          },
          {
            id: 9,
            name: "blastoise",
            hp: 79,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/9.png",
            },
          },
          {
            id: 10,
            name: "caterpie",
            hp: 45,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/10.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/10.png",
            },
          },
          {
            id: 11,
            name: "metapod",
            hp: 50,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/11.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/11.png",
            },
          },
          {
            id: 12,
            name: "butterfree",
            hp: 60,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/12.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/12.png",
            },
          },
          {
            id: 13,
            name: "weedle",
            hp: 40,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/13.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/13.png",
            },
          },
          {
            id: 14,
            name: "kakuna",
            hp: 45,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/14.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/14.png",
            },
          },
          {
            id: 15,
            name: "beedrill",
            hp: 65,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/15.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/15.png",
            },
          },
          {
            id: 16,
            name: "pidgey",
            hp: 40,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/16.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/16.png",
            },
          },
          {
            id: 17,
            name: "pidgeotto",
            hp: 63,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/17.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/17.png",
            },
          },
          {
            id: 18,
            name: "pidgeot",
            hp: 83,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/18.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/18.png",
            },
          },
          {
            id: 19,
            name: "rattata",
            hp: 30,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/19.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/19.png",
            },
          },
          {
            id: 20,
            name: "raticate",
            hp: 55,
            sprites: {
              front:
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/20.png",
              back: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/20.png",
            },
          },
        ],
      },
    ],
  };
  const [counter, setCounter] = useState(0);
  const [pokemon, setPokemon] = useState([]);

  useEffect(() => {
    setPokemon(state.pokemon[0].pokemon);
  }, []);

  const houses = [
    {
      title: "Stacy's Beach House",
      address: "123 Main St. USA",
    },
    {
      title: "Stacy's Beach House 2",
      address: "12323 Main St. USA",
    },
  ];
  const owner = {
    firstName: "Stacy",
    lastName: "Samuels",
  };
  return (
    <div className="App">
      <h1>Prop Drilling</h1>
      <button onClick={() => setCounter(counter + 1)}>+</button>
      <div className="pokeCard">
        {pokemon?.map((poke, i) => {
          return (
            <PokeCard
              poke={poke}
              pokemon={pokemon}
              setPokemon={setPokemon}
              i={i}
            />
          );
        })}
        {/* <Prop1 houses={houses} owner={owner} /> */}
      </div>
    </div>
  );
}

export default App;
