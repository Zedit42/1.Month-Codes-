var flipCoin = coin()
function coin(){
   return Math.ceil(Math.random() * 2)
}
if(flipCoin<1.5){
    console.log("tura")
}
else{
    console.log("yazı")
}