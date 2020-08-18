let users_data = {};


$(document).on('submit', '#estimate', e => {
    // デフォルトの処理(同じページに遷移する=保持しているデータが消える)を中止する
    e.preventDefault();
    let val = document.getElementById("estimate_gage").value;
    alert(val);
    users_data["data0"] = val;
    try {
        export_log();
    } catch (e) {
        return false;
    }

});


function export_log() {
    users_data["data1"] = 1;
    users_data["data2"] = 1;
    users_data["data3"] = 1;
    users_data["data4"] = 1;
    users_data["data5"] = 1;
    $.ajax({
        url: '/send_data/',
        type: "POST",
        async: false,
        data: {"data": JSON.stringify(users_data)},
        timeout: 50000
    })
        .done(function (response) {
            alert("データ送信成功");
        })
        .fail(function (jqXHR, textStatus, errorThrown) {
            alert("回答送信中にエラーが発生しました。再送信ボタンを押して再送信してください。何度も発生する場合は直接問い合わせてください");
            document.getElementById("resend").style.display = "block";
            throw 'Server Error';
        });
}