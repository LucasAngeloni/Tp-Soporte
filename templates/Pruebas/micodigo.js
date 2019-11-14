function mostraralerta(){
       alert('hizo clic!');
       }
function hacerclic(){
       var elemento=document.getElementsByTagName('p')[0];
       elemento.addEventListener('click', mostraralerta, false);
       }
window.addEventListener('load', hacerclic, false);