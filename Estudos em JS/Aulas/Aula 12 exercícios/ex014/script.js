function carregar(){
    var div = document.querySelector(`div#msg`)
    var imagem = document.querySelector(`img#imagem`)
    var data = new Date()
    var hora = data.getHours()
    div.innerHTML = `Agora são ${hora} horas.`
    if(hora >= 0 && hora < 12){
        imagem.src = `manha_circulo.png`
        document.body.style.background = `#f9c545`
    } else if(hora >= 12 && hora < 18){
        imagem.src = `tarde_circulo.png`
        document.body.style.background = `#faac50`
    } else{
        imagem.src = `noite_circulo.png`
        document.body.style.background = `#3c3c3c`
    }
    
}
