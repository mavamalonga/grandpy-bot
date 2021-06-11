

var messageHistory = function(message){
  var divChat = document.getElementById('chat');

  var bulle = document.createElement('div').appendChild( document.createElement('p') );

  var att = document.createAttribute('class');
  att.value = 'bulle-guest';
  bulle.setAttributeNode(att);

  bulle.innerHTML = `${message}`;

  divChat.insertBefore(bulle, divChat.children[-1]);
}


function makeRequest(event) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      response = JSON.parse(this.responseText)
      document.querySelector('.bulle-grandpy p').innerHTML = response['text']

      var grandpy = document.querySelector('.bulle-grandpy');
      var divChat = document.getElementById('chat');
      divChat.insertBefore(grandpy, divChat.children[-1]);

    }
  };
  var message = document.getElementById("input").value;
  let endpoint = "http://127.0.0.1:5000/api"
  let url = endpoint.concat('/', message);

  messageHistory(message);

  xhttp.open("GET", url, true);
  xhttp.send();
  event.preventDefault();


  const myElement = document.getElementById('chat');
  console.log('childen elements : ' + myElement.children.length);
};



const form = document.getElementById('form');
form.addEventListener('submit', makeRequest);