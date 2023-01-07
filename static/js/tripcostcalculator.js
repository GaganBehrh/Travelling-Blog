let submit = document.getElementById("submit");

let numberofdays = document.getElementById("num").value;

function addition() {
    console.log(numberofdays);
    console.log(numberofdays * 1000);
    alert(numberofdays * 1000);
    return (numberofdays);
}
submit.addEventListener("click", addition)
console.log(numberofdays);

/*function handleSubmit(event) {
    event.preventDefault();
    /*let cityentered=document.getElementById("cityentered");
    search(cityentered.value);*/


// module.exports = addition;