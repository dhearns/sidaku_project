const copy = "&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors";
const url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
const layer = L.tileLayer(url, { attribution: copy });
const map = L.map("map", { layers: [layer] });

const markers = JSON.parse(document.getElementById("markers-data").textContent);

let feature = L.geoJSON(markers, {
  onEachFeature: function (feature, layer) {
    var popupContent = "<b>Name:</b> " + feature.properties.nama +
                        '<br><a href="http://127.0.0.1:8000/' + feature.properties.label + '/' + feature.properties.pk + '/" >More details</a>';

    layer.bindPopup(popupContent);
  },
}).addTo(map);

map.fitBounds(feature.getBounds(), { padding: [100, 100] });