let submit = document.getElementById("submit");
const numberofdays = document.getElementById("num");
console.log(numberofdays);
// const value = numberofdays.value;


function addition(event) {
    event.preventDefault();
    let value = numberofdays.value;
    console.log(value);
    console.log(value * 1000);
    //alert("You will pay " + value * 1000 + " for this trip");
    document.getElementById("par").innerHTML = "You will pay " + value * 1000 + " for this trip";
    return (value * 1000);
}
submit.addEventListener("click", addition, false)
console.log(value);

/*function handleSubmit(event) {
    event.preventDefault();
    /*let cityentered=document.getElementById("cityentered");
    search(cityentered.value);*/


// module.exports = addition;