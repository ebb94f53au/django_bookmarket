$(document).ready(function(){


    var addShoppings = document.getElementsByClassName("addShopping")
    var subShoppings = document.getElementsByClassName("subShopping")
    var ischoses = document.getElementsByClassName("ischose")
    var sumprice =document.getElementById("sumprice")

//    加号操作
    for (var i = 0 ; i < addShoppings.length; i++) {
        addShopping = addShoppings[i]

        addShopping.addEventListener("click",function(){
            pid = this.getAttribute("ga")
            $.post("/changecart/0/", {"bookid":pid}, function(data){
                if (data.status == "success"){
                    document.getElementById(pid).innerHTML = data.data
                    document.getElementById(pid + "price").innerHTML = data.price
                    var sum=0
                    for (var j = 0; j < ischoses.length; j++) {
                               var bookid = ischoses[j].getAttribute("goodsid")
                               if (document.getElementById(bookid+'a').innerHTML=="√"){
                               var price =document.getElementById(bookid+"price").innerHTML
                               sum+=parseFloat(price)
                               }}
                    sumprice.innerHTML=sum
                }
            })
        },false)

        }

//        减号操作
    for (var i = 0; i < subShoppings.length; i++){
        subShopping = subShoppings[i]

        subShopping.addEventListener("click",function(){
            pid = this.getAttribute("ga")
            $.post("/changecart/1/", {"bookid":pid}, function(data){
                if (data.status == "success"){
                //添加成功，把中间的span的innerHTML变成当前的数量
                    document.getElementById(pid).innerHTML = data.data
                    document.getElementById(pid + "price").innerHTML = data.price
                    var sum=0
                    for (var j = 0; j < ischoses.length; j++) {
                               var bookid = ischoses[j].getAttribute("goodsid")
                               if (document.getElementById(bookid+'a').innerHTML=="√"){
                               var price =document.getElementById(bookid+"price").innerHTML
                               sum+=parseFloat(price)
                               }}
                    sumprice.innerHTML=sum
                    if (data.data == 0){
                        //window.location.reload()
                        //Dom节点动态操作
                        //当选中商品在购物车中减少至0，自动删除该项
                        var li = document.getElementById(pid + "li")
                        li.parentNode.removeChild(li)
                    }
                    //document.getElementById(sid).innerHTML = data.data

                }
            })
        },false)
    }


//单选操作
    for (var i = 0; i < ischoses.length; i++) {

        ischoses[i].addEventListener("click", function(){
            pid = this.getAttribute("goodsid")
            $.post("/changecart/2/", {"bookid":pid}, function(data){
                if (data.status == "success"){
                   //window.location.href = "http://127.0.0.1:8000/cart/"
                   var s = document.getElementById(pid + "a")
                   s.innerHTML = data.data
                   var sum=0
                    for (var j = 0; j < ischoses.length; j++) {
                               var bookid = ischoses[j].getAttribute("goodsid")
                               if (document.getElementById(bookid+'a').innerHTML=="√"){
                               var price =document.getElementById(bookid+"price").innerHTML
                               sum+=parseFloat(price)
                               }}
                    sumprice.innerHTML=sum
                }
            })
        }, false)
    }
//全选操作
    var allchose = document.getElementsByClassName("allchose")

        allchose[0].addEventListener("click", function(){
        if (allchose[1].innerHTML=='√'){
//            全选false
            for (var i = 0; i < ischoses.length; i++) {
               var pid = ischoses[i].getAttribute("goodsid")
               var s = document.getElementById(pid + "a")
                        s.innerHTML = ' '
                $.post("/changecart/4/", {"bookid":pid})
                                                        }
                allchose[1].innerHTML=' '
                var sum=0
                    for (var j = 0; j < ischoses.length; j++) {
                               var bookid = ischoses[j].getAttribute("goodsid")
                               if (document.getElementById(bookid+'a').innerHTML=="√"){
                               var price =document.getElementById(bookid+"price").innerHTML
                               sum+=parseFloat(price)
                               }}
                    sumprice.innerHTML=sum
        }
        else{
//        全选true
            for (var j = 0; j < ischoses.length; j++) {
               var  pid = ischoses[j].getAttribute("goodsid")
                var s = document.getElementById(pid + "a")
                        s.innerHTML ='√'
                $.post("/changecart/3/", {"bookid":pid})
                                                        }
                allchose[1].innerHTML='√'
                var sum=0
                    for (var j = 0; j < ischoses.length; j++) {
                               var bookid = ischoses[j].getAttribute("goodsid")
                               if (document.getElementById(bookid+'a').innerHTML=="√"){
                               var price =document.getElementById(bookid+"price").innerHTML
                               sum+=parseFloat(price)
                               }}
                    sumprice.innerHTML=sum
            }
        }, false)


//    总价初始操作，后将总价加入 加   减   单选  全选操作中
    var sum=0
    for (var j = 0; j < ischoses.length; j++) {
               var pid = ischoses[j].getAttribute("goodsid")
               if (document.getElementById(pid+'a').innerHTML=="√"){
               var price =document.getElementById(pid+"price").innerHTML
               sum+=parseFloat(price)
               }}
        sumprice.innerHTML=sum



//下单
    var ok = document.getElementById("ok")
    ok.addEventListener("click",function(){
        var d = confirm("是否下单？")

//           true为确定 ，false为取消
        if (d){
//            var pids=new Array()
//            for (var j = 0; j < ischoses.length; j++) {
//                var pid = ischoses[j].getAttribute("goodsid")
//                if (document.getElementById(pid+'a').innerHTML=="√"){
//                   pids[j]=pid    -->     可以用JSON.stringify转换为json字符
//                           }
//    }
//            alert(pids)
            var remarks =document.getElementById('remarks').value
            $.post("/saveorder/",{'remarks':remarks},function(data){

//                    window.location.href = "http://127.0.0.1/8000/cart/"
            if (data.status == "success"){
                alert("订单成功")
                window.location.reload()
            } else {
                alert("订单失败")
            }

            })
        }


//            $.get("/saveorder/",function(data){
//                if (data.status == "error"){
//                alert("订单失败")
//            } else {
//                alert("订单成功")
//                window.location.reload()
//            }
//        })
    })



})
