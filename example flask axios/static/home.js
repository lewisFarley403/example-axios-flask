let time = document.getElementById('time');
let resp = axios.get('http://127.0.0.1:5000/getTime');
resp.then((value)=>{
     //when the promise is resolved. ()=>{} defines an anonymous function code goes between {}
     time.innerHTML = `the unix time is ${value.data.toString()}` // string concat, same as print('the unix time is ' + str(value.data)) in python


})