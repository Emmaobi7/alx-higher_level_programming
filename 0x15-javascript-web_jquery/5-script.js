const $add = $('div#add_item')
const $ls = $('ul.my_list')

$add.on('click', function () {
  $ls.append('<li>item</li>')
})
