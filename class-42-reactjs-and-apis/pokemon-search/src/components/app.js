import React from 'react';
import ReactDom from 'react-dom';
import PokemonDetail from './pokemon/pokemon-detail.js';

class App extends React.Component {
  render() {
    return (
      <React.Fragment>
        <PokemonDetail></PokemonDetail>
      </React.Fragment>
    )
  }
}

export default App;