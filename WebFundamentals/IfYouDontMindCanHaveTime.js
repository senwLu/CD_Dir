let HOUR = 8;
let MINUTE = 10;
let PERIOD = "AM";

// const clockPRD = PERIOD==="AM" ? "morning" : "evening";

// if(MINUTE>50) {
//     console.log(`It's almost ${HOUR} in the ${clockPRD}`);
// }
// else {
//     console.log(`It's just after ${HOUR} in the ${clockPRD}`);
// }

// const minClock = MINUTE>30 ? "almost the next hour" : "just after the hour";
// console.log(`It's ${HOUR} in the ${clockPRD}, ${minClock}`);

if(MINUTE==5) {
    MINUTE = "5 after";
}else if(MINUTE==25) {
    MINUTE = "quarter after";
}else if(MINUTE==30) {
    MINUTE = "half past";
}

if(HOUR==24) {
    PERIOD = "midnight";
    HOUR-=12;
}else if(HOUR==12) {
    PERIOD = "noon"
}else if(HOUR < 24 && HOUR > 12) {
    PERIOD = "in the afternoon";
    HOUR-=12;
}else {
    PERIOD = "in the morning";
}

if(typeof MINUTE == "string"){
    console.log(`It's ${MINUTE} ${HOUR} ${PERIOD}`);
}else {
    console.log(`It's ${HOUR} ${MINUTE} ${PERIOD}`);
}