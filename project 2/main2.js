 const learn_more=document.querySelector("#learn_more");
 learn_more.addEventListener("click",function(){
    learn_more.style.border="4px solid red";

 }
);
 learn_more.addEventListener("mouseenter",function(){
    learn_more.style.backgroundColor="yellow";

 }
);
function dogImg(element){
    
        element.src="images/dog.png"
    }
function changeText(element){
    if (element.innerText="Shop_iphone"){
        element.innerText="Buy_iphone"
    }
    else{
        element.innerText="Shop_iphone"
    }
    element.style.backgroundColor="green"
}
