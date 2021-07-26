function initMap() {
  const berlin = { lat: 52.520008, lng: 13.404954 };
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 13,
    center: berlin,
  });
  const geocoder = new google.maps.Geocoder();
  document.getElementById("submit").addEventListener("click", () => {
    geocodeAddress(geocoder, map);
  });

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

  function geocodeAddress(geocoder, resultsMap) {
    const address = document.getElementById("address").value;
    geocoder
      .geocode({ address: address })
      .then(({ results }) => {
        resultsMap.setCenter(results[0].geometry.location);
        const marker = new google.maps.Marker({
          map: resultsMap,
          position: results[0].geometry.location,
          title: "InfoWindow",
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
      })
      .catch((e) =>
        alert("Geocode was not successful for the following reason: " + e)
      );
  }
}
