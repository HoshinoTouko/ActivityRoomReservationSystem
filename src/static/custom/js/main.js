

// Materializecss jQuery Plugin Initialization
$(".button-collapse").sideNav();
$(document).ready(function () {
    $('select').material_select();

    $('.scrollspy').scrollSpy();

    $('.collapsible').collapsible();

    $('ul.tabs').tabs();
    $('#admin-tabs-swipe').tabs({ 'swipeable': true });
});

// Materializecss scrolFire
$(document).ready(function () {
    var options = [
        {
            selector: '.list-scrollFire', offset: 0, callback: function (el) {
                Materialize.showStaggeredList($(el));
            }
        }
    ];
    Materialize.scrollFire(options);
});


// Time picker
$('.timepicker').pickatime({
    default: '8:00', // Set default time: 'now', '1:30AM', '16:30'
    fromnow: 0,       // set default time to * milliseconds from now (using with default = 'now')
    twelvehour: false, // Use AM/PM or 24-hour format
    donetext: 'OK', // text for done-button
    cleartext: 'Clear', // text for clear-button
    canceltext: 'Cancel', // Text for cancel-button
    autoclose: true, // automatic close timepicker
    ampmclickable: true, // make AM PM clickable
    aftershow: function () { } //Function for after opening timepicker
});
// Date picker
$('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 1, // Creates a dropdown of 15 years to control year,
    today: 'Today',
    clear: 'Clear',
    close: 'Ok',
    closeOnSelect: true // Close upon selecting a date,
});