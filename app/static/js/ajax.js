var updateScrollbar = function() {
  var elem = document.getElementsByClassName('chat_box');
  elem.scrollTop = elem.scrollHeight;
  console.log(elem.scrollHeight);
};



var messageBubble = function(user, message){

  if (user=='grandpy') {
    let chat_box = document.getElementsByClassName('chat-box')[0];
    
    // create balises

    let div_chat_r = document.createElement('div')
    let  att_chat_r = document.createAttribute('class');
    att_chat_r.value = "chat-r";
    div_chat_r.setAttributeNode(att_chat_r);

    let div_mess_r = document.createElement('div');
    let att_mess_r = document.createAttribute('class');
    att_mess_r.value = "mess mess-r";
    div_mess_r.setAttributeNode(att_mess_r);
    let paragraph = document.createElement('p');
    paragraph.innerHTML = `${message['text']}`;
    div_mess_r.appendChild(paragraph);

    let div_check = document.createElement('div');
    let att_check = document.createAttribute('class');
    att_check.value = "check";
    div_check.setAttributeNode(att_check);
    let span = document.createElement('span');
    span.innerHTML = `${message['datetime']}`;
    div_check.appendChild(span);
    let img = document.createElement('img');
    let att_img = document.createAttribute('src');
    att_img.value = "http://127.0.0.1:5000/static/img/grandpy.jpg";
    img.setAttributeNode(att_img);
    div_check.appendChild(img);

    div_mess_r.appendChild(div_check)
    div_chat_r.appendChild(div_mess_r);

    chat_box.insertBefore(div_chat_r, chat_box.children[-1]);
    updateScrollbar();


  }else if(user=='guest'){
    let chat_box = document.getElementsByClassName('chat-box')[0];
    
    // create balises

    let div_chat_l = document.createElement('div')
    let  att_chat_l = document.createAttribute('class');
    att_chat_l.value = 'chat-l';
    div_chat_l.setAttributeNode(att_chat_l);

    let div_mess = document.createElement('div');
    let att_mess = document.createAttribute('class');
    att_mess.value = 'mess';
    div_mess.setAttributeNode(att_mess);
    let paragraph = document.createElement('p');
    paragraph.innerHTML = `${message['message']}`;
    div_mess.appendChild(paragraph);

    let div_check = document.createElement('div');
    let att_check = document.createAttribute('class');
    att_check.value = 'check';
    div_check.setAttributeNode(att_check);
    let span = document.createElement('span');
    span.innerHTML = `${message['datetime']}`;
    div_check.appendChild(span);
    let img = document.createElement('img');
    let att_img = document.createAttribute('src');
    att_img.value = "http://127.0.0.1:5000/static/img/grandpy.jpg";
    img.setAttributeNode(att_img);
    div_check.appendChild(img);

    div_mess.appendChild(div_check);
    div_chat_l.appendChild(div_mess);

    chat_box.insertBefore(div_chat_l, chat_box.children[-1]);
    updateScrollbar();
  }
}


function makeRequest(event) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      response = JSON.parse(this.responseText)
      console.log(response['text'])
      messageBubble('grandpy', response)

    }
  };
  var message = document.getElementById('text-msg').value;
  console.log(message);
  let endpoint = "http://127.0.0.1:5000/api"
  let url = endpoint.concat('/', message);

  var currentdate = new Date();
  var datetime = currentdate.getHours() + ":" + currentdate.getMinutes();
  
  var guestMessage = { 'message' : message,
                   'datetime' : datetime
                 }
  messageBubble('guest', guestMessage);

  xhttp.open("GET", url, true);
  xhttp.send();
  event.preventDefault();

};


const send = document.getElementsByClassName('send')[0];
send.addEventListener('click', makeRequest);



let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -34.397, lng: 150.644 },
    zoom: 8,
  });
}