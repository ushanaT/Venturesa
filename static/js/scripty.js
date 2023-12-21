let inn = document.querySelector('.in');
let out = document.querySelector('.out')
let navb = document.querySelector('.sidebar');




inn.onclick = () =>{
    inn.classList.toggle('dotshow')
    navb.classList.toggle('show')
    out.classList.toggle('dotshow')

};



out.onclick = () =>{
    inn.classList.toggle('dotshow')
    navb.classList.toggle('show')
    out.classList.toggle('dotshow')

};



