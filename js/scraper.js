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
					class:'media panel panel-default',
					html:'<a class="pull-left" href="#"><div class="media-object" style="background-image:url('+json[i].image+')"></div></a><div class="media-body"><h4 class="media-heading">'+json[i].model+'</h4></div>'
				});
				media.appendTo('#bike-container');
			}
		});
	}
}