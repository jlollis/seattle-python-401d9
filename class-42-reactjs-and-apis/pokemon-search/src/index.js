import React from 'react';
import ReactDOM from 'react-dom';
import App from './components/app.js';
import * as serviceWorker from './serviceWorker';

class Main extends React.Component {
  render() {
    return (
      <React.Fragment>
        <App />
      </React.Fragment>
    )
  }
}

ReactDOM.render(<Main />, document.getElementById('root'));

serviceWorker.unregister();
