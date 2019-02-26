const IconService = require('icon-sdk-js');

var HttpProvider = IconService.HttpProvider;
var IconWallet = IconService.IconWallet;
const IconConverter = IconService.IconConverter;
const IconAmount = IconService.IconAmount;

const CallBuilder = IconService.IconBuilder.CallBuilder;
const CallTransactionBuilder = IconService.IconBuilder.CallTransactionBuilder;
const IcxTransactionBuilder = IconService.IconBuilder.IcxTransactionBuilder;
const SignedTransaction = IconService.SignedTransaction

const httpProvider = new HttpProvider('http://127.0.0.1:9000/api/v3');
// const httpProvider = new HttpProvider('https://bicon.net.solidwallet.io/api/v3');
const iconService = new IconService(httpProvider);

// const wallet = IconWallet.create();
// console.log("Address: " + wallet.getAddress()); // Address Check
// console.log("PrivateKey: " + wallet.getPrivateKey()); // PrivateKey Check

test()

async function test() {
    
    wallet = IconWallet.loadPrivateKey("5c2e41d402a9b5c8c468d5c309129cd48a07abf3be8c4d8ee9f9e71f29c4d040");
    // console.log(wallet)

    // var callCreateCard = new CallTransactionBuilder()
    //     .from('hx08711b77e894c3509c78efbf9b62a85a4354c8df')
    //     .to('cx37d5799e548048ba19566e3d018e77a9392b1cc2')
    //     .stepLimit(IconConverter.toBigNumber('2000000'))
    //     .nid(IconConverter.toBigNumber('3'))
    //     .nonce(IconConverter.toBigNumber('1'))
    //     .version(IconConverter.toBigNumber('3'))
    //     .timestamp((new Date()).getTime() * 1000)
    //     .method('createCard')
    //     .params({
    //         "_grade": "3",
    //         "_player":"hx08711b77e894c3509c78efbf9b62a85a4354c8df"
    //     })
    //     .build()

    // const signedTransaction = new SignedTransaction(callCreateCard, wallet);

    // txHash = await iconService.sendTransaction(signedTransaction).execute();
    // console.log(txHash);

    // console.log(callCreateCard);
    // const respond = await iconService.sendTransaction(signedTransaction).excute();

    var call = new CallBuilder()
        .from('hx08711b77e894c3509c78efbf9b62a85a4354c8df')
        .to('cx37d5799e548048ba19566e3d018e77a9392b1cc2')
        .method('name')
        .build()

    var name = await iconService.call(call).execute(); 
    console.log("name: "+name)

    var call = new CallBuilder()
        .from('hx08711b77e894c3509c78efbf9b62a85a4354c8df')
        .to('cx37d5799e548048ba19566e3d018e77a9392b1cc2')
        .method('symbol')
        .build()

    var symbol = await iconService.call(call).execute(); 
    console.log("symbol: "+symbol)

    var call = new CallBuilder()
        .from('hx08711b77e894c3509c78efbf9b62a85a4354c8df')
        .to('cx37d5799e548048ba19566e3d018e77a9392b1cc2')
        .method('balanceOf')
        .params({ 
            "_owner":"hx08711b77e894c3509c78efbf9b62a85a4354c8df"
        })
        .build()

    var balanceOf = await iconService.call(call).execute(); 
    console.log("balanceOf: "+balanceOf)

    var call = new CallBuilder()
    .from('hx08711b77e894c3509c78efbf9b62a85a4354c8df')
    .to('cx37d5799e548048ba19566e3d018e77a9392b1cc2')
    .method('showAllCard')
    .build()

    var showAllCard = await iconService.call(call).execute(); 
    console.log("showAllCard: "+showAllCard)
    // var call = new CallBuilder()
    //     .from('hx08711b77e894c3509c78efbf9b62a85a4354c8df')
    //     .to('cx37d5799e548048ba19566e3d018e77a9392b1cc2')
    //     .method('getProperty')
    //     .params({ 
    //         "_tokenId":"1"
    //     })
    //     .build()

    // var getProperty = await iconService.call(call).execute(); 
    // console.log("getProperty: "+getProperty)
       



    // console.log("totalSupply: "+totalSupply)
    // console.log("balance: "+balance)
    // console.log("block2: "+block2)
    // console.log(block2)
    // console.log(apiList.getList());
    
    // var txObj = new IcxTransactionBuilder()
    //     .from('hx08711b77e894c3509c78efbf9b62a85a4354c8df')
    //     .to('hx79e7f88e6186e72d86a1b3f1c4e29bd4ae00ff53')
    //     .value(IconAmount.of(7, IconAmount.Unit.ICX).toLoop())
    //     .stepLimit(IconConverter.toBigNumber(100000))
    //     .nid(IconConverter.toBigNumber(3))
    //     .nonce(IconConverter.toBigNumber(1))
    //     .version(IconConverter.toBigNumber(3))
    //     .timestamp((new Date()).getTime() * 1000)
    //     .build()
    // console.log(txObj)

    // var response = await iconService.call(txObj).execute();
    // console.log(response)
}

