var sad = "Kaldın"
var good = "Geçtin"
function myExams(System){
    return Math.ceil(Math.random() * System)

}
var math = myExams(100)
console.log("Matematik " + math)
var chemestry = myExams(5)
console.log("Kimya " + chemestry)
if(math<50){
    console.log(sad)
}
else{
    console.log(good)
}