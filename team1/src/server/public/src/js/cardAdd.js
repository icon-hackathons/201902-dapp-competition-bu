import IconService, { IconAmount, IconConverter, HttpProvider, IconWallet, IconBuilder, SignedTransaction } from 'icon-sdk-js';


// default 
const httpProvider = new HttpProvider('http://127.0.0.1:9000/api/v3');
const iconService = new IconService(httpProvider);

// builder
const CallBuilder = IconService.IconBuilder.CallBuilder;
const CallTransactionBuilder = IconService.IconBuilder.CallTransactionBuilder;
const IcxTransactionBuilder = IconService.IconBuilder.IcxTransactionBuilder;

// service 
const iconWallet = IconService.IconWallet;
const signedTransaction = IconService.SignedTransaction;


// document.getElementById("normalCard").onclick = transaction(1);
var nomalCard = document.getElementById("normalCard");
var rareCard = document.getElementById("rareCard");
var UniqueCard = document.getElementById("UniqueCard");

window.addEventListener("ICONEX_RELAY_RESPONSE", eventHandler, false);
// type and payload are in event.detail


// 커스텀 변수
var address = getParameterByAddress('address');
var score_to = 'cxdacd3169934b4da8ab0141c5f6c2b74ce320fd67';
var addr_to = "hxc22ae778606f626c03815a5adc41da4a1dad6b4f";
var grade = 0;


function eventHandler(event) {
    var type = event.detail.type;
    var payload = event.detail.payload;

    switch (type) {
        case "RESPONSE_HAS_ACCOUNT":
            console.log("> Result : " + payload.hasAccount + " (" + typeof payload.hasAccount + ")");
            break;
        case "RESPONSE_HAS_ADDRESS":
            console.log("2");
            break;
        case "RESPONSE_ADDRESS":
            console.log("> Selected ICX Address : " + payload);
            fromAddress = payload;
            break;
        case "RESPONSE_JSON-RPC":
            console.log("카드 1강: "+JSON.stringify(payload));
            // 카드 등급 정하기
            if(grade===0) {
                console.log("error grade is 0"+grade);
                alert("error")
            } else {
                console.log("grade is: "+grade);
                // purchaseCard(grade);
            }
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

// 노멀카드 구매시
nomalCard.onclick = function() {
    grade = String(1);

    var callTransactionBuilder = new IconBuilder.CallTransactionBuilder;
    var callTransactionData = callTransactionBuilder
        .from(address)
        .to(score_to)
        .nid(IconConverter.toBigNumber(3))
        .value(IconAmount.of(1, IconAmount.Unit.ICX).toLoop())
        .timestamp((new Date()).getTime() * 1000)
        .stepLimit(IconConverter.toBigNumber(10000000))
        .version(IconConverter.toBigNumber(3))
        .method('createCard')
        .params({
            "_grade": grade
        })
        .build();
    var score_sdk = JSON.stringify( {
        "jsonrpc":"2.0",
        "method":"icx_sendTransaction",
        "params":IconConverter.toRawTransaction(callTransactionData),
        "id":50889
    })

    var parsed = JSON.parse(score_sdk)

    window.dispatchEvent(new CustomEvent('ICONEX_RELAY_REQUEST', {
        detail: {
            type: 'REQUEST_JSON-RPC',
            payload: parsed,
        }
    })); 
}

// 레어카드 구매시
rareCard.onclick = function() {
    grade = String(2);

    var callTransactionBuilder = new IconBuilder.CallTransactionBuilder;
    var callTransactionData = callTransactionBuilder
        .from(address)
        .to(score_to)
        .nid(IconConverter.toBigNumber(3))
        .value(IconAmount.of(2, IconAmount.Unit.ICX).toLoop())
        .timestamp((new Date()).getTime() * 1000)
        .stepLimit(IconConverter.toBigNumber(10000000))
        .version(IconConverter.toBigNumber(3))
        .method('createCard')
        .params({
            "_grade": grade
        })
        .build();
    var score_sdk = JSON.stringify( {
        "jsonrpc":"2.0",
        "method":"icx_sendTransaction",
        "params":IconConverter.toRawTransaction(callTransactionData),
        "id":50889
    })

    var parsed = JSON.parse(score_sdk)

    window.dispatchEvent(new CustomEvent('ICONEX_RELAY_REQUEST', {
        detail: {
            type: 'REQUEST_JSON-RPC',
            payload: parsed,
        }
    })); 
}

// 유니크카드 구매시
UniqueCard.onclick = function() {
    grade = String(3);

    var callTransactionBuilder = new IconBuilder.CallTransactionBuilder;
    var callTransactionData = callTransactionBuilder
        .from(address)
        .to(score_to)
        .nid(IconConverter.toBigNumber(3))
        .value(IconAmount.of(3, IconAmount.Unit.ICX).toLoop())
        .timestamp((new Date()).getTime() * 1000)
        .stepLimit(IconConverter.toBigNumber(10000000))
        .version(IconConverter.toBigNumber(3))
        .method('createCard')
        .params({
            "_grade": grade
        })
        .build();
    var score_sdk = JSON.stringify( {
        "jsonrpc":"2.0",
        "method":"icx_sendTransaction",
        "params":IconConverter.toRawTransaction(callTransactionData),
        "id":50889
    })

    var parsed = JSON.parse(score_sdk)

    window.dispatchEvent(new CustomEvent('ICONEX_RELAY_REQUEST', {
        detail: {
            type: 'REQUEST_JSON-RPC',
            payload: parsed,
        }
    })); 
}


// get방식으로 넘어온 address 를 리턴함
function getParameterByAddress(address) {
    var address = address.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + address + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}



// 카드구매함수 자신의 주소로 카드구매함
// async function purchaseCard(_grade) {
//     var callTransaction = new CallTransactionBuilder()
//         .from(address)
//         .to(score_to)
//         // .value(10000000000000000000)
//         .nid(IconConverter.toBigNumber(3))
//         .stepLimit(IconConverter.toBigNumber(10000000))
//         .timestamp((new Date()).getTime() * 1000)
//         .version(IconConverter.toBigNumber(3))
//         .method('createCard')
//         .params({
//             "_grade":_grade
//         })
//         .build();        
        
//     const SignedTransaction = new signedTransaction(callTransaction, iconWallet.loadPrivateKey("5c2e41d402a9b5c8c468d5c309129cd48a07abf3be8c4d8ee9f9e71f29c4d040"));
//     const txHash = await iconService.sendTransaction(SignedTransaction).execute();
//     console.log(txHash)
// }



// var icxTransactionBuilder = new IconBuilder.IcxTransactionBuilder;
// var icxTransferData = icxTransactionBuilder
//     .from(address)
//     .to(addr_to)
//     .nid(IconConverter.toBigNumber(3))
//     .value(IconAmount.of(2, IconAmount.Unit.ICX).toLoop())
//     .timestamp((new Date()).getTime() * 1000)
//     .version(IconConverter.toBigNumber(3))
//     .stepLimit(IconConverter.toBigNumber(1000000))
//     .build();

// var score_sdk = JSON.stringify( {
//     "jsonrpc":"2.0",
//     "method":"icx_sendTransaction",
//     "params":IconConverter.toRawTransaction(icxTransferData),
//     "id":50889
// })

// var parsed = JSON.parse(score_sdk)

// window.dispatchEvent(new CustomEvent('ICONEX_RELAY_REQUEST', {
//     detail: {
//         type: 'REQUEST_JSON-RPC',
//         payload: parsed
//     }
// })); 


