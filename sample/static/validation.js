// variables
let username = document.getElementById('username');
let password = document.getElementById('password');
let conf = document.getElementById('conf');
let btn = document.querySelector('.btn');
//let err = document.querySelector('.err');

//equal passwords
function equal_passwords(){
	if (password === conf){
		return true
	}else{
		return false
	}
};

// minimal lenght
function min_len(){
	if (password.lenght < 8){
	return false
	}else if(password.lenght > 12){
		return false
	}else if(username.lenght < 3){
		return false
	}else if(username.lenght > 10){
		return false
	} else{
		return true
	}
};

//validation
btn.addEventListener('click', function(ev){
	if (min_len() === false || equal_passwords() === false){
	ev.preventDefault()	
}
});
