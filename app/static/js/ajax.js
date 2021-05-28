
let response;
var boolean = false;

function makeRequest(event) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var response = JSON.parse(this.responseText)
      document.getElementById("log").innerHTML = response['sentences']
      boolean = true
    }
  };
  var message = document.getElementById("input").value;
  let endpoint = "http://127.0.0.1:5000/api"
  let url = endpoint.concat('/', message);
  xhttp.open("GET", url, true);
  xhttp.send();
  event.preventDefault();
};


let map;
function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -34.397, lng: 150.644 },
    zoom: 8,
  });
}



const form = document.getElementById('form');
form.addEventListener('submit', makeRequest);

