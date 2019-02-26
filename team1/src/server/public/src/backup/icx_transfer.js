import IconService, { IconAmount, IconConverter, HttpProvider, IconWallet, IconBuilder, SignedTransaction } from 'icon-sdk-js';

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


transaction();


// get방식으로 넘어온 address 를 리턴함
function getParameterByAddress(address) {
    var address = address.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + address + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}


async function transaction() {
    // console.log("cardPrice: "+);
    const txObj = new IcxTransactionBuilder()
        .from('hx08711b77e894c3509c78efbf9b62a85a4354c8df')
        .to('cxdacd3169934b4da8ab0141c5f6c2b74ce320fd67')
        .value(IconAmount.of(1, IconAmount.Unit.ICX).toLoop())
        .stepLimit(IconConverter.toBigNumber(10000000))
        .nid(IconConverter.toBigNumber(3))
        .nonce(IconConverter.toBigNumber(1))
        .version(IconConverter.toBigNumber(3))
        .timestamp((new Date()).getTime() * 1000)
        .build()
    // Returns raw transaction object
    // const rawTxObj = IconConverter.toRawTransaction(txObj)
    const SignedTransaction = new signedTransaction(txObj, iconWallet.loadPrivateKey("5c2e41d402a9b5c8c468d5c309129cd48a07abf3be8c4d8ee9f9e71f29c4d040"));
    const txHash = await iconService.sendTransaction(SignedTransaction).execute();
    console.log(txHash)
}