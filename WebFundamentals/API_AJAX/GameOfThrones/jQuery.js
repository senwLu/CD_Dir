$(document).ready(function() {
    $('img').on('click', function() {
        // if there is previous data, remove
        $('legend').siblings().remove();

        const houseName = $(this).attr('value');
        const houseCall = `https://www.anapioficeandfire.com/api/houses/?name=${houseName}`;
        $.get(houseCall, function(res) {
            console.log(res);
            const name = res[0].name;
            const words = res[0].words;
            const titles = res[0].titles;
            let addTitles = '';

            $('#houseInfo').append(`<p>Name: ${name}</p>`);
            $('#houseInfo').append(`<p>Name: ${words}</p>`);
            $('#houseInfo').append(`<br><br>`);
            for(let i=0; i < titles.length; i++) {
                if(i === 0 ) {
                    addTitles += titles[0];
                }else {
                    addTitles += ', '+titles[i];
                }
            }
            $('#houseInfo').append(`<p>Name: ${addTitles}</p>`);
        })        
    })

});