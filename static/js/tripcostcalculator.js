let submit = document.getElementById("submit");

function addition() {
    let numberofdays = document.getElementById("num").value;
    console.log(numberofdays);
    console.log(numberofdays.value * 1000);
}
submit.addEventListener("click", addition)
console.log(numberofdays.value);

/*function handleSubmit(event) {
    event.preventDefault();
    /*let cityentered=document.getElementById("cityentered");
    search(cityentered.value);*/


// module.exports = addition;