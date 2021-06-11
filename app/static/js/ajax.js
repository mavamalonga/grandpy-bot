

var messageHistory = function(message){
  var divChat = document.getElementById('chat');

  var bulle = document.createElement('div').appendChild( document.createElement('p') );
  bulle.innerHTML = `${message}`;
  divChat.appendChild(bulle);
}


function makeRequest(event) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      response = JSON.parse(this.responseText)
      document.querySelector('.bulle-grandpy p').innerHTML = response['text']
    }
  };
  var message = document.getElementById("input").value;
  let endpoint = "http://127.0.0.1:5000/api"
  let url = endpoint.concat('/', message);

  messageHistory(message);

  xhttp.open("GET", url, true);
  xhttp.send();
  event.preventDefault();
};


const form = document.getElementById('form');
form.addEventListener('submit', makeRequest);