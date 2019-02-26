// import IconService from 'icon-sdk-js';
// import 'babel-polyfill';
import IconService, {IconAmount,IconConverter,HttpProvider,IconWallet,IconBuilder,SignedTransaction} from 'icon-sdk-js';

// httpProvider = new HttpProvider();
const httpProvider = new HttpProvider('http://127.0.0.1:9000/api/v3');
const iconService = new IconService(httpProvider);


const CallBuilder = IconService.IconBuilder.CallBuilder;
const iconConverter = IconService.IconConverter;
const signedTransaction = IconService.SignedTransaction;
const iconWallet = IconService.IconWallet;
const callTransactionBuilder = IconService.IconBuilder.CallTransactionBuilder;



function getParameterByName(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}

var address = getParameterByName('address');
console.log('address : '+address);

// cx29c4e8d9affdb1f7bc9143083c8cbf2c51eb7c2d



test()
async function test() {

    // wallet = iconWallet.loadPrivateKey("5c2e41d402a9b5c8c468d5c309129cd48a07abf3be8c4d8ee9f9e71f29c4d040");

    var CreateCard = new callTransactionBuilder()
        .from(address)
        .to('cx29c4e8d9affdb1f7bc9143083c8cbf2c51eb7c2d')
        .stepLimit(iconConverter.toBigNumber('2000000'))
        .nid(iconConverter.toBigNumber('3'))
        .nonce(iconConverter.toBigNumber('1'))
        .version(iconConverter.toBigNumber('3'))
        .timestamp((new Date()).getTime() * 1000)
        .method('createCard')
        .params({
            "_grade": "3",
            "_player":"jordan"
        })
        .build()

    const SignedTransaction = new signedTransaction(CreateCard, iconWallet.loadPrivateKey("5c2e41d402a9b5c8c468d5c309129cd48a07abf3be8c4d8ee9f9e71f29c4d040"));
    const txHash = await iconService.sendTransaction(SignedTransaction).execute();
    console.log(txHash)
    
}
