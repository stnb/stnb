var EditarLlengua = {
	llengues: ["ca", "es", "en"],
	init: function()  {

	},

	canviar_llengua: function(lleng)  {
		for (var i = 0; i < EditarLlengua.llengues.length; i++)  {
			var lleng_div = null;

			lleng_div = $(".trans-" + EditarLlengua.llengues[i]);
			if (lleng == EditarLlengua.llengues[i])  {
				var areas = lleng_div.find("textarea");
				for (var j = 0; j < areas.length; j++)  {
					var ta = areas.eq(j);
					console.log(ta.next());
					if (ta.next(".mceEditor").length > 0)  {
						$("#"+ta.attr("id")+"_tbl").css("width", ta.css("width"));
						$("#"+ta.attr("id")+"_tbl").css("height", ta.css("height"));
						$("#"+ta.attr("id")+"_ifr").css("height", "100%");
					}
				}
				lleng_div.show();
				var ta = lleng_div.find("textarea");
				
				console.log(ta);
				console.log(ta.width());
				console.log(ta.css("width"));
				$("#"+ta.attr("id")+"_tbl").css("width", ta.css("width"));

			}
			else  {
				lleng_div.hide();
			}
		}

		// Canviar "class" per la llengua activa
		$("#llengua-formulari .editar-lleng").removeClass("actiu");
		$("#editar-"+lleng).addClass("actiu");
	},

	elegir_llengua_base: function()  {
		var	llengua_base, llengues;

		llengues = $(".llengua");
		for (var j = 0; j < llengues.length; j++)  {
			if ($(llengues[j]).hasClass('current'))  {
				for (var i = 0; i < EditarLlengua.llengues.length; i++)  {
					if ($(llengues[j]).hasClass(EditarLlengua.llengues[i]))  {
						llengua_base = EditarLlengua.llengues[i];
					}
				}
			}
		}
		
		EditarLlengua.canviar_llengua(llengua_base);
	}

};
	
$(document).ready(function() {
	EditarLlengua.elegir_llengua_base();
});
