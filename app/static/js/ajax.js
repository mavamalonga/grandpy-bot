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


function checkInputText(){

  question = document.getElementById("input").value;
  if (question === ""){
    text = 'False';
  }else{
    text = 'True';
  }
}


function makeRequest(event) {
    var xhttp = new XMLHttpRequest();

    checkInputText()
    console.log(text)

    if (text === 'True'){
        let endpoint = "http://127.0.0.1:5000/api"
        let url = endpoint.concat('/', question);
        xhttp.open("GET", url, true);
        xhttp.send();
        event.preventDefault();

        xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
           response = JSON.parse(this.responseText)
           console.log(response)
           if (response !== ""){

              if (response["sentences"] !== ""){
                document.getElementById("log").innerHTML = response['sentences']
              }

              if (response["geolocation"] !== ""){
                initMap()
              }
              
            }else{
              document.getElementById("log").innerHTML = "Désolé mec j'ai pas capté ta question";
            }
          }
        }
    }else if (text === 'False'){
      document.getElementById("log").innerHTML = "Désolé mec j'ai pas capté ta question";
    };

  };



const form = document.getElementById('form');
form.addEventListener('submit', makeRequest);
