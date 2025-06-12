function carregar(){
    var div1 = document.querySelector(`div#msg`)
    var imagem = document.querySelector(`img#imagem`)
    var data = new Date()
    // var hora = data.getHours()
    var hora = 
    div1.innerHTML = `Agora são ${hora} horas.`
    if(hora >= 0 && hora < 12){
        imagem.src = `manha.png` 
        document.body.style.background = "#f9c545"
    }else if(hora >= 12 && hora < 18){
        imagem.src = `tarde.png`
        document.body.style.background = "#faac50"
    }else{
        imagem.src = `noite.png`
        document.body.style.background = "#3573ae"
    }
}
