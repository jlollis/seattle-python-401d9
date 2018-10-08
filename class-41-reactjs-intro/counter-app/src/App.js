import React, { Component } from 'react';
import Header from './components/header/header.js';
import Footer from './components/footer/footer.js';
import Counter from './components/counter/counter.js';
import './App.css';

class App extends Component {
  render() {
    return (
      <React.Fragment>
        <Header></Header>
        <Counter></Counter>
        <Counter></Counter>
        <Counter></Counter>
        <Counter></Counter>
        <Counter></Counter>
        <Counter></Counter>
        <Footer></Footer>
      </React.Fragment>
    );
  }
}

export default App;
