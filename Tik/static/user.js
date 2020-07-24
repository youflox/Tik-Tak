const sound = new Audio('static/click.mp3')
const player = 'X'

const user = document.getElementById('username').innerText;
let opponent;

if (user == 'Nanda'){
    opponent = 'Ratna'}
else{
    opponent = 'Nanda'};

console.log('user -',user)
console.log('opponent -',opponent)



function btn(val){
    sound.play()

    document.getElementById(`btn${val}`).innerText = 'O'

    data = {'button' : `btn${val}`}
    console.log(data)


    fetch(`${window.origin}/${user}/post`,{
        method : 'POST',
        cache : 'no-cache',
        body : JSON.stringify(data),
        headers : new Headers({'content-type' : 'application/json',
                            'Access-Control-Allow-Origin': "*",
                            'Access-Control-Allow-Headers' : "*"
        })
    })
}

var rec = setInterval(recu, 7000)

function recu(){
    console.log('op', opponent)
    fetch(`${window.origin}/${opponent}/get`)
    .then(response => response.json())
    .then( data => {
            console.log(data['data']);
            document.getElementById(data["data"]['button']).innerText = player

    })
}


