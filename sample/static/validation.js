// variables
let username = document.getElementById('username').innerText;
let password = document.getElementById('password').innerText;
let conf = document.getElementById('conf').innerText;
let btn = document.querySelector('.btn');
let err = document.querySelector('.err');

//equal passwords
function equal_passwords(){
	if (password === conf){
		return true
	}else{
		return false
	}
};

// minimal lenght password
function pass_min_len(){
	if (password.lenght < 8){
		return false
	}else{
		return true
	}
};

// max length password
function pass_max_len(){
	if(password.lenght > 12){
		return false
		}else{
		return true
		}};
		
// min length user
function user_min_len(){
	if(username.lenght > 3){
		return true
	}else{
		return false
	}
};

//max lentgh user
function user_max_len(){
	if(username.lenght < 10){
		return true
}else{
	return false
}
};

//validation -- Need a debugging
btn.addEventListener('click', function(ev){
	if (user_min_len() === false){
		err.innerText = "Username is too short"
		ev.preventDefault()
}else if(user_max_len() === false){
		err.innerText = "Username is too long"
		ev.preventDefault()
}else if (equal_passwords() === false){
		err.innerText = 'The passwords do not match'
		ev.preventDefault()
		console.log('The passwords do not match')	
}else if (pass_min_len() === false) {
		err.innerText = 'Password is too short'
		ev.preventDefault()	
}else if (pass_max_len() === false) {
		err.innerText = 'Password is too long'
		ev.preventDefault()	
		
}});
