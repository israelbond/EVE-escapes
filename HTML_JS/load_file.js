//open json file from relative directory 
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
//add data to table using getElementById and layout of json file
readTextFile("../swaggerScripts/map_connections.json", function(text){
	    var data = JSON.parse(text);
	    var table = document.getElementById("system_table");
	    var row;
	    var cell0;
	    var cell1;
	    var cell2;
		for (system_id in data.systems){
			row = table.insertRow(0);
			cell0 = row.insertCell(0);
			cell0.innerHTML = data.systems[system_id].system_name;
			cell0.style.backgroundColor = "yellow";
			cell1 = row.insertCell(1);
			cell1.innerHTML = system_id;
			cell1.style.backgroundColor = "deepskyblue"
			for(i = 0; i < data.systems[system_id].connections.length; i++){
				
				cell2 = row.insertCell(2);
				cell2.innerHTML = data.systems[system_id].connections[i];
				cell2.style.backgroundColor = "cornflowerblue"
		}
		}

});
