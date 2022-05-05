const map = L.map('map', {
    center: [66.1690857076364, 29.161765586689256],
    zoom: 12
});

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoibWFrZXJpODkiLCJhIjoiY2wyc3k5d2NoMDE1YzNjcnl4dHpoNWpyNCJ9.WmaLEB80OWli3v8v8k8fiw'
}).addTo(map);


// L.marker([60.16888443716738, 24.945217269936368]).addTo(map)
//     .bindPopup('<h1>Nitor</h1>')
//     .openPopup();

const setMarker = (lat, long) => {
    // console.log(post)
    L.marker([lat, long]).addTo(map)
        .bindPopup('kuva')
        // .bindPopup('<img src="data:image/jpeg;base64, {{ data }} "><img>')
}

const setMarkers = () => {
    // posts = posts.replace(/&#34;/g, '\'')
    // posts = posts.replace(/&#39;/g, "")
    // posts = posts.replace(/\]/g, '"')
    // posts = posts.replace(/\[/g, '"')
    // posts = posts.split('},')
    // console.log(posts)
    // posts = posts.map(post => post.concat('}'))
    // posts = posts.map(post => post.replace('"',''))
    // console.log(posts)
    // posts = posts.map(post => post.replace(/'/g, '"'))
    // console.log(posts)
    // posts = posts.map(post => JSON.parse(post))
    // console.log(posts)
    // console.log(JSON.parse(posts))
    setMarker(66.1690857076364, 29.161765586689256)
    setMarker(66.16769778169346, 29.13931099097882)
    setMarker(66.16944885418808, 29.155163414833567)
    setMarker(66.16988654330092, 29.170672500752087)
}

const showAddNewPost = () => {
	const s = document.getElementById("c");
	const bb = document.getElementById("newbutton");
	bb.style.display = "none";
	s.style.display = "inline-block";
}