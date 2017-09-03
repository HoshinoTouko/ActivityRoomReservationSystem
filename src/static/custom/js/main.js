//Index page function
function refresh_future_data(){
    $('#future_reservation_info').empty();
    $.post(
        'api/get_future_reservation', [],
        function (result) {
            let json = JSON.parse(result);
            count = 0;
            json.forEach(function(item) {
                var time_text = item.reservdate + ' ' + item.starttime + ' - ' + item.endtime;
                var name_text = item.name;
                var room_text = item.room;
                var status_text = '未通过';
                switch (item.status){
                    case '0':
                        status_text = '待确认';
                        break;
                    case '1':
                        status_text = '已通过';
                        break;
                    case '-1':
                    default:
                        status_text = '未通过';
                        break;
                }
                final_html = '<tr>'
                        + '<td>' + time_text + '</td>'
                        + '<td>' + name_text + '</td>'
                        + '<td>' + room_text + '</td>'
                        + '<td>' + status_text + '</td>'
                        + '</tr>';
                $('#future_reservation_info').append(final_html);
                count++;
            }, this);
            if (count == 0){
                final_html = '<tr><td>暂时没有预约</td><td></td><td></td><td> </td></tr>';
                $('#future_reservation_info').append(final_html);
            }
        }
    );
}
function refresh_past_data(){
    $('#past_reservation_info').empty();
    $.post(
        'api/get_past_reservation', [],
        function (result) {
            let json = JSON.parse(result);
            count = 0;
            json.forEach(function(item) {
                var time_text = item.reservdate + ' ' + item.starttime + ' - ' + item.endtime;
                var name_text = item.name;
                var room_text = item.room;
                var status_text = '未通过';
                switch (item.status){
                    case '0':
                        status_text = '待确认';
                        break;
                    case '1':
                        status_text = '已通过';
                        break;
                    case '-1':
                    default:
                        status_text = '未通过';
                        break;
                }
                final_html = '<tr>'
                        + '<td>' + time_text + '</td>'
                        + '<td>' + name_text + '</td>'
                        + '<td>' + room_text + '</td>'
                        + '<td>' + status_text + '</td>'
                        + '</tr>';
                $('#past_reservation_info').append(final_html);
                count++;
            }, this);
            if (count == 0){
                final_html = '<tr><td>暂时没有预约</td><td></td><td></td><td></td></tr>';
                $('#past_reservation_info').append(final_html);
            }
        }
    );
}

// Materializecss jQuery Plugin Initialization
$('.button-collapse').sideNav();
$(document).ready(function () {
    $('select').material_select();

    $('.scrollspy').scrollSpy();

    $('.collapsible').collapsible();

    $('ul.tabs').tabs();
    $('#admin-tabs-swipe').tabs({ 'swipeable': true });

    refresh_future_data();
    refresh_past_data();    
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