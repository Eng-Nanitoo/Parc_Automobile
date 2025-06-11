document.getElementById("form").onsubmit = function () {
    if(checkPhone()){
        return true;
    }

    return false
}


function checkPhone(){
    let phone = document.getElementById("phone").value
    let span = document.getElementById("phoneError")
    const phoneRegex  = /^[2-4]\d{7}$/

    if(phone === ""){
        span.innerHTML = ""
        return true
    }

    else if(phone[0] != "2" && phone[0] != "3" && phone[0] != "4"){
        span.innerHTML = "Numero doit commence par 2,3 ou 4"
    }

    else if (phoneRegex.test(phone)){
        span.innerHTML = ""
        return true
    }

    else if(phone.length != 8){
        span.innerHTML = "Numero de telephone doit etre 8"
    }

    else {
        span.innerHTML = "invalid numero"
    }

    return false
}