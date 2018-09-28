function printRange(start,end,skip) {
    for(let i=start; i < end; i+=skip) {
        console.log(i);
    }
}

printRange(2,10,2);