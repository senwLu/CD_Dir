let nameArr = ["James", "Jill", "Jane", "Jack"];
let sym = "==>";

function fancyOut(arr,symb,reversed) {
    if(reversed) {
        for(let i = 0; i < arr.length; i++) {
            console.log(arr[i] + ' ' + symb + ' ' + i);
        }        
    }else {
        for(let i = 0; i < arr.length; i++) {
            console.log(i + ' ' + symb + ' ' + arr[i]);
        }       
    }
}

fancyOut(nameArr, sym);