$(function(){
    // 鍒濆鍖朿heckbox浜嬩欢
    $('#rememberMe').iCheck({
        checkboxClass: 'icheckbox_square-green',
        increaseArea: '20%' // optional
    });

    // 鍔ㄦ€佺爜鐧婚檰鐨勬椂鍊欐牎楠屽拰杩涜鍊掕鏃�
    $("#casDynamicLoginForm").find("#getDynamicCode").click(function () {
        var username = $("#casDynamicLoginForm").find("#username");

        if (!checkRequired(username, "dynamicNameError")) {
            username.focus();
            return;
        }

        sendDynamicCodeByPhone(username.val(), "dynamicCodeType");
    });

    // 缁戝畾閫夐」鍗＄殑鐐瑰嚮浜嬩欢
//    $(".auth_tab_content_item[tabid=02]").hide();
    $(".auth_tab_links li").bind("click",function(){
        selectLi($(this));
    });

});

function loadFresh(){
    if(window != window.top){
        // 澶勭悊鍚屽煙鍚嶄笅鐨剅eload
        try{
            top.location.reload(true);
        }catch(ignoreErr){
        }
        // 澶勭悊璺ㄥ煙鎯呭喌涓嬬殑reload
        try{
            window.top.postMessage({type:"loginReload"},'*');
        }catch(ignoreErr){
        }
    }
}

function selectLi(obj){
    $(obj).siblings().removeClass("selected");
    $(obj).addClass("selected");
    var tabid = $(obj).attr("tabid");
    $(".auth_tab_content_item").hide();
    $(".auth_tab_content_item[tabid="+tabid+"]").show();
}