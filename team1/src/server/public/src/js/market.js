import IconService, { IconAmount, IconConverter, HttpProvider, IconWallet, IconBuilder, SignedTransaction } from 'icon-sdk-js';

const httpProvider = new HttpProvider('http://127.0.0.1:9000/api/v3');
const iconService = new IconService(httpProvider);
const CallBuilder = IconService.IconBuilder.CallBuilder;

// service 
const IcxTransactionBuilder = IconService.IconBuilder.IcxTransactionBuilder;
const signedTransaction = IconService.SignedTransaction;
const iconWallet = IconService.IconWallet;

// 커스텀 변수
var score_to = 'cxa6b3cb2b3a474412d7f0b870525213a8665c77ec';
var address = getParameterByAddress('address');


// var price_value = parseInt(document.getElementById('input_price').value);
// console.log("price_: "+price_value);
// console.log("price_value: "+price_value.value);

// 이벤트 핸들러
window.addEventListener("ICONEX_RELAY_RESPONSE", eventHandler, false);


var full_html = "";

// 경매장의 카드 보여줌
myCard();

document.getElementById('buyCard').addEventListener('click', async () => {
    $('#buyModal').hide();

    var player_id = document.getElementById('player_id').value;

    // 경매장에 있는 카드리스트를 가져옴
    var call = new CallBuilder()
        .from(address)
        .to(score_to)
        .method('getAuctionToken')
        .build()

    let myCards = await iconService.call(call).execute();
    
    console.log("myCards.length: "+myCards.length);
    console.log("myCards: "+myCards);
    console.log("myCards: "+typeof(myCards));
    
    // 빈 카드가 존재하기 때문에 빈카드 없앰!
    var cardList = [];
    for(var i=0; i<myCards.length; i++) {
        if(!myCards[i]) {
            continue;
        } 
        cardList.push(myCards[i]);
    }
    
    if(myCards.length < player_id) {
        alert("잘못된 입력!!");
        location.reload();
        
    } else {
        var selectCard = cardList[player_id-1];
        console.log("selectCard: "+selectCard);
        
        var card_str = selectCard.replace(/\'/gi, "\"");
        if(!card_str) {
            alert("잘못된 입력!!");
        }
        var card_property = JSON.parse(card_str);
        var price = String(card_property.price);

        console.log("price: "+price);
        // var card_address = card_property.address;

        console.log("price: "+typeof(price));
        // console.log("price: "+price);

        // console.log("player_id: "+ player_id);
        // console.log("CLICK BUY CARD");

        var callTransactionBuilder = new IconBuilder.CallTransactionBuilder;
        var callTransactionData = callTransactionBuilder
            .from(address)
            .to(score_to)
            .nid(IconConverter.toBigNumber(3))
            .value(IconAmount.of(Number(price), IconAmount.Unit.ICX).toLoop())
            .timestamp((new Date()).getTime() * 1000)
            .stepLimit(IconConverter.toBigNumber(10000000))
            .version(IconConverter.toBigNumber(3))
            .method('auctionBuy')
            .params({  
                "_playerId":player_id,
                "_price":price
            })
            .build();

        var score_sdk = JSON.stringify( {
            "jsonrpc":"2.0",
            "method":"icx_sendTransaction",
            "params":IconConverter.toRawTransaction(callTransactionData),
            "id":50889
        })

        var parsed = JSON.parse(score_sdk)
        console.log("parsed: "+parsed);

        window.dispatchEvent(new CustomEvent('ICONEX_RELAY_REQUEST', {
            detail: {
                type: 'REQUEST_JSON-RPC',
                payload: parsed,
            }
        }));
    }
});

// 이벤트 핸들러 - ICONex
function eventHandler(event) {
    var type = event.detail.type;
    var payload = event.detail.payload;

    switch (type) {
        case "RESPONSE_JSON-RPC":
            console.log("RESPONSE_JSON-RPC: "+JSON.stringify(payload));
            location.reload();

            break;
        case "CANCEL_JSON-RPC":
            console.log("CANCEL_JSON-RPC");
            location.reload();
            break;
        case "RESPONSE_SIGNING":
            console.log("RESPONSE_SIGNING6");
            location.reload();
            break;
        case "CANCEL_SIGNING":
            console.log("CANCEL_SIGNING");
            location.reload();
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
        .method('getAuctionToken')
        .build()

    let myCards = await iconService.call(call).execute();
    console.log("myCards: "+myCards);
    console.log("showAllCard: "+myCards);


     images(myCards)
}

// 자신이 소유한 카드들을 보여주는 함수
async function images(cards) {
    // Bryant_N / Cury_N / Griffin_N / Harden_N / Hayward_N / Irving_N / Jordan_N / Lebron_N
    // player = ['Bryant', 'Cury', 'Griffin', 'Harden', 'Hayward', 'Irving', 'Jordan', 'Lebron' ]
// {'address': <iconservice.base.address.Address object at 0x108fd9f28>, 
// 'property': {'player': 'Griffin', 'run': 306, 'power': 355, 'dribble': 390}, 'price': 1}

    var cardCount = cards.length;
    console.log("cardCount: "+cardCount);
    // var card_property;
    // console.log("card_property: "+card_property);
    var grade;
    
    // for(var i=0; i<cardCount; i++) {
    //     $('#basic').html(html);
    // }

    for(var i=0; i<cardCount; i++) {
        var card = cards[i];
        console.log("card: "+card);
        var card_str = card.replace(/\'/gi, "\"");

        console.log("card_str:"+card_str);
        console.log("card_str:"+typeof(card_str));
        
        if( !card_str) {
            console.log("데이터 없음!");
            continue;
        }

        var cardObject = JSON.parse(card_str);

        var cardOwner = cardObject["address"];
        var cardPrice = cardObject["price"];

        var cardInfo =  cardObject["property"];

        var tokenId = cardInfo["tokenId"];
        var cardPlayer = cardInfo["player"];
        var cardRun = cardInfo["run"];
        var cardPower = cardInfo["power"];
        var cardDribble = cardInfo["dribble"];
        
        console.log("tokenID: "+tokenId);


        // console.log("address"+ cardObject["address"]);
        // console.log("property"+ cardObject["property"]);
        // console.log("price"+ cardObject["price"]);

        // console.log(typeof(card_property));
        // console.log(card_property.player);
        // console.log(card_property.dribble);
        // console.log(card_property.power);
        // console.log(card_property.run);

        if(cardRun >= 300) {
            grade = 'S';
        } else if ( cardRun >= 200) {
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
            html += '<img src="../../img/player/'+cardPlayer+'_'+grade+'.png" style="weight:400px; height:280px;">'
            html += '</div>';  
        html += '<div id="back'+i+'" class="back">'; 
        html += '<span id="cardinfo" class="tableNo" style="margin-left: 45px; margin-top:100px; color: #0b0b0b;">';
        html += '<h6> run:'+cardRun+' <br>'+'dribble:'+cardDribble+' <br>'+'power:'+cardPower+' <br><br>'+cardPlayer+'<br><br><font color="red">'+cardPrice+' ICX </font></h6></span>'
        html += '<img src="../../img/player/'+cardPlayer+'_'+grade+'_back.png" style="weight:400px; height:280px;">'
        html += '<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#buyModal" style="margin-bottom:100px"> BUY CARD </button>';
        html += '</div>';
        html += '</div>';
        html += '</div>';
        html += '</div>';
        html += '</div>';
        html += '</div>';
        
        $('#basic').append(html);

        // full_html += html; 
    }
}

// get방식으로 넘어온 address 를 리턴함
function getParameterByAddress(address) {
    var address = address.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + address + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}