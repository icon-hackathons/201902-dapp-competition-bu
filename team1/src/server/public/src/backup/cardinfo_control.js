var playerInfo = "run:306 dribble:390 power:355 Griffin"

var splitInfo = playerInfo.split(" ");

console.log("splitInfo: "+splitInfo);
console.log("splitInfo: "+typeof(splitInfo));

for(var i=0; i<splitInfo.length; i++) {
    console.log(" "+splitInfo[i]);
}

var run = splitInfo[0].split(":");
var dribble = splitInfo[1].split(":");
var power = splitInfo[2].split(":");

console.log("run: "+run[1]);
console.log("dribble: "+dribble[1]);
console.log("power: "+power[1]);
console.log("splitInfo[3]: "+splitInfo[3]);



