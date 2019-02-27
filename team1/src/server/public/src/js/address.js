
// ################# card.html #################
// main.html 메인화면으로 이동
function goMyTeam() {
    var address = getParameterByAddress("address");
    location.href = "./main.html?address="+address;
}



// ################# main.html  #################
// 경매 화면으로 이동
function goMarket() {
    var address = getParameterByAddress("address");
    location.href = "./market.html?address="+address;
}

// 상자깡 화면으로 이동
function buyCard() {
    var address = getParameterByAddress("address");
    location.href = "./card.html?address="+address;
}

function goGame() {
    var address = getParameterByAddress("address");
    location.href = "./gamepage.html?address="+address;
}

// get방식으로 넘어온 address 를 리턴함
function getParameterByAddress(address) {
    var address = address.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + address + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}
