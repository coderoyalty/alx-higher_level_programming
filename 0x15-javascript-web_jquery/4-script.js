// toggle classes using jquery
$(document).ready(function () {
  $('div#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
});
