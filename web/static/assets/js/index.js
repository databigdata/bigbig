function addValue() {
    // if (sessionStorage.name != undefined || sessionStorage.name != null || sessionStorage.name != "") {
    //     if(window.document.getElementById("tag-input-33") != null) {
    //         // var data = sessionStorage.name.toString().split(", ");
    //         $('#tag-input-33').tokenfield();
    //         for (var i = 0; i < data.length; i++) {
    //             $('#tag-input-33').tokenfield('createToken', data[i]);
    //         }
    //     }
    //     console.log(sessionStorage.name);
    // }
    // if(sessionStorage.temp != undefined || sessionStorage.temp != null || sessionStorage.temp != "") {
    //     console.log(sessionStorage.temp);
    //      if(window.document.getElementById("tag-input") != null)
    //          console.log("tag-input True");
    //          $('#tag-input').tokenfield();
    //          var data = sessionStorage.temp.toString().split(", ");
    //          for(var i=0; i<data.length; i++){
    //              $("#tag-input").tokenfield('createToken', data[i]);
    //          }
    // }
    // console.log("onload1" + window.document.getElementById("tag-input-33").value);
    // console.log("onload2" + window.document.getElementsByClassName("close").value);
    // console.log("onload2" + window.document.getElementsByClassName("close"));
}


// 페이지 로드시
window.onload = addValue();


//페이지 벗어났을 때
window.onbeforeunload = function () {
    console.log(window.location.pathname);
    console.log(window.location.pathname.toString());
    console.log(window.location.pathname.toString().indexOf("query"));
    if((window.location.pathname.toString()).indexOf("query") == -1){
        sessionStorage.name = "";
        sessionStorage.temp = "";
    }

}

//보류
function bClick() {
    console.log("bClick");
}

//

window.document.getElementById("rc").addEventListener("click", bClick);
window.document.getElementById("recommend").addEventListener("click", bClick);
window.document.getElementById("caution").addEventListener("click", bClick);

(function () {
    $("#tag-input-33").tokenfield();
     $("#tag-input").tokenfield();
    $("#tokenlist-loaded").tokenfield();

    $("submit").on('click', function (e) {
        e.preventDefault();
        console.log("sdfs");
        // console.log("1"+ window.document.getElementById("tag-input-33").value);
        console.log("3" + $("#tag-input-33").tokenfield('getTokensList'));
        console.log("4" + $("#tag-input").tokenfield('getTokensList'));
        var form = document.find;
        form.submit();
        if (sessionStorage.name == null || sessionStorage.name == "") {
            console.log('sessionStorage.name null');
            sessionStorage.name = $("#tag-input-33").tokenfield('getTokensList');
        }
        else {
            sessionStorage.name = $("#tag-input-33").tokenfield('getTokensList');
            console.log('sessionStorage.name : ' + sessionStorage.name);

        }

         if (sessionStorage.temp == null || sessionStorage.temp == "") {
            console.log('sessionStorage.name null');
            sessionStorage.temp = $("#tag-input").tokenfield('getTokensList');
        }
        else {
            sessionStorage.temp = $("#tag-input").tokenfield('getTokensList');
            console.log('sessionStorage.temp : ' + sessionStorage.temp);
        }



        return $("#tokenlist-1").val($("#tag-input-33").tokenfield('getTokensList'));
    });

}).call(this);
