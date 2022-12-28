/*nextdestination = document.getElementById("nextdestination");
nextdestination.onclick = myFunction();
var choice = 0;

function myFunction() {
    prompt("Enter a number between 1 to 5?");
    if (choice === 1)
        alert("You are going to France");
    else {
        alert("You are going to Germany");
    }

}*/
import 'bootstrap/js/dist/util';
setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2500);