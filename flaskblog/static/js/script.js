console.log("it works");

let autocomplete;

function initAutocomplete() {
  console.log("autocomplete");
  autocomplete = new google.maps.places.Autocomplete(
    document.getElementById("autocomplete"),
    { types: ["geocode"] }
  );

  map = new google.maps.Map(document.getElementById("map"), {
    zoom: 14,
    center: { lat: 52.520008, lng: 13.404954 },
    streetViewControl: false,
    mapTypeControl: false,
    scaleControl: false,
    rotateControl: false,
    fullscreenControl: false,
  });

  autocomplete.addListener("place_changed", onPlaceChanged);
  let mylat = parseFloat(document.getElementById("lat").value);
  let mylng = parseFloat(document.getElementById("lng").value);

  map.setCenter({ lat: mylat, lng: mylng });
  var marker = new google.maps.Marker({
    map: map,
    position: { lat: mylat, lng: mylng },
  });
  marker.addListener("mouseover", () => {
    infowindow.open({
      anchor: marker,
      map,
      shouldFocus: false,
    });
  });
  marker.addListener("mouseout", () => {
    infowindow.close({
      anchor: marker,
      map,
      shouldFocus: false,
    });
  });

  /*const geocoder = new google.maps.Geocoder();
  document.getElementById("submit").addEventListener("click", () => {
    geocodeAddress(geocoder, map);
  });
*/
  const contentString =
    '<div id="content">' +
    '<div id="siteNotice">' +
    "</div>" +
    '<h2 id="firstHeading" class="firstHeading"> {{ form.name.label}}</h2>' +
    '<div id="bodyContent">' +
    "<p>{{ form.languages.label }} <br> {{ form.specialization.label}}</p>";
  "</div>" + "</div>";
  const infowindow = new google.maps.InfoWindow({
    content: contentString,
  });
}

function onPlaceChanged() {
  let place = autocomplete.getPlace();
  console.log(place);
  console.log(place.formatted_address);
  console.log(place.geometry.location.lat());
  console.log(place.geometry.location.lng());

  if (!place.geometry) {
    //User did not select a predicition; reset the input field
    document.getElementById("autocomplete").placeholder = "Enter your address";
  } else {
    //Display detials about the valid place
    document.getElementById("lat").value = place.geometry.location.lat();
    document.getElementById("lng").value = place.geometry.location.lng();
    document.getElementById("address").value = place.formatted_address;

    var marker = new google.maps.Marker({
      map: map,
      position: place.geometry.location,
    });
    if (place.geometry.viewport) {
      map.fitBounds(place.geometry.viewport);
    } else {
      map.setCenter(place.geometry.location);
      map.setZoom(17);
    }
  }
}
// Bias the autocomplete object to the user's geographical location,
// as supplied by the browser's 'navigator.geolocation' object.
function geolocate() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function (position) {
      var geolocation = {
        lat: position.coords.latitude,
        lng: position.coords.longitude,
      };
      var circle = new google.maps.Circle({
        center: geolocation,
        radius: position.coords.accuracy,
      });
      autocomplete.setBounds(circle.getBounds());
    });
  }
}

/*function geocodeAddress(geocoder, resultsMap) {
    const address = document.getElementById("address").value;
    geocoder
      .geocode({ address: address })
      .then(({ results }) => {
        resultsMap.setCenter(results[0].geometry.location);*/
