//const { compileFunction } = require("vm");

window.location.href("https://nyu.qualtrics.com/jfe/form/SV_ePNv0eXvGWgCxkq?");
document.getElementById("NextButton").click();

document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById("QID2-1-label").click();
    document.getElementById("NextButton").click();  
})

document.getElementById("username").value = "username";
document.getElementById("password").value = "password";

//To get the submit button
combined = document.getElementsByName("_eventId_proceed")
combined[0].click()

document.getElementById("duo_iframe").contentWindow;

combo = document.getElementsByClassName("positive auth-button")
combo[0].click()

//You can definitely write something to also bypass the code...
//but that is so much more work that it's definitely not worth it
//Just use the push button or contribute to this project to add the bye duo stuff here
//Note that would involve needing to mess with local files to store the hotp and counter

completion(true);