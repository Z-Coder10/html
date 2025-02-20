var myform = document.getElementById("myform")

var myInput = document.getElementById("myinput")

var myItem = document.getElementById("myitem")

myform.addEventListener('submit',

function(event){

createItem(myInput.value)

}

)

function createItem(inputItems){

var item = `<li> ${inputItems}

<button onclick="deleteElement(this)">Delete</button></li>

`

myItem.insertAdjacentElement("beforeend", item)

myInput.value=""

myInput.focus()

}

function deleteElement(ElementToDelete){

ElementToDelete.parentElement.remove()

}clock