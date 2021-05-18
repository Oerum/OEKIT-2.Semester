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
  $('#table_generelt').DataTable( {
    dom: 'Bfrtip',
    buttons: [ 'copy', 'csv', 'excel' ],
    fixedHeader: true,
      "footerCallback": function ( row, data, start, end, display ) {
          var api = this.api(), data;

          // Remove the formatting to get integer data for summation
          var intVal = function ( i ) {
              return typeof i === 'string' ?
                  i.replace(/[\$,]/g, '')*1 :
                  typeof i === 'number' ?
                      i : 0;
          };

          // Total over all pages
          total = api
              .column( 1 )
              .data()
              .reduce( function (a, b) {
                  return intVal(a) + intVal(b);
              }, 0 );
              var nf1 = new Intl.NumberFormat();
              var total_dec = nf1.format(total)

          // Total over this page
          pageTotal = api
              .column( 1, { page: 'current'} )
              .data()
              .reduce( function (a, b) {
                  return intVal(a) + intVal(b);
              }, 0 );
              var nf2 = new Intl.NumberFormat();
              var pagetotal_dec = nf2.format(pageTotal)

          // Update footer
          $( api.column( 1 ).footer() ).html(
              'Pr. Side: ' + pagetotal_dec + ' --- ' + 'Total beløb: ' + total_dec
          );
      }
  } );
} );


/* Supply_table convert to datatable*/
$(document).ready(function() {
  $('#supply_table').DataTable( {
    dom: 'Bfrtip',
    buttons: [ 'copy', 'csv', 'excel' ],
    fixedHeader: true,
      "footerCallback": function ( row, data, start, end, display ) {
          var api = this.api(), data;

          // Remove the formatting to get integer data for summation
          var intVal = function ( i ) {
              return typeof i === 'string' ?
                  i.replace(/[\$,]/g, '')*1 :
                  typeof i === 'number' ?
                      i : 0;
          };

          // Total over all pages
          total_antal = api
              .column( 4 )
              .data()
              .reduce( function (a, b) {
                  return intVal(a) + intVal(b);
              }, 0 );
              var nf1 = new Intl.NumberFormat();
              var totalantal_dec = nf1.format(total_antal)

          // Total over this page
          pageTotal_antal = api
              .column( 4, { page: 'current'} )
              .data()
              .reduce( function (a, b) {
                  return intVal(a) + intVal(b);
              }, 0 );
              var nf2 = new Intl.NumberFormat();
              var pagetotalantal_dec = nf2.format(pageTotal_antal)

          // Total over all pages
          total_indk = api
          .column( 5 )
          .data()
          .reduce( function (a, b) {
              return intVal(a) + intVal(b);
          }, 0 );
          var nf3 = new Intl.NumberFormat();
          var totalindk_dec = nf3.format(total_indk)

        // Total over this page
        pageTotal_indk = api
            .column( 5, { page: 'current'} )
            .data()
            .reduce( function (a, b) {
                return intVal(a) + intVal(b);
            }, 0 );
            var nf4 = new Intl.NumberFormat();
            var pagetotalindk_dec = nf4.format(pageTotal_indk)

        // Total over all pages
        total_sum = api
        .column( 6 )
        .data()
        .reduce( function (a, b) {
            return intVal(a) + intVal(b);
        }, 0 );
        var nf5 = new Intl.NumberFormat();
        var totalsum_dec = nf5.format(total_sum)

        // Total over this page
        pageTotal_sum = api
            .column( 6, { page: 'current'} )
            .data()
            .reduce( function (a, b) {
                return intVal(a) + intVal(b);
            }, 0 );
            var nf6 = new Intl.NumberFormat();
            var pagetotalsum_dec = nf6.format(pageTotal_sum)

        var revenue = total_sum-total_indk
        var nf7 = new Intl.NumberFormat();
        var revenue_dec = nf7.format(revenue)

          // Update footer
          $( api.column( 4 ).footer() ).html('Pr. Side: ' + pagetotalantal_dec + ' ____________ ' + 'Total antal: ' + totalantal_dec);
          $( api.column( 5 ).footer() ).html('Pr. Side: '+ pagetotalindk_dec + ' ________________________ ' + 'Total beløb: ' + totalindk_dec);
          $( api.column( 6 ).footer() ).html('Pr. Side: '+ pagetotalsum_dec + ' _____________________ ' + ' Total antal: ' + totalsum_dec + ' _____________________ ' +  'Total indtjening: ' + revenue_dec);

      }
  } );
} );





/* table_erhverv convert to datatable*/
$(document).ready(function() {
  $('#post_sales').DataTable( {
    dom: 'Bfrtip',
    buttons: [ 'copy', 'csv', 'excel' ],
    fixedHeader: true,
      "footerCallback": function ( row, data, start, end, display ) {
          var api = this.api(), data;

          // Remove the formatting to get integer data for summation
          var intVal = function ( i ) {
              return typeof i === 'string' ?
                  i.replace(/[\$,]/g, '')*1 :
                  typeof i === 'number' ?
                      i : 0;
          };

          // Total over all pages
          total = api
          .column( 1 )
          .data()
          .reduce( function (a, b) {
              return intVal(a) + intVal(b);
          }, 0 );
          var nf1 = new Intl.NumberFormat();
          var total_dec = nf1.format(total)

          // Total over this page
          pageTotal = api
              .column( 1, { page: 'current'} )
              .data()
              .reduce( function (a, b) {
                  return intVal(a) + intVal(b);
              }, 0 );
              var nf2 = new Intl.NumberFormat();
              var pagetotal_dec = nf2.format(pageTotal)

            // Update footer
            $( api.column( 1 ).footer() ).html('Pr. Side: '+ pagetotal_dec + ' - ' +  'Total salg: ' + total_dec);
      }
  } );
} );
