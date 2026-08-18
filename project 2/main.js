function changelog(element){
    if (element.innerText=='login') {
        element.innerText='logout'
        
    }
    else{
        element.innerText='login'

    }
}
function remove(element){
    element.remove();
}
function showAlert(){
    alert('this button');
}
function ShowAlert(){
    alert('button click');
}

var x=3;
let addspan= document.querySelector('#addspan');
function addLike(){
    x++;
    addspan.innerText=x;
}