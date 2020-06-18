import React from 'react';
import '../static/css/App.css';
import { BrowserRouter, Switch, Route } from 'react-router-dom';

// components
import Login from './login'

function App() {
  return (
    <div className="App">
      <nav className="nav">
        <BrowserRouter>
          <Switch>
            <Route exact path="/login"
            component={Login}>
            </Route>
          </Switch>
        </BrowserRouter>
      </nav>
      <header className="App-header">
        <p>hello world</p>
      </header>
    </div>
  );
}

export default App;
