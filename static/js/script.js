//popout boxes for help
$(function () {
    $('[data-toggle="popover"]').popover()
  })

//star rating

const stars=document.querySelectorAll('.star');

stars.forEach((star, i)=> {
  star.onclick = function (){
    console.log(star);
    console.log(i +1)
  }
})