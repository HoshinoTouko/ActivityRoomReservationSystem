if(1){
    console.log('Test function running...');
    $("#name").val("TestName");
    $("#telephone").val('13012345678');
    $("#stuid").val('2016300012345');
    $("#password").val('123214');
    $("#starttime").val('08:00');
    $("#endtime").val('10:00');
    $("#reservdate").val('30 August, 2017');
    $("#forwhat").val('213213213');

}

$(function () {
    $("#submit").on("click",
        async function () {
            // Values init
            var name = $("#name").val();
            var telephone = $("#telephone").val();
            var stuid = $("#stuid").val();
            var password = $("#password").val();
            var starttime = $("#starttime").val();
            var endtime = $("#endtime").val();
            var reservdate = $("#reservdate").val();
            var room = $("#room").find("option:selected").text();
            var forwhat = $("#forwhat").val();

            var data = {
                name: name,
                telephone: telephone,
                stuid: stuid,
                password: password,
                starttime: starttime,
                endtime: endtime,
                reservdate: reservdate,
                room: room,
                forwhat: forwhat
            };
            console.log(data);
            // Post JSON
            // Frontend check data
            var checked = await is_valid()
                .then(function (checked) {
                    if (checked) {
                        // If checked
                        console.log(checked);
                        // Post data
                        $.post(
                            'api/add_reservation', data,
                            function (result) {
                                let json = JSON.parse(result);
                                Materialize.toast(json.tip, 4000);
                                console.log(json);
                                if (json.status == 1) {
                                    $('#reservation_form')[0].reset();
                                    $(document.body).animate({scrollTop: $('#inquire').offset().top}, 1000);
                                    // Refresh data
                                    refresh_future_data();
                                    refresh_past_data()
                                }
                            }
                        );
                    }
                }).catch(function (err) {
                    console.error(err);
                });
        }
    )
});


async function is_valid() {
    let result = true;
    $("#reservation_form").find("input,textarea").each(await function () {
        if (result) {
            if ($(this).val() == '') {
                Materialize.toast('未填写完整！', 4000);
                $(this).focus();
                result = false;
            }
        }
    })
    return await result;
}
