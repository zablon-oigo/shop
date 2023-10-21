const intiApp=()=>{

let openMenu=document.querySelector('#openMenu')
let menu=document.querySelector('#menu')
let closeMenu=document.querySelector('#closeMenu')

toggleMenu=()=>{
 menu.classList.toggle('hidden')
 menu.classList.toggle('flex')

}
openMenu.addEventListener('click',toggleMenu)
closeMenu.addEventListener('click',toggleMenu)

}
document.addEventListener('DOMContentLoaded',intiApp)