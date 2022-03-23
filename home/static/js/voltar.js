 let btnVoltar = document.querySelector('.voltar');


 btnVoltar.addEventListener('click', (event) => {

     event.preventDefault();
     window.history.go(-1);

 });