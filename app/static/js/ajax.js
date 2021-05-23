function logSubmit(event) {
  log.textContent = `Form Submitted! Time stamp: ${event.timeStamp}`;
  event.preventDefault();
}


function makeRequest(event) {

  var xhttp = new XMLHttpRequest();

  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     document.getElementById("log").innerHTML = this.responseText;
    }
  };

  var message = document.getElementById("input").value;
  console.log(message);

  xhttp.open("GET", "http://127.0.0.1:5000/api/makeRequest", true);
  xhttp.send();
  event.preventDefault();
  console.log(this.responseText)
}
  


const form = document.getElementById('form');
const log = document.getElementById('log');
form.addEventListener('submit', makeRequest);