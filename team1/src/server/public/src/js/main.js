// 아이콘 2초 ㅋㅋㅋㅋ 10초걸리는데??ㅋㅋㅋㅋ  (로컬이라서 그런가?)

import IconService, { IconAmount, IconConverter, HttpProvider, IconWallet, IconBuilder, SignedTransaction } from 'icon-sdk-js';
// import cheerio from 'cheerio';
const cheerio = require('cheerio');


// console.log("cheerio: "+cheerio);
// httpProvider = new HttpProvider();
const httpProvider = new HttpProvider('http://127.0.0.1:9000/api/v3');
const iconService = new IconService(httpProvider);
const CallBuilder = IconService.IconBuilder.CallBuilder;

// service 
const IcxTransactionBuilder = IconService.IconBuilder.IcxTransactionBuilder;
const signedTransaction = IconService.SignedTransaction;
const iconWallet = IconService.IconWallet;

// 커스텀 변수
var score_to = 'cxdacd3169934b4da8ab0141c5f6c2b74ce320fd67';
var addr_to = 'hxc22ae778606f626c03815a5adc41da4a1dad6b4f';
var address = getParameterByAddress('address');

// var price_value = parseInt(document.getElementById('input_price').value);
// console.log("price_: "+price_value);
// console.log("price_value: "+price_value.value);

// 이벤트 핸들러
window.addEventListener("ICONEX_RELAY_RESPONSE", eventHandler, false);

let current = '';
var full_html = "";

// 로딩바 바로 사라지게하기 위해
$('#loading').hide();  


// 소유자의 카드 보여줌
myCard();


