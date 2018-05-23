function readTextFile(file, callback) {
    var rawFile = new XMLHttpRequest();
    rawFile.overrideMimeType("application/json");
    rawFile.open("GET", file, true);
    rawFile.onreadystatechange = function() {
    if (rawFile.readyState === 4 && rawFile.status == "200") {
    callback(rawFile.responseText);
         }
    }
    rawFile.send(null);
}

readTextFile("map_connections.json", function(text){
	    var data = JSON.parse(text);
		for (system_id in data.systems){
			var record = "<tr><td>" + system_id + "</td><td>";
			for(connection in data.systems[system_id].connections){
				record +=  connection + "</td><td>";
			}
			record +=  "</td></tr>";
		}
});
