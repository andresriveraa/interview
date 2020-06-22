import React from 'react';
import { Link } from 'react-router-dom'
import '../Styles/menu.scss'


const Menu = () => {
  return(
    <div id="menu">
      <nav>
        <Link to="/">Home </Link>
        <Link to="/login">Users</Link>
      </nav>
    </div>
  )
}

export default Menu;
