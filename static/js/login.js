const form = document.querySelector("form");

const email = document.getElementById("email");

const password = document.getElementById("password");

const button = document.getElementById("loginBtn");



// Email Validation

email.addEventListener("input",()=>{

const regex=/^[^\s@]+@[^\s@]+\.[^\s@]+$/;

if(regex.test(email.value)){

email.style.borderColor="green";

}else{

email.style.borderColor="red";

}

});



// Show Password

document.getElementById("togglePassword").onclick=function(){

if(password.type==="password"){

password.type="text";

this.className="fa-solid fa-eye-slash";

}else{

password.type="password";

this.className="fa-solid fa-eye";

}

};



// Loading Button

form.addEventListener("submit",function(){

button.innerHTML="Logging in...";

button.disabled=true;

});

document

.querySelectorAll(".page-transition")

.forEach(link=>{

link.addEventListener("click",function(e){

e.preventDefault();

document

.querySelector(".login-container")

.classList.add("fade-out");

setTimeout(()=>{

window.location=this.href;

},450);

});

});

/* =====================================
PAGE TRANSITION
===================================== */

document.querySelectorAll(".page-transition").forEach(link=>{

link.addEventListener("click",function(e){

e.preventDefault();

const card=document.querySelector(".login-container");

card.style.pointerEvents="none";

card.animate(

[

{

opacity:1,

transform:"translateX(0px) scale(1)"

},

{

opacity:0,

transform:"translateX(-80px) scale(.95)"

}

],

{

duration:450,

easing:"ease-in-out",

fill:"forwards"

}

);

setTimeout(()=>{

window.location=this.href;

},450);

});

});