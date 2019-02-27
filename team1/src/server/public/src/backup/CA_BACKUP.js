import IconService, { IconAmount, IconConverter, HttpProvider, IconWallet, IconBuilder, SignedTransaction } from 'icon-sdk-js';
// // cx37d5799e548048ba19566e3d018e77a9392b1cc2
// // cx6ad3a41000e745a811132501dbc9cc96c67ac6dc

// default 
const httpProvider = new HttpProvider('http://127.0.0.1:9000/api/v3');
const iconService = new IconService(httpProvider);

// builder
const CallBuilder = IconService.IconBuilder.CallBuilder;
const IcxTransactionBuilder = IconService.IconBuilder.IcxTransactionBuilder;

// service 
const iconWallet = IconService.IconWallet;
const signedTransaction = IconService.SignedTransaction;

// myCard()
// const iconAmount = IconAmount.of('2', IconAmount.Unit.ICX);
// console.log("iconAmount: "+iconAmount);
// const value = IconAmount.of('2', IconAmount.Unit.ICX).toString();
// console.log("value: "+value);
// const value2 = IconAmount.of('2', IconAmount.Unit.ICX).toLoop();
// console.log("value2: "+value2);
// const value3 = IconAmount.of('2', IconAmount.Unit.ICX).convertUnit(IconAmount.Unit.LOOP);
// console.log("value3: "+value3);

// document.getElementById("normalCard").onclick = transaction(1);
var nomalCard = document.getElementById("normalCard");
var rareCard = document.getElementById("rareCard");
var UniqueCard = document.getElementById("UniqueCard");


nomalCard.onclick = function() {
    // transaction(1);
    myCard("1")
}
rareCard.onclick = function() {
    // transaction(2);
    myCard("2")
}
UniqueCard.onclick = function() {
    // transaction(3);
    myCard("3")
}


async function transaction(cardPrice) {
    console.log("cardPrice: "+cardPrice);
    const txObj = new IcxTransactionBuilder()
        .from('hx08711b77e894c3509c78efbf9b62a85a4354c8df')
        .to('cx37d5799e548048ba19566e3d018e77a9392b1cc2')
        .value(IconAmount.of(cardPrice, IconAmount.Unit.ICX).toLoop())
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

async function myCard(_grade) {
    var call = new CallBuilder()
        .from("hx08711b77e894c3509c78efbf9b62a85a4354c8df")
        .to('cx37d5799e548048ba19566e3d018e77a9392b1cc2')
        .method('createCard')
        .params({ 
            "_grade":_grade
        })
        .build()

    let card = await iconService.call(call).execute(); 
    console.log("card: "+card);
    // return balanceOf;
}