export const traerUser = () => async (dispatch) => {
  try{
    let loginResponse = await fetch('http://127.0.0.1:8000/').then((res) => res.json())
    console.log(typeof(loginResponse));
    console.log(loginResponse);
    
    dispatch({
      type: 'Login',
      payload: loginResponse
    })
  }catch(error){
    console.log(error);
    
  }
}
