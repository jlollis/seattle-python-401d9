import React from 'react';
import ReactDom from 'react-dom';

class PokemonForm extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      pokeName: ''
    }
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handlePokemonNameChange = this.handlePokemonNameChange.bind(this);
  }

  handleSubmit(e) {
    e.preventDefault();
    this.props.pokemonSelect(this.state.pokeName);
  }

  handlePokemonNameChange(e) {
    this.setState({ pokeName: e.target.value });
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <input
          type='text'
          name='pokemonName'
          placeholder='search for a pokemon'
          value={this.state.pokeName}
          onChange={this.handlePokemonNameChange} />
      </form>
    )
  }
}

export default PokemonForm;