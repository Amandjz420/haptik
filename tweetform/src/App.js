import React, { Component } from 'react';

import {NameForm} from './form'
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
            <h1>My Tweet Page</h1>
        </header>
          <NameForm></NameForm>
      </div>
    );
  }
}

export default App;
