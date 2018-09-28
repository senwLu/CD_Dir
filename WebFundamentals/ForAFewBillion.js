let start = 0.01;
let days = 20;

// for(let i = 0; i < days; i++) {
//     start += start;
// }

// console.log(start);

let countDays = 0;

while(start < 10000) {
    start+=start;
    countDays++;
}
console.log(countDays);