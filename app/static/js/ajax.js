

var messageBubble = function(user, message){

  if (user=='guest') {
    let chatBox = document.getElementsByClassName('chat-box');
    
    // create balises

    let chatRight = document.createElement('div').appendChild( document.createElement('p') );
    let  attChatRight= document.createAttribute('class');
    attChatRight.value = 'chat-r';
    chatRight.setAttributeNode(attChatRight)

    let msgRight = document.createElement('div');
    let attMsgRight = document.createAttribute('class');
    attMsgRight.value = 'mess mess-r';
    msgRight.setAttributeNode(attMsgRight); 
    

    let check = document.createElement('div');
    let paragraph = document.createElement('p');
    let span = document.createElement('span');
    let img = document.createElement('img');

    //create attributes
  

    bulle.setAttributeNode(att);
    bulle.innerHTML = `${message}`;
    divChat.insertBefore(bulle, divChat.children[-1]);

  }else if(user=='grandpy'){
    var divChat = document.getElementById('chat');
    var bulle = document.createElement('div').appendChild( document.createElement('p') );
    var att = document.createAttribute('class');
    att.value = 'bulle-grandpy';
    bulle.setAttributeNode(att);
    bulle.innerHTML = `${message}`;
    divChat.insertBefore(bulle, divChat.children[-1]);

  }
}


function makeRequest(event) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      response = JSON.parse(this.responseText)
      console.log(response['text'])
      //messageHistory('grandpy', response['text'])

    }
  };
  var message = document.getElementById('text-msg').value;
  console.log(message);
  let endpoint = "http://127.0.0.1:5000/api"
  let url = endpoint.concat('/', message);

  //messageHistory('guest', message);

  xhttp.open("GET", url, true);
  xhttp.send();
  event.preventDefault();

};

const send = document.getElementsByClassName('send')[0];
send.addEventListener('click', makeRequest);
