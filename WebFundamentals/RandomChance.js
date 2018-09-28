function playSlots(coins) {
    let coinCount = coins;

    while(coinCount > 0) {
        let winLose = Math.floor(Math.random()*100+1);

        if(winLose === 100) {
            let coinsWon = Math.floor(Math.random()*(100-50+1))+50;
            coinCount+=coinsWon;
        }else {
            coinCount--;
        }
        console.log(coinCount);
    }
    return 0;
}

function playUntil(coins,stop) {
    let coinCount = coins;

    while(coinCount > 0) {
        if(coinCount >= stop) {
            return coinCount;
        }else {
            let winLose = Math.floor(Math.random()*100+1);

            if(winLose === 100) {
                let coinsWon = Math.floor(Math.random()*(100-50+1))+50;
                coinCount+=coinsWon;
            }else {
                coinCount--;
            }
        }
        console.log(coinCount);
    }
    return 0;    
}


playUntil(10,100);