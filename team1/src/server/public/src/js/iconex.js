
var requestAddress = document.getElementById("request-address");
var responseAddress = document.getElementById("response-address");



window.addEventListener("ICONEX_RELAY_RESPONSE", eventHandler, false);

// type and payload are in event.detail
function eventHandler(event) {
    var type = event.detail.type;
    var payload = event.detail.payload;

    switch (type) {
        // connect iconex
        case "RESPONSE_ADDRESS":
            console.log("payload: "+payload)
            if(payload) {
                // alert(payload);
                location.href = "./main.html?address="+payload;
            }
            responseAddress.innerHTML = "> Selected ICX Address : " + payload;
            break;
    }
}

requestAddress.onclick = function () {
    window.dispatchEvent(new CustomEvent('ICONEX_RELAY_REQUEST', {
        detail: {
            type: 'REQUEST_ADDRESS'
        }
    }))
};



function images() {
    return 'to';
    // for (var i = 1; i <= 4; i++) {
    //     // append 메소드를 사용해서 이미지 추가 이름은 bg_01.jpg 같은 숫자 증가 형태
    //     /* $('.wrap').append('<img src="https://biketago.com/img/bg_thumb/bg_' + zeroFill(i, 2) + '.jpg">');--> */
    //     $('.wrap').append('<img src="../../img/card1.png">');
    // }

    // // wrap 클래스안의 모든 이미지가 로딩되면 masonry 적용
    // $imgs = $('.wrap').imagesLoaded(function () {
    //     $imgs.masonry({
    //         itemSelector: 'img', // img 태그를 대상으로 masonry 적용
    //         fitWidth: true,
    //         columnWidth: 10

    //     });
    // });

}