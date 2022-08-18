import React from "react";
import { useState } from "react";

export default function PokeCard(props) {
  const [front, setFront] = useState(true);

  return (
    <div className="pokemoncard">
      <p>{props?.poke?.name}</p>
      <button
        onClick={() => {
          console.log(props.i);
          props.setPokemon(
            props.pokemon.filter((i) => props.i !== props.pokemon[i])
          );
        }}
      >
        Delete
      </button>
      <img
        onClick={() => setFront(!front)}
        src={front ? props?.poke?.sprites?.front : props?.poke?.sprites?.back}
        alt=""
      />
      <p>{props?.poke?.hp}</p>
    </div>
  );
}

//splice at the index in the state
