//popout boxes for help
$(function () {
    $('[data-toggle="popover"]').popover()
  })

//Pagination

var numberOfBooks = $(`#loop .books`).length;
var booksPerPage = 5;
let totalPages = Math.round(numberOfBooks / booksPerPage)

