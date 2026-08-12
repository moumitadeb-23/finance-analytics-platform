// ===============================================
// FINANCE ANALYTICS PLATFORM
// Registration JS Version 5.0
// Part 1
// ===============================================


// ---------- Elements ----------

const form = document.getElementById("registerForm");

const nameInput = document.getElementById("name");

const emailInput = document.getElementById("email");

const passwordInput = document.getElementById("password");

const confirmInput = document.getElementById("confirm_password");

const nameMsg = document.getElementById("nameMsg");

const emailMsg = document.getElementById("emailMsg");

const passwordMsg = document.getElementById("passwordMsg");

const confirmMsg = document.getElementById("confirmMsg");

const strengthBar = document.getElementById("strengthBar");

//const togglePassword = document.getElementById("togglePassword");

//const toggleConfirm = document.getElementById("toggleConfirm");



// ---------- Name Validation ----------

nameInput.addEventListener("input", () => {

    const regex = /^[A-Za-z ]{3,50}$/;

    if (regex.test(nameInput.value.trim())) {

        nameMsg.innerHTML = "✅ Valid Name";

        nameMsg.style.color = "green";

    }

    else {

        nameMsg.innerHTML = "❌ Enter only letters (3-50 characters)";

        nameMsg.style.color = "red";

    }

});




// ---------- Email Validation ----------

emailInput.addEventListener("input", () => {

    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (regex.test(emailInput.value.trim())) {

        emailMsg.innerHTML = "✅ Valid Email";

        emailMsg.style.color = "green";

    }

    else {

        emailMsg.innerHTML = "❌ Invalid Email Address";

        emailMsg.style.color = "red";

    }

});




// ---------- Password Strength ----------

passwordInput.addEventListener("input", () => {

    const password = passwordInput.value;

    let score = 0;

    if (password.length >= 8) score++;

    if (/[A-Z]/.test(password)) score++;

    if (/[a-z]/.test(password)) score++;

    if (/[0-9]/.test(password)) score++;

    if (/[!@#$%^&*(),.?":{}|<>]/.test(password)) score++;




    if (score <= 2) {

        strengthBar.style.width = "30%";

        strengthBar.style.background = "#dc3545";

        passwordMsg.innerHTML = "Weak Password";

        passwordMsg.style.color = "#dc3545";

    }

    else if (score <= 4) {

        strengthBar.style.width = "70%";

        strengthBar.style.background = "#ffc107";

        passwordMsg.innerHTML = "Medium Password";

        passwordMsg.style.color = "#d97706";

    }

    else {

        strengthBar.style.width = "100%";

        strengthBar.style.background = "#16a34a";

        passwordMsg.innerHTML = "Strong Password";

        passwordMsg.style.color = "#16a34a";

    }

});

// ===============================================
// Confirm Password Validation
// ===============================================

confirmInput.addEventListener("input", () => {

    if (confirmInput.value.length === 0) {

        confirmMsg.innerHTML = "";
        return;

    }

    if (passwordInput.value === confirmInput.value) {

        confirmMsg.innerHTML = "✅ Passwords Match";
        confirmMsg.style.color = "#16a34a";

    }

    else {

        confirmMsg.innerHTML = "❌ Passwords Do Not Match";
        confirmMsg.style.color = "#dc3545";

    }

});



// ===============================================
// Show / Hide Password
// ===============================================

/*togglePassword.addEventListener("click", () => {

    if (passwordInput.type === "password") {

        passwordInput.type = "text";

        togglePassword.classList.remove("fa-eye");
        togglePassword.classList.add("fa-eye-slash");

    }

    else {

        passwordInput.type = "password";

        togglePassword.classList.remove("fa-eye-slash");
        togglePassword.classList.add("fa-eye");

    }

});*/



// ===============================================
// Show / Hide Confirm Password
// ===============================================

/*toggleConfirm.addEventListener("click", () => {

    if (confirmInput.type === "password") {

        confirmInput.type = "text";

        toggleConfirm.classList.remove("fa-eye");
        toggleConfirm.classList.add("fa-eye-slash");

    }

    else {

        confirmInput.type = "password";

        toggleConfirm.classList.remove("fa-eye-slash");
        toggleConfirm.classList.add("fa-eye");

    }

});*/



// ===============================================
// Form Validation
// ===============================================

form.addEventListener("submit", function (e) {

    const nameRegex = /^[A-Za-z ]{3,50}$/;

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    const password = passwordInput.value;

    const strongPassword =

        password.length >= 8 &&
        /[A-Z]/.test(password) &&
        /[a-z]/.test(password) &&
        /[0-9]/.test(password) &&
        /[!@#$%^&*(),.?":{}|<>]/.test(password);



    if (!nameRegex.test(nameInput.value.trim())) {

        alert("Please enter a valid full name.");

        e.preventDefault();

        return;

    }



    if (!emailRegex.test(emailInput.value.trim())) {

        alert("Please enter a valid email address.");

        e.preventDefault();

        return;

    }



    if (!strongPassword) {

        alert(
`Password must contain:

• Minimum 8 characters
• One uppercase letter
• One lowercase letter
• One number
• One special character`
        );

        e.preventDefault();

        return;

    }



    if (passwordInput.value !== confirmInput.value) {

        alert("Passwords do not match.");

        e.preventDefault();

        return;

    }



    if (!document.getElementById("terms").checked) {

        alert("Please accept the Terms & Conditions.");

        e.preventDefault();

        return;

    }

});

document

.querySelectorAll(".page-transition")

.forEach(link=>{

link.addEventListener("click",function(e){

e.preventDefault();

document

.querySelector(".container")

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

const card=document.querySelector(".container");

card.style.pointerEvents="none";

card.animate(

[

{

opacity:1,

transform:"translateX(0px) scale(1)"

},

{

opacity:0,

transform:"translateX(80px) scale(.95)"

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

/* ==========================================
PASSWORD SHOW / HIDE
========================================== */

document.querySelectorAll(".toggle-password").forEach((icon)=>{

    icon.style.cursor="pointer";

    icon.addEventListener("click",function(e){

        e.preventDefault();
        e.stopPropagation();

        const input=document.getElementById(
            this.dataset.target
        );

        if(!input) return;

        if(input.type==="password"){

            input.type="text";

            this.classList.remove("fa-eye");
            this.classList.add("fa-eye-slash");

        }

        else{

            input.type="password";

            this.classList.remove("fa-eye-slash");
            this.classList.add("fa-eye");

        }

    });

});