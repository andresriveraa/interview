import React from 'react';
// import '../styles/index.scss';
import { BrowserRouter, Switch, Route } from 'react-router-dom';

// components
import Login from './login'
import Menu from '../Components/menu'

function App() {
  return (
    <div className="App">
      <main>
        <nav className="nav">
          <BrowserRouter>
            <Menu />
            <Switch>
              <Route exact path="/login"
              component={Login}>
              </Route>
            </Switch>
          </BrowserRouter>
        </nav>
      </main>
    </div>
  );
}

export default App;
