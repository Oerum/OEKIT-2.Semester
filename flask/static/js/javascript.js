/* Scroll to top button */
var btn = $('#button');

$(window).scroll(function() {
  if ($(window).scrollTop() > 300) {
    btn.addClass('show');
  } else {
    btn.removeClass('show');
  }
});

btn.on('click', function(e) {
  e.preventDefault();
  $('html, body').animate({scrollTop:0}, '300');
});
/* */

/* generelt_table convert to datatable*/
$(document).ready(function() {
  $('#table_generelt').DataTable({
    dom: 'Bfrtip',
    buttons: [ 'copy', 'csv', 'excel' ],
    fixedHeader: true,
  });

} );

/* Supply_table convert to datatable*/
$(document).ready(function() {
  $('#supply_table').DataTable({
    dom: 'Bfrtip',
    buttons: [ 'copy', 'csv', 'excel' ],
    fixedHeader: true,
  });

} );

/* table_erhverv convert to datatable*/
$(document).ready(function() {
  $('#table_erhverv').DataTable({
    dom: 'Bfrtip',
    buttons: [ 'copy', 'csv', 'excel' ],
    fixedHeader: true,
  });
} );

/* erhvervs_post_sales convert to datatable*/
$(document).ready(function() {
  $('#post_sales').DataTable({
    dom: 'Bfrtip',
    buttons: [ 'copy', 'csv', 'excel' ],
    fixedHeader: true,
  });
} );


