var Scraper = {
	load:function(){
		$.getJSON("bikes.json", function () {
			console.log("done retreiving!");
		}).done(function(json){
			console.log(json);
			for(var i=0;i<json.length;i++){
				console.log(json[i].image);
				console.log(json[i].contact);
				var media = $('<div/>',{
					class:'media panel panel-default'
				});
				var pullLeft = $('<a/>',{
					href:json[i].href,
					class:"pull-left",
					html:'<div class="media-object" style="background-image:url('+json[i].image+')"></div>'
				});
				var mediaBody = $('<div/>',{
					class:"media-body"
				});
				var table = $('<table/>',{
					class:"table table-body table-hover"
				});
				var tr1 = $('<tr/>',{
					class:"table-row",
					html:"<td><strong>Price: </strong>"+json[i].price+"</td><td><strong>COE Expire: </strong>"+json[i].expire+"</td><td><strong>Name: </strong>"+json[i].name+"</td>"
				});
				var tr2 = $('<tr/>',{
					class:"table-row",
					html:"<td><strong>Price/Day: </strong>$"+json[i].ppd+"</td><td><strong>Reg Date: </strong>"+json[i].reg+"</td><td><strong>No: </strong>"+json[i].contact+"</td>"
				});
				var tr3 = $('<tr/>',{
					class:"table-row",
					html:"<td><strong>Model: </strong>"+json[i].model+"</td><td><strong>Description: </strong>"+json[i].desc+"</td><td></td>"
				});
				tr1.appendTo(table);
				tr2.appendTo(table);
				tr3.appendTo(table);
				table.appendTo(mediaBody);
				pullLeft.appendTo(media);
				mediaBody.appendTo(media);
				media.appendTo('#bike-container');
			}
		});
	}
}
