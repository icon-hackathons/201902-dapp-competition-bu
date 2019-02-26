import IconService, { IconAmount, IconConverter, HttpProvider, IconWallet, IconBuilder, SignedTransaction } from 'icon-sdk-js';

const httpProvider = new HttpProvider('http://127.0.0.1:9000/api/v3');
const iconService = new IconService(httpProvider);
const CallBuilder = IconService.IconBuilder.CallBuilder;

// service 
const IcxTransactionBuilder = IconService.IconBuilder.IcxTransactionBuilder;
const signedTransaction = IconService.SignedTransaction;
const iconWallet = IconService.IconWallet;

// 커스텀 변수
var score_to = 'cxdacd3169934b4da8ab0141c5f6c2b74ce320fd67';
// var addr_to = 'hxc22ae778606f626c03815a5adc41da4a1dad6b4f';
var address = getParameterByAddress('address');


// var price_value = parseInt(document.getElementById('input_price').value);
// console.log("price_: "+price_value);
// console.log("price_value: "+price_value.value);

// 이벤트 핸들러
window.addEventListener("ICONEX_RELAY_RESPONSE", eventHandler, false);


var full_html = "";

// 경매장의 카드 보여줌
myCard();


// 이벤트 핸들러 - ICONex
function eventHandler(event) {
    var type = event.detail.type;
    var payload = event.detail.payload;

    switch (type) {
        case "RESPONSE_JSON-RPC":
            console.log("RESPONSE_JSON-RPC: "+JSON.stringify(payload));
            break;
        case "CANCEL_JSON-RPC":
            console.log("CANCEL_JSON-RPC");
            break;
        case "RESPONSE_SIGNING":
            console.log("RESPONSE_SIGNING6");
            break;
        case "CANCEL_SIGNING":
            console.log("CANCEL_SIGNING");
            break;
        default:
    }
}

// SCORE 랑 통신하여 소유자의 카드갯수를 반환
async function myCard() {
    // console.log("exe myCard()");
    var call = new CallBuilder()
        .from(address)
        .to(score_to)
        .method('auction_results')
        .build()

    let myCards = await iconService.call(call).execute();
    console.log("showAllCard: "+myCards);

     images(myCards)
}

// 자신이 소유한 카드들을 보여주는 함수
async function images(cards) {
    // Bryant_N / Cury_N / Griffin_N / Harden_N / Hayward_N / Irving_N / Jordan_N / Lebron_N
    // player = ['Bryant', 'Cury', 'Griffin', 'Harden', 'Hayward', 'Irving', 'Jordan', 'Lebron' ]
// {'address': <iconservice.base.address.Address object at 0x108fd9f28>, 
// 'property': {'player': 'Griffin', 'run': 306, 'power': 355, 'dribble': 390}, 'price': 1}

    console.log("exe images");

    var cardCount = cards.length;
    console.log("cardCount: "+cardCount);
    var card_property;
    console.log("card_property: "+card_property);
    var grade;
    
    // for(var i=0; i<cardCount; i++) {
    //     $('#basic').html(html);
    // }

    for(var i=0; i<cardCount; i++) {
        var card = cards[i];
        var card_str = card.replace(/\'/gi, "\"");

        console.log("card_str:"+card_str);
        console.log("card_str:"+typeof(card_str));

        card_property = JSON.parse(card_str);
        console.log(typeof(card_property));
        console.log(card_property.player);
        console.log(card_property.dribble);
        console.log(card_property.power);
        console.log(card_property.run);

        if(card_property.run >= 300) {
            grade = 'S';
        } else if ( card_property.run >= 200) {
            grade = "R";
        } else {
            grade = 'N';
        }

        var html = "";

        html += '<div class="card card-personal col-xs-3" style="margin-top:40px; height:350px; margin-left:90px;">';
        html += '<div class="card-body">';

        html += '<div class="flip-container" style="margin-bottom:30px; height:100px;">'; 
        html += '<div class="flipper">';
        html += '<div id="front" class="front"> '
            html += '<img src="../../img/player/'+card_property.player+'_'+grade+'.png" style="weight:400px; height:280px;">'
            html += '</div>';  
        html += '<div id="back'+i+'" class="back">'; 
        html += '<span id="cardinfo" class="tableNo" style="margin-left: 45px; margin-top:100px; color: #0b0b0b;">';
        html += '<h6> run:'+card_property.run+' <br>'+'dribble:'+card_property.dribble+' <br>'+'power:'+card_property.power+' 
<br><br><br>'+card_property.player+'</h6></span>'
        html += '<img src="../../img/player/'+card_property.player+'_'+grade+'_back.png" style="weight:400px; height:280px;">'
        html += '<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#sellModal" 
style="margin-bottom:100px">sell card </button>';
        html += '</div>';
        html += '</div>';
        html += '</div>';
        html += '</div>';
        html += '</div>';

        html += '</div>';
        
        $('#basic').append(html);

        full_html += html; 
    }
}


// get방식으로 넘어온 address 를 리턴함
function getParameterByAddress(address) {
    var address = address.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + address + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}

