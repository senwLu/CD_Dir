let students = [ 
    {first_name:  'Michael', last_name : 'Jordan'},
    {first_name : 'John', last_name : 'Rosales'},
    {first_name : 'Mark', last_name : 'Guillen'},
    {first_name : 'KB', last_name : 'Tonel'}
]

function combineFL(arrObj) {
    for(let i=0; i < arrObj.length; i++) {
        let name = "";
        for(a in arrObj[i]) {
           name+= arrObj[i][a] + " ";
        }
        console.log(name);
        name = "";
    }
}

// combineFL(students);

let users = {
    'Students': [ 
        {first_name:  'Michael', last_name : 'Jordan'},
        {first_name : 'John', last_name : 'Rosales'},
        {first_name : 'Mark', last_name : 'Guillen'},
        {first_name : 'KB', last_name : 'Tonel'}
     ],
    'Instructors': [
        {first_name : 'Michael', last_name : 'Choi'},
        {first_name : 'Martin', last_name : 'Puryear'}
     ]
    }

function combineFL2(arrObj) {
    // loop through the keys of users object
    for(i in arrObj){
        console.log(i);
        let lineCount;

        // loop through the array 
        for(let a=0; a < arrObj[i].length; a++) {
            let nameNums = 0;
            let name = "";
            lineCount = a+1;

            // loop through each key in object
            // combine each vaule of key to name variable
            // count length of value and add to nameNums variable
            for(b in arrObj[i][a]) {
                name += arrObj[i][a][b] + " ";
                nameNums += (arrObj[i][a][b]).length;
            }

            console.log(lineCount + " - " + name + " - " + nameNums);
            name = "";
            nameNums = 0;
        }
    }
}

combineFL2(users);