function playSlots(coins) {
    let coinCount = coins;

    while(coinCount !== 0) {
        if(coinCount === 0) {
            return 0;
        }else {
            coinCount--;
            let winLose = Math.floor(Math.random() * (100 - 0 + 1)) + 0;
            
            if(winLose === 100) {
                let winCoins = Math.floor(Math.random() * (100 - 50 + 1)) + 50;
                coinCount += winCoins;
            }
        }
        console.log(coinCount);
    }
}

playSlots(30);