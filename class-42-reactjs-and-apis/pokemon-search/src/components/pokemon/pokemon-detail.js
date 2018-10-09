import React from 'react';
import ReactDom from 'react-dom';
import PokemonForm from './pokemon-form';
import superagent from 'superagent';

const API_URL = 'https://pokeapi.co/api/v2';

class PokemonDetail extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      pokemonLookup: {},
      pokemonSelected: null
    }

    this.pokemonSelect = this.pokemonSelect.bind(this);
  }

  componentDidUpdate() {
    console.log('search status:', this.state);
  }

  componentDidMount() {
    if (localStorage.pokemonLookup) {
      let pokemonLookup = JSON.parse(localStorage.pokemonLookup);
      this.setState({ pokemonLookup });
    } else {
      superagent.get(`${API_URL}/pokemon/`)
      .then( res => {
        let pokemonLookup = res.body.results.reduce((lookup, n) => {
          lookup[n.name] = n.url;
          return lookup;
        }, {});

        localStorage.pokemonLookup = JSON.stringify(pokemonLookup);
        this.setState({ pokemonLookup });
      })
      .catch(console.error);
    }
  }

  pokemonSelect(name) {
    if (!this.state.pokemonLookup[name]) {
      this.setState({ pokemonSelected: null })
    } else {
      superagent.get(this.state.pokemonLookup[name])
      .then( res => {
        this.setState({ pokemonSelected: res.body })
      })
      .catch(console.error)
    }
  }

  render() {
    return (
      <React.Fragment>
        <h1>Pokemon Wiki</h1>

        <PokemonForm pokemonSelect={this.pokemonSelect} />

        {!this.state.pokemonSelected ?
          <p>please select a pokemon</p> :
          <section className="pokemon">
            <h2>Selected Pokemon: {this.state.pokemonSelected.name}</h2>
            <h3>Abilities:</h3>
            <ul>
              {this.state.pokemonSelected.abilities.map((item, i) => {
                return (
                  <li key={i}>
                    <p>{item.ability.name}</p>
                  </li>
                )
              })}
            </ul>
          </section>
        }
      </React.Fragment>
    )
  }
}

export default PokemonDetail;