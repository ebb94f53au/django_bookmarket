$(document).ready(function(){

var sumprice = document.getElementsByClassName("sumprice")

for(var i=0;i<sumprice.length;i++){
var money=document.getElementsByClassName(i+1+"price")
    var sum=0
    for(var j=0;j<money.length;j++){
    sum+=parseFloat(money[j].innerHTML.replace("￥",""))

    }
     sumprice[i].innerHTML=sum
}
//收货

var ok =document.getElementsByClassName("check")
for (var i=0;i<ok.length;i++){

    ok[i].addEventListener("click",function(){
var token=this.getAttribute("token")
    alert(token)
        $.post("/show_orders/",{"token":token},function(data){
            if(data.status=="success"){
            alert("收货成功")
            window.location.href="/mine/"
            }
            else{

            }

        })

    })
}
})