function pass_reservation(reservation_id){
    $.post(
        '/admin/api/pass_reservation', {id: reservation_id},
        function (result) {
            if (result == '1'){
                $('#reservation-' + reservation_id).removeClass('red').removeClass('blue').addClass('green');
                $('#reservation_title-' + reservation_id).empty().append('已审核：通过');
                Materialize.toast('成功！', 4000);
            }
            else{
                Materialize.toast('失败！', 4000);
            }
        }
    );
}
function pend_reservation(reservation_id){
    $.post(
        '/admin/api/pend_reservation', {id: reservation_id},
        function (result) {
            if (result == '1'){
                $('#reservation-' + reservation_id).removeClass('green').removeClass('red').addClass('blue');
                $('#reservation_title-' + reservation_id).empty().append('待审核');
                Materialize.toast('成功！', 4000);
            }
            else{
                Materialize.toast('失败！', 4000);
            }
        }
    );
}
function refuse_reservation(reservation_id){
    $.post(
        '/admin/api/refuse_reservation', {id: reservation_id},
        function (result) {
            if (result == '1'){
                $('#reservation-' + reservation_id).removeClass('green').removeClass('blue').addClass('red');
                $('#reservation_title-' + reservation_id).empty().append('已审核：拒绝');
                Materialize.toast('成功！', 4000);
            }
            else{
                Materialize.toast('失败！', 4000);
            }
        }
    );
}
