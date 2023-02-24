const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");

// When the login button is clicked, the following code is executed
loginButton.addEventListener("click", (e) => {
    // Prevent the default submission of the form
    e.preventDefault();
    // Get the values input by the user in the form fields
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    if (username === "Never gonna let you down" && password === "Never gonna say goodbye") {
        // If the credentials are valid, show an alert box and reload the page
        // selam! :)
        alert("IGU{c0ngr4tz!_bas1t_s1fr3lr3_d1kk4t}");
        location.reload();
    } else {
        // Otherwise, make the login error message show (change its oppacity)
        loginErrorMsg.style.opacity = 1;
    }
})
