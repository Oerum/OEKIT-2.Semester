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


/*Generelt_table convert to datatable*/
$(document).ready(function() {
  $('#table_generelt').dataTable({
    dom: 'Bfrtip',
    buttons: [ 'copy', 'csv', 'excel' ],
    fixedHeader: true,
    "footerCallback": function ( row, data, start, end, display ) {
          var api = this.api(), data;

          // converting to interger to find total
          var intVal = function ( i ) {
            return typeof i === 'string' ?
                i.replace(/[\$,]/g, '')*1 :
                typeof i === 'number' ?
                    i : 0;
          };

          // computing column Total of the complete result
          var monTotal = api
              .column( 1 )
              .data()
              .reduce( function (a, b) {
                  return intVal(a) + intVal(b);
              }, 0 );
          var nf1 = new Intl.NumberFormat();
          var totalsum_dec = nf1.format(monTotal)

          // Update footer by showing the total with the reference of the column index
          $( api.column( 1 ).footer() ).html('Total: ' + totalsum_dec);
      }
  } );
} );



/* Supply_table convert to datatable*/
$(document).ready(function() {
  $('#supply_table').dataTable({
    dom: 'Bfrtip',
    buttons: [ 'copy', 'csv', 'excel' ],
    fixedHeader: true,
    "footerCallback": function ( row, data, start, end, display ) {
          var api = this.api(), data;

          // converting to interger to find total
          var intVal = function ( i ) {
            return typeof i === 'string' ?
                i.replace(/[\$,]/g, '')*1 :
                typeof i === 'number' ?
                    i : 0;
          };

          // computing column Total of the complete result
          var Totalantal = api
          .column( 4 )
          .data()
          .reduce( function (a, b) {
              return intVal(a) + intVal(b);
          }, 0 );
          var nf1 = new Intl.NumberFormat();
          var totalantal_dec = nf1.format(Totalantal)

          var Totalind = api
              .column( 5 )
              .data()
              .reduce( function (a, b) {
                  return intVal(a) + intVal(b);
              }, 0 );
          var nf2 = new Intl.NumberFormat();
          var totalind_dec = nf2.format(Totalind)

          var Totalsum = api
              .column( 6 )
              .data()
              .reduce( function (a, b) {
                  return intVal(a) + intVal(b);
              }, 0 );
          var nf2 = new Intl.NumberFormat();
          var totalsum_dec = nf2.format(Totalsum)


          // Update footer by showing the total with the reference of the column index
          $( api.column( 4 ).footer() ).html('Total: ' + totalantal_dec);
          $( api.column( 5 ).footer() ).html('Total: ' + totalind_dec);
          $( api.column( 6 ).footer() ).html('Total: ' + totalsum_dec);
      }
  } );
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
  $('#post_sales').dataTable({
    dom: 'Bfrtip',
    buttons: [ 'copy', 'csv', 'excel' ],
    fixedHeader: true,
    "footerCallback": function ( row, data, start, end, display ) {
          var api = this.api(), data;

          // converting to interger to find total
          var intVal = function ( i ) {
            return typeof i === 'string' ?
                i.replace(/[\$,]/g, '')*1 :
                typeof i === 'number' ?
                    i : 0;
          };

          // computing column Total of the complete result
          var monTotal = api
              .column( 1 )
              .data()
              .reduce( function (a, b) {
                  return intVal(a) + intVal(b);
              }, 0 );

          // Update footer by showing the total with the reference of the column index
          $( api.column( 1 ).footer() ).html('Antal salg i alt: ' + monTotal);
      }
  } );
} );
