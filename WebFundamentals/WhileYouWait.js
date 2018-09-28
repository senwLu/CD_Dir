let daysUntilMyBirthday = 60;

while(daysUntilMyBirthday !== 0) {
    daysUntilMyBirthday--;
    if(daysUntilMyBirthday === 0) {
        console.log("IT's My BIRTHDAY!!!")
    } else if(daysUntilMyBirthday <= 30) {
        console.log(daysUntilMyBirthday + " Days UNTIL MY BIRTHDAY!!!");
    }else {
        console.log(daysUntilMyBirthday + " days until my birthday. Such a long time... :(");
    }
}