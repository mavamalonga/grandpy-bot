var response = {
  'geolocation': {
    'lat': -34.397,
    'lng': 150.644
  }
};


let map;
function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: parseInt(response['geolocation']['lat']), lng: parseInt(response['geolocation']['lng']) },
    zoom: 8,
  });
}


function checkInputContains(){
  var value, text;
  value = document.getElementById("input").value;
  if (value === ""){
    text = "input not valid";
  }else{
    text = "input Ok";
  }
  document.getElementById('log').innerHTML = text;
  return false;
}



function makeRequest(event) {


  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      response = JSON.parse(this.responseText)
      document.getElementById("log").innerHTML = response['sentences']

      initMap()
    }
  };
  var message = document.getElementById("input").value;
  let endpoint = "http://127.0.0.1:5000/api"
  let url = endpoint.concat('/', message);
  xhttp.open("GET", url, true);
  xhttp.send();
  event.preventDefault();
};


const form = document.getElementById('form');
form.addEventListener('submit', makeRequest);
