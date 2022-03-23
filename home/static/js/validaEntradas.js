let inputfileImg = document.querySelector('#inputfileImg');
let notificaerro = document.querySelector('.notificacao');
let form = document.querySelector('.form');
let btnMSG = document.querySelector('.close-msg');
let formEditar = document.querySelector('.form-editar');
let inputText = document.querySelector('.inputText');
let extensoes = ['png', 'jpeg', "jpg"];

form.addEventListener('submit', (event => {

    validaImagens(event);

}))

function validaImagens(event) {

    let erro = true;

    let extensaoArquivo = inputfileImg.value.split(".")[inputfileImg.value.split(".").length - 1]

    for (let extensao = 0; extensao < extensoes.length; extensao++) {


        if (extensaoArquivo.toUpperCase() == extensoes[extensao].toUpperCase()) {


            erro = false;
            break;
        }

    }


    if (erro) {

        event.preventDefault();

        notificaerro.style.display = 'block';


    }


}