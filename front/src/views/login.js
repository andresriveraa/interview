import React from 'react';
import { connect } from 'react-redux';
// actions
import * as loginActions from '../actions/loginActions'

class Login extends React.Component{
  componentDidMount(){
    this.props.traerUser()
  }
  ponerpost = () => this.props.users.map((post) => (
    <ul key={post}>
      <li><p >{post.clicks}</p></li>
    </ul>
  ))
  render(){
    return(
      <div className="log">
        {this.ponerpost()}   
      </div>
    )
  }
}

const mapStateToProps = (reducers) => {
  return reducers.loginReducer
}

export default connect(mapStateToProps, loginActions)(Login);
