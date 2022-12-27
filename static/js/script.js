nextdestination = document.getElementById("nextdestination");
nextdestination.onclick = myFunction();
var choice;

function myFunction() {
    prompt("Enter a number between 1 to 5?");
    if (choice === 1)
        alert("You are going to France")
    else {
        alert("You are going to Germany")
    }

}