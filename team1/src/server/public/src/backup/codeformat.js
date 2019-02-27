// ********************* call *********************
// var call = new CallBuilder()
    //     .from("hx08711b77e894c3509c78efbf9b62a85a4354c8df")
    //     .to('cx37d5799e548048ba19566e3d018e77a9392b1cc2')
    //     .method('createCard')
    //     .params({ 
    //         "_grade":_grade
    //     })
    //     .build()

    // let card = await iconService.call(call).execute(); 
    // console.log("card: "+card);

// ********************* calltransaction *********************
// var callTransaction = new CallTransactionBuilder()
//     .from(address)
//     .to('cx37d5799e548048ba19566e3d018e77a9392b1cc2')
//     .nid(IconConverter.toBigNumber(3))
//     .stepLimit(IconConverter.toBigNumber(10000000))
//     .timestamp((new Date()).getTime() * 1000)
//     .version(IconConverter.toBigNumber(3))
//     .method('createCard')
//     .params({
//         "_grade":_grade
//     })
//     .build();        
// const SignedTransaction = new signedTransaction(callTransaction, iconWallet.loadPrivateKey("5c2e41d402a9b5c8c468d5c309129cd48a07abf3be8c4d8ee9f9e71f29c4d040"));
// const txHash = await iconService.sendTransaction(SignedTransaction).execute();
// console.log(txHash)

// 확인 해봐야함
// ********************* IcxTransactionBuilder *********************
// const txObj = new IcxTransactionBuilder()
//         .from('hx08711b77e894c3509c78efbf9b62a85a4354c8df')
//         .to('cx37d5799e548048ba19566e3d018e77a9392b1cc2')
//         .value(IconAmount.of(cardPrice, IconAmount.Unit.ICX).toLoop())
//         .stepLimit(IconConverter.toBigNumber(10000000))
//         .nid(IconConverter.toBigNumber(3))
//         .nonce(IconConverter.toBigNumber(1))
//         .version(IconConverter.toBigNumber(3))
//         .timestamp((new Date()).getTime() * 1000)
//         .build()
//     // Returns raw transaction object
//     // const rawTxObj = IconConverter.toRawTransaction(txObj)
//     const SignedTransaction = new signedTransaction(txObj, iconWallet.loadPrivateKey("5c2e41d402a9b5c8c468d5c309129cd48a07abf3be8c4d8ee9f9e71f29c4d040"));
//     const txHash = await iconService.sendTransaction(SignedTransaction).execute();
//     console.log(txHash)


// ====================================================================================================================================================
// async function transaction(cardPrice) {
//     console.log("cardPrice: "+cardPrice);
//     const txObj = new IcxTransactionBuilder()
//         .from('hx08711b77e894c3509c78efbf9b62a85a4354c8df')
//         .to('cx37d5799e548048ba19566e3d018e77a9392b1cc2')
//         .value(IconAmount.of(cardPrice, IconAmount.Unit.ICX).toLoop())
//         .stepLimit(IconConverter.toBigNumber(10000000))
//         .nid(IconConverter.toBigNumber(3))
//         .nonce(IconConverter.toBigNumber(1))
//         .version(IconConverter.toBigNumber(3))
//         .timestamp((new Date()).getTime() * 1000)
//         .build()
//     // Returns raw transaction object
//     // const rawTxObj = IconConverter.toRawTransaction(txObj)
//     const SignedTransaction = new signedTransaction(txObj, iconWallet.loadPrivateKey("5c2e41d402a9b5c8c468d5c309129cd48a07abf3be8c4d8ee9f9e71f29c4d040"));
//     const txHash = await iconService.sendTransaction(SignedTransaction).execute();
//     console.log(txHash)
// }

// mycard source
// var callTransactionBuilder = new IconBuilder.CallTransactionBuilder;
// var callTransactionData = callTransactionBuilder
//     .from("hx08711b77e894c3509c78efbf9b62a85a4354c8df")
//     .to("cx37d5799e548048ba19566e3d018e77a9392b1cc2")
//     .nid(IconConverter.toBigNumber(3))
//     .timestamp((new Date()).getTime() * 1000)
//     .stepLimit(IconConverter.toBigNumber(1000000))
//     .version(IconConverter.toBigNumber(3))
//     .method('createCard')
//     .params({
//         "_grade":_grade
//     })
//     .build();

// var score_sdk = JSON.stringify( {
//         "jsonrpc":"2.0",
//         "method":"icx_sendTransaction",
//         "params":IconConverter.toRawTransaction(callTransactionData),
//         "id":50889
//     })

// var parsed = JSON.parse(score_sdk)
// window.dispatchEvent(new CustomEvent('ICONEX_RELAY_REQUEST', {
//     detail: {
//         type: 'REQUEST_JSON-RPC',
//         payload: parsed,
//     }
// })); 