let testArr = [1, "apple", -3, "orange", 0.5];

function rtnNums(arr) {
    let tempArr = [];
    for(let i=0; i < arr.length; i++) {
        if(typeof arr[i] === "number") {
            tempArr.push(arr[i]);
        }
    }
    return tempArr;
}

console.log(rtnNums(testArr));