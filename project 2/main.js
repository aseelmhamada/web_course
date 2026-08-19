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
const btn13=document.querySelector('#btn13');
btn13.addEventListener('click',function(){
    btn13.style.padding='20px';
    
})

    

function ShowAlert(){
    alert('button click');

}

const btn37= document.querySelector('#btn37');

like2.addEventListener('click', function() {
    btn37.style.borderWidth = '4px';
    btn37.style.borderStyle = 'solid';
    btn37.style.border =' 4px solid red';
});


var x=3;
let addspan= document.querySelector('#addspan');
function addLike(){
    x++;

    addspan.innerText=x;
    
}
function changecolor(element){
    element.style.backgroundColor = 'blue';
    element.style.color="red";
    



}

