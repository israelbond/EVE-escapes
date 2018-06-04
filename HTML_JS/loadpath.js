
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

readTextFile("path.json", function(text) {
	    var data = JSON.parse(text);
	    var table = document.getElementById("path");
	    var row;
	    var cell0;
	    var cell1;
	    var cell2;
	    row = table.insertRow(0);
	    var max = data.length
	    for ( system_name in data ) {
            cell0 = row.insertCell(0);
            cell0.innerHTML = data[max-1];
            max = max - 1;
        }

});