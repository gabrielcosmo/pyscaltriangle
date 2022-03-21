let hamburguer = document.getElementById("hamburguer")
let aside = document.getElementById("side-bar")

hamburguer.onclick = () => {
    if(aside.style.display != "none"){
        aside.style.display = "none"
        offHamburguer()
    } else{
        aside.style.display = "block"
        onHamburguer()
    }
}

//#region function

function ocultContent(e) {

    let desc = e.parentElement.children[1]

    if (desc.style.cssText == "display: none;") {
        desc.style.cssText = "display: inherit;"
    } else {
        desc.style.cssText = "display: none;"
    }
}

function onHamburguer(){
    hamburguer.style.width = "4vh"
    hamburguer.style.height = "4vh"
    hamburguer.style.padding = "1vh"
}

function offHamburguer(){
    hamburguer.style.width = "5vh"
    hamburguer.style.height = "5vh"
    hamburguer.style.padding = "0.5vh"

    hamburguer.style.borderWidth = "0px"
}

//#endregion