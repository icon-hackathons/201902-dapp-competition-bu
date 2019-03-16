var iconService = window['icon-sdk-js'];
var IconAmount = iconService.IconAmount;
var IconConverter = iconService.IconConverter;
var IconBuilder = iconService.IconBuilder;

var responseHasAddress = document.getElementById("response-has-address");
var requestAddress = document.getElementById("request-address");
var responseAddress = document.getElementById("response-address");
var requestScore = document.getElementById("request-score");
var requestScoreForm = document.getElementById("request-score-form");
var responseScore = document.getElementById("response-score");
var jsonRpc0 = document.getElementById("json-rpc-0");
var jsonRpc1 = document.getElementById("json-rpc-1");
var jsonRpc2 = document.getElementById("json-rpc-2");
var jsonRpc3 = document.getElementById("json-rpc-3");
var scoreData = document.getElementById("score-data");
var signingData = document.getElementById("signing-data");
var requestSigning = document.getElementById("request-signing");
var responseSigning = document.getElementById("response-signing");

window.addEventListener("ICONEX_RELAY_RESPONSE", eventHandler, false);
// type and payload are in event.detail
function eventHandler(event) {
    var type = event.detail.type;
    var payload = event.detail.payload;
    switch (type) {

        case "RESPONSE_ADDRESS":
            fromAddress = payload;
            responseAddress.innerHTML = "> Selected ICX Address : " + payload;
            jsonRpc0.disabled = false;
            jsonRpc1.disabled = false;
            jsonRpc2.disabled = false;
            jsonRpc3.disabled = false;
            break;

        case "RESPONSE_JSON-RPC":
            responseScore.value = JSON.stringify(payload);
            break;
        case "CANCEL_JSON-RPC":
            responseScore.value = null;
            break;
        case "RESPONSE_SIGNING":
            signingData.value = null;
            responseSigning.innerHTML = "> Signature : " + JSON.stringify(payload);
            break;
        case "CANCEL_SIGNING":
            signingData.value = null;
            responseSigning.value = "> Signature : ";
            break;
        default:
    }
}

function setRequestScoreForm() {
    var data = new FormData(requestScoreForm);
    var type = '';
    for (const entry of data) {
        type = entry[1]
    }
    switch (type) {
        case 'read-only':
            var callBuilder = new IconBuilder.CallBuilder;
            var readOnlyData = callBuilder
                .from(fromAddress)
                .to('cx915746079d5878a54e267b6e2378e8aa79f26953')
                .method("name")
                .build();
            scoreData.value = JSON.stringify({
                "jsonrpc": "2.0",
                "method": "icx_call",
                "params": readOnlyData,
                "id": 50889
            });

            console.log("readOnlyData: ", readOnlyData)
            break;
        case 'send-transaction':
            var callTransactionBuilder = new IconBuilder.CallTransactionBuilder;
            var callTransactionData = callTransactionBuilder
                .from(fromAddress)
                .to("cx915746079d5878a54e267b6e2378e8aa79f26953")
                .nid(IconConverter.toBigNumber(3))
                .timestamp((new Date()).getTime() * 1000)
                .stepLimit(IconConverter.toBigNumber(1000000))
                .version(IconConverter.toBigNumber(3))
                .method('name')
                .params({
                    "price": IconConverter.toHex(10000),
                    "tokenType": IconConverter.toHex(2)
                })
                .build();
            scoreData.value = JSON.stringify({
                "jsonrpc": "2.0",
                "method": "icx_sendTransaction",
                "params": IconConverter.toRawTransaction(callTransactionData),
                "id": 50889
            });

            console.log(callTransactionData)
            break;
        case 'icx-transfer':
            var icxTransactionBuilder = new IconBuilder.IcxTransactionBuilder;
            var icxTransferData = icxTransactionBuilder
                .from("hx79e7f88e6186e72d86a1b3f1c4e29bd4ae00ff53")
                .to("hx04d669879227bb24fc32312c408b0d5503362ef0")
                .nid(IconConverter.toBigNumber(3))
                .value(IconAmount.of(1, IconAmount.Unit.ICX).toLoop())
                .timestamp((new Date()).getTime() * 1000)
                .version(IconConverter.toBigNumber(3))
                .stepLimit(IconConverter.toBigNumber(100000))
                .build();

            scoreData.value = JSON.stringify({
                "jsonrpc": "2.0",
                "method": "icx_sendTransaction",
                "params": IconConverter.toRawTransaction(icxTransferData),
                "id": 50889
            });
            break;
        default:
    }
}
requestAddress.onclick = function () {
    window.dispatchEvent(new CustomEvent('ICONEX_RELAY_REQUEST', {
        detail: {
            type: 'REQUEST_ADDRESS'
        }
    }))
};
requestScore.onclick = function () {
    responseScore.value = null;
    if (!scoreData.value) {
        alert('Check the param data');
        return
    }
    var parsed = JSON.parse(scoreData.value);
    if (parsed.method === "icx_sendTransaction" && !fromAddress) {
        alert('Select the ICX Address');
        return
    }
    window.dispatchEvent(new CustomEvent('ICONEX_RELAY_REQUEST', {
        detail: {
            type: 'REQUEST_JSON-RPC',
            payload: parsed
        }
    }))
};
requestSigning.onclick = function () {
    if (!fromAddress) {
        alert('Select an ICX wallet');
        return
    }
    window.dispatchEvent(new CustomEvent('ICONEX_RELAY_REQUEST', {
        detail: {
            type: 'REQUEST_SIGNING',
            payload: {
                from: fromAddress,
                hash: signingData.value || signingData.placeholder,
            }
        }
    }))
}