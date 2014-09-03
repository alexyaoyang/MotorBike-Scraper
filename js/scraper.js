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
					html:'<a class="pull-left" href="#"><img class="media-object" src="'+json[i].image+'"></a><div class="media-body"><h4 class="media-heading">'+json[i].model+'</h4></div>'
				});
				media.appendTo('#bike-container');
			}
		});
	}
}


/*
						<div class="col-xs-12">
							<div class="media">
							  <a class="pull-left" href="#">
							    <img class="media-object" src="">
							  </a>
							  <div class="media-body">
							    <h4 class="media-heading"></h4>
							  </div>
							</div>
						</div>
*/