//Index page function
function resolve_info(item){
    switch (item.status){
        case '0':
            status_text = '待确认';
            class_text = 'blue lighten-5';
            break;
        case '1':
            status_text = '已通过';
            class_text = 'green lighten-5';
            break;
        case '-1':
        default:
            status_text = '未通过';
            class_text = 'red lighten-5';
            break;
    }
    var final_html = formatString(
        '<tr {class_text}> <td> {time_text} </td> <td> {name_text} </td> <td> {room_text} </td> <td> {status_text} </td></tr>', {
            class_text: 'class="' + class_text + '"',
            time_text: item.reservdate + ' ' + item.starttime + ' - ' + item.endtime,
            name_text: item.name + ' ' + item.stuid,
            room_text: item.room,
            status_text: status_text
        }
    );
    return final_html;
}
function resolve_no_info(){
    return '<tr><td>暂时没有预约</td><td></td><td></td><td> </td></tr>';
}

function refresh_future_data(){
    $('#future_reservation_info').empty();
    $.post(
        '/api/get_future_reservation', [],
        function (result) {
            var json = JSON.parse(result);
            count = 0;
            json.forEach(function(item) {
                var final_html = resolve_info(item);
                $('#future_reservation_info').append(final_html);
                count++;
            }, this);
            if (count == 0){
                final_html = resolve_no_info();
                $('#future_reservation_info').append(final_html);
            }
        }
    );
}
function refresh_past_data(){
    $('#past_reservation_info').empty();
    $.post(
        '/api/get_past_reservation', [],
        function (result) {
            var json = JSON.parse(result);
            count = 0;
            json.forEach(function(item) {
                var final_html = resolve_info(item);
                $('#past_reservation_info').append(final_html);
                count++;
            }, this);
            if (count == 0){
                final_html = resolve_no_info();
                $('#past_reservation_info').append(final_html);
            }
        }
    );
}

// When click fresh buttom, refresh reservation list.


// Materializecss jQuery Plugin Initialization
$('.button-collapse').sideNav();
$(document).ready(function () {
    $('select').material_select();

    $('.scrollspy').scrollSpy();

    $('.collapsible').collapsible();

    $('ul.tabs').tabs();
    $('#admin-tabs-swipe').tabs({ 'swipeable': true });
    
    $('.modal').modal();    
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