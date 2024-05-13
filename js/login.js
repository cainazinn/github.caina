function Entrar(){
    var email = document.getElementById('email').value;
    var senha = document.getElementById('senha').value;
    
    if(email == "rafael" && senha == "1234"){
        location.href = "home.html";
    }else{
        alert('email ou senha incorretos.');
    }
    }