// 게임 시작 버튼 클릭시
document.getElementById('gameStart').addEventListener('click', async () => {
    $('#modal').hide();
    var date = new Date();
    // currentTime = date.getTime();
    current = String(date.getTime());
    
    // console.log("date.getTime(): "+date.getTime());
    console.log("gameStart()1, current: "+current)
    console.log("gameStart()1, current: "+typeof(current))

    // await this.readFile();
    var price = parseInt(document.getElementById('betting_price').value);

    // var price = Number(price_value);
    // console.log("price: "+price);
    console.log("price: "+typeof(price));
    
    var callTransactionBuilder = new IconBuilder.CallTransactionBuilder;
    var callTransactionData = callTransactionBuilder
        .from(address)
        .to(score_to)
        .nid(IconConverter.toBigNumber(3))
        .value(IconAmount.of(Number(price), IconAmount.Unit.ICX).toLoop())
        .timestamp((new Date()).getTime() * 1000)
        .stepLimit(IconConverter.toBigNumber(10000000))
        .version(IconConverter.toBigNumber(3))
        .method('startGame')
        .params({  
            "_time": current
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

    $('#loading').show();
});

document.getElementById('sellCard').addEventListener('click', async () => {
    $('#modal').hide();

    var player_id = document.getElementById('player_id').value;
    var player_price = document.getElementById('player_price').value;

    console.log("player_id: "+ player_id);
    console.log("player_price: "+ player_price);

    playerSell(player_id)


});


// 이벤트 핸들러 - ICONex
function eventHandler(event) {
    var type = event.detail.type;
    var payload = event.detail.payload;

    switch (type) {
        case "RESPONSE_JSON-RPC":
            console.log("RESPONSE_JSON-RPC: "+JSON.stringify(payload));
            
            sleep(10000);
            gemeResult();
            $('#loading').hide();

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


// 게임한 결과를 가져옴
async function gemeResult() {
    current = String(current)
    if(current === '') {
        console.log("에러!!");
    } else {
        var call = new CallBuilder()
        .from(address)
        .to(score_to)
        .method('getGameResult')
        .params({
            "_time":current
        })
        .build()

        var gameResult = await iconService.call(call).execute(); 
        if(gameResult == 1) {
            window.open("../../win.html", "a", "width=500, height=500, left=520, top=100");
            console.log("win, You earned an icx.");
        } else if(gameResult == 0) {
            window.open("../../lose.html", "a", "width=500, height=500, left=520, top=100");
            console.log("lose, At the  time.");
        } else {next
            alert("에러!!")
        }
    }
}

// SCORE 랑 통신하여 소유자의 카드갯수를 반환
async function myCard() {

    // console.log("exe myCard()");
    var call = new CallBuilder()
        .from(address)
        .to(score_to)
        .method('showAllCard')
        .build()

    let myCards = await iconService.call(call).execute();
    console.log("showAllCard: "+myCards);

    images(myCards)
}

// 자신이 소유한 카드들을 보여주는 함수
async function images(cards) {
    // Bryant_N / Cury_N / Griffin_N / Harden_N / Hayward_N / Irving_N / Jordan_N / Lebron_N
    // player = ['Bryant', 'Cury', 'Griffin', 'Harden', 'Hayward', 'Irving', 'Jordan', 'Lebron' ]

    var cardCount = cards.length;
    var card_property;
    var grade;

    // for(var i=0; i<cardCount; i++) {
    //     $('#basic').html(html);
    // }

    for(var i=0; i<cardCount; i++) {
        var card = cards[i];
        var card_str = card.replace(/\'/gi, "\"");

        card_property = JSON.parse(card_str);
        // console.log(typeof(card_property));
        // console.log(card_property.player);
        // console.log(card_property.dribble);
        // console.log(card_property.power);
        // console.log(card_property.run);

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
        html += '<h6> run:'+card_property.run+' <br>'+'dribble:'+card_property.dribble+' <br>'+'power:'+card_property.power+' <br><br><br>'+card_property.player+'</h6></span>'
        html += '<img src="../../img/player/'+card_property.player+'_'+grade+'_back.png" style="weight:400px; height:280px;">'
        html += '<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#sellModal" style="margin-bottom:100px">sell card </button>';
                // <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#sellModal" style="margin-bottom:150px">Let's GAME  </button>
        html += '</div>';
        html += '</div>';
        html += '</div>';
        html += '</div>';
        html += '</div>';

        html += '</div>';
        
        $('#basic').append(html);

        full_html += html;

        
    }
    // console.log("card_property="+card_property);
}

// get방식으로 넘어온 address 를 리턴함
function getParameterByAddress(address) {
    var address = address.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + address + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}

// 아이콘 블록체인에 맞게 설정
function sleep (delay) {
    var start = new Date().getTime();
    while (new Date().getTime() < start + delay);
 }
 
 
// 
function playerSell(player_id) {
    //  컴퓨터는 0부터  
    player_id -= 1;
    
    var playerInfo = "";
    
    var $ = cheerio.load(full_html);
    
    var class_a = $('h6', 'span', $('#back'+player_id));
        
    class_a.each(function () {
        playerInfo = $(this).text();
        // console.log("선수들 정보: "+$(this).text());
    });

    // console.log("playerInfo: "+playerInfo);
    var splitInfo = playerInfo.split(" ");

    // console.log("splitInfo: "+splitInfo);
    // console.log("splitInfo: "+typeof(splitInfo));

    // for(var i=0; i<splitInfo.length; i++) {
    //     console.log(" "+splitInfo[i]);
    // }

    // console.log(splitInfo[1].split(":"));
    // console.log(splitInfo[2].split(":"));
    // console.log(splitInfo[3].split(":"));
    // console.log(splitInfo[4].split(":"));


    var run = splitInfo[1].split(":")[1];
    var dribble = splitInfo[2].split(":")[1];
    var power = splitInfo[3].split(":")[1];
    var name = splitInfo[4];

    console.log("run: "+run);
    console.log("dribble: "+dribble);
    console.log("power: "+power);
    console.log("name: "+name);
   
    // var player_name = playerInfo

}


//  // create container
        // var div = document.createElement('div');
        // div.id = "flip-container";
        // div.innerHTML = document.getElementById('container my-auto').innerHTML;
        // document.getElementById('container').appendChild(div);

        // create container-fluid
        // var div = document.createElement('div');
        // div.innerHTML = document.getElementById('container').innerHTML;
        // document.getElementById('container-fluid').appendChild(div);

        // // create col-xs-12
        // var div = document.createElement('div');
        // div.innerHTML = document.getElementById('ontainer-fluid').innerHTML;
        // document.getElementById('row col-xs-12').appendChild(div);

        // // create card card-personal col-xs-3
        // var div = document.createElement('div');
        // div.innerHTML = document.getElementById('row col-xs-12').innerHTML;
        // document.getElementById('card card-personal col-xs-3').append('style="margin-top:40px; height:350px; margin-left:90px;"').appendChild(div);

        // // create card-body
        // var div = document.createElement('div');
        // div.innerHTML = document.getElementById('card card-personal col-xs-3').innerHTML;
        // document.getElementById('card-body').append('style="margin-top:40px; height:350px; margin-left:90px;"').appendChild(div);

        // // create flip-container
        // var div = document.createElement('div');
        // div.innerHTML = document.getElementById('card-body').innerHTML;
        // document.getElementById('flip-container').append('style="margin-bottom:30px; height:100px;"').appendChild(div);


// sell card()
    // var info = "#back"+player_id;
    // 선수들의 정보 가져옴
    // var $ = cheerio.load(full_html);
    // var class_a = $('h6', 'span', $("#back"+player_id));

    // // consol
    // class_a.each(function () {
    //     console.log($(this).text());
    // });

    // console.log("full_html: "+full_html);
    // test(full_html);
    // var date = new Date();
    // // currentTime = date.getTime();
    // current = String(date.getTime());
    
    // // console.log("date.getTime(): "+date.getTime());
    // console.log("gameStart()1, current: "+current)
    // console.log("gameStart()1, current: "+typeof(current))

    // // await this.readFile();
    // var price = parseInt(document.getElementById('price_number').value);

    // // var price = Number(price_value);
    // // console.log("price: "+price);
    // console.log("price: "+typeof(price));
    
    // var callTransactionBuilder = new IconBuilder.CallTransactionBuilder;
    // var callTransactionData = callTransactionBuilder
    //     .from(address)
    //     .to(score_to)
    //     .nid(IconConverter.toBigNumber(3))
    //     .value(IconAmount.of(Number(price), IconAmount.Unit.ICX).toLoop())
    //     .timestamp((new Date()).getTime() * 1000)
    //     .stepLimit(IconConverter.toBigNumber(10000000))
    //     .version(IconConverter.toBigNumber(3))
    //     .method('startGame')
    //     .params({  
    //         "_time": current
    //     })
    //     .build();

    // var score_sdk = JSON.stringify( {
    //     "jsonrpc":"2.0",
    //     "method":"icx_sendTransaction",
    //     "params":IconConverter.toRawTransaction(callTransactionData),
    //     "id":50889
    // })

    // var parsed = JSON.parse(score_sdk)
    // console.log("parsed: "+parsed);
    // window.dispatchEvent(new CustomEvent('ICONEX_RELAY_REQUEST', {
    //     detail: {
    //         type: 'REQUEST_JSON-RPC',
    //         payload: parsed,
    //     }
    // })); 

    // $('#loading').show();