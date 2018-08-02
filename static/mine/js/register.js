$(document).ready(function(){
    var accunt = document.getElementById('accunt')
    var pass = document.getElementById('pass')
    var passwd = document.getElementById('passwd')
    var form1 = document.getElementById('form1')

    var accunterr = document.getElementById('accunterr')
    var checkerr = document.getElementById('checkerr')
    var passerr = document.getElementById('passerr')
    var passwderr = document.getElementById('passwderr')

    accunt.addEventListener("focus",function(){
        accunterr.style.display = "none"
        checkerr.style.display = "none"

    },false)
    accunt.addEventListener("blur",function(){
        var inputStr = this.value

        /*
        if (inputStr.length != 8) {
        */
        if (inputStr.length < 6 || inputStr.length >12){
            accunterr.style.display = "block"
        }else{
        sub.disabled=0
        }

        $.post("/checkuserid/",{"userid":inputStr},function(data){

            if(data.status == "error"){
                checkerr.style.display = "block"

            }else{
        sub.disabled=0
        }
        })
        },false)


        /*
        else{
//          验证账号是否被注册
            console.log("*****************1")
            $.ajax({
                url:"/checkuserid/",
                type:"post",
                typedata:"json",
                data:{"checkid":accunt.value},
                success:function(data){
                    console.log(data)
                    if (data.status == "error"){
                        checkerr.style.display = "block"
                    }
                }
            })
        }
    },false)
    */

    pass.addEventListener("focus",function(){
        passerr.style.display = "none"
    },false)
    pass.addEventListener("blur",function(){
        var inputStr = this.value
        if (inputStr.length < 6 || inputStr.length > 16) {
            passerr.style.display = "block"

        }else{
        sub.disabled=0
        }
    },false)


    passwd.addEventListener("focus",function(){
        passwderr.style.display = "none"

    },false)
    passwd.addEventListener("blur",function(){
        var inputStr = this.value
        if (inputStr != pass.value) {
            passwderr.style.display = "block"

        }else{
        sub.disabled=0
        }
    },false)


//    form1.addEventListener("click",function(){
//        if(accunterr.style.display=="none"&&
//        passwderr.style.display=="none"&&
//        checkerr.style.display=="none"&&
//        passerr.style.display=="none"){
//        alert(111111)
//            this.submit="return true"
//        }else{
//        alert(22222)
//        this.submit="return false"
//        }
//
//
//    },false)

})
function checksubmit(){
        if(accunterr.style.display=="none"&&
        passwderr.style.display=="none"&&
        checkerr.style.display=="none"&&
        passerr.style.display=="none"){

            return true
        }else{

        return false
        }
}