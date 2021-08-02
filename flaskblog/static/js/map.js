console.log("it works");

function initMap() {
  //var locations = [
  //["Battersea Park Road", 51.4705666, -0.1728984, 2],
  //["Webbs Road", 51.4575458, -0.165245, 1],
  //];

  var map = new google.maps.Map(document.getElementById("map"), {
    zoom: 12,
    center: new google.maps.LatLng(52.52, 13.405),
    mapTypeId: google.maps.MapTypeId.ROADMAP,
  });

  var infowindow = new google.maps.InfoWindow();

  var marker, i;

  var icon = {
    url: "https://www.google.com/intl/en_us/mapfiles/ms/micons/blue-dot.png",
  };

  var marker = new google.maps.Marker({
    map: map,
    animation: google.maps.Animation.DROP,
    icon: icon,
  });

  for (i = 0; i < locations2.length; i++) {
    marker = new google.maps.Marker({
      position: new google.maps.LatLng(locations2[i][1], locations2[i][2]),
      map: map,
      icon: icon,
    });

    google.maps.event.addListener(
      marker,
      "mouseover",
      (function (marker, i) {
        return function () {
          infowindow.setContent(locations2[i][0]);
          infowindow.open(map, marker);
        };
      })(marker, i)
    );
  }
}
