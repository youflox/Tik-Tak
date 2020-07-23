const sound = new Audio('static/click.mp3')
const player = 'O'

function btn(val){
    sound.play()
    document.getElementById(`btn${val}`).innerText = 'X'

    data = {'button' : `btn${val}`}

    fetch(`${window.origin}/getter`,{
        method : 'POST',
        cache : 'no-cache',
        body : JSON.stringify(data),
        headers : new Headers({'content-type' : 'application/json',
                            'Access-Control-Allow-Origin': "*",
                            'Access-Control-Allow-Headers' : "*"
        })
    })
}

var rec = setInterval(recu, 2000)

function recu(){
    fetch(`${window.origin}/post`)
    .then(response => response.json())
    .then( data => {
    console.log(data['data'])
            document.getElementById(data["data"]['button']).innerText = player

    })
}