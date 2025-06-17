function verific(){
    var div = document.querySelector(`div#msg`)
    var imagem = document.querySelector(`img#imagem`)
    var input = document.querySelector(`input#inpt`)
    var anoNasc = (input.value)
    var data = new Date()
    var anoAtual = data.getFullYear()
    var idade = anoAtual - anoNasc

    div.innerHTML = `Sua idade é.`
}
