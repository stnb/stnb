var EditarLlengua = {
	llengues: ["ca", "es", "en"],
	init: function()  {

	},

	canviar_llengua: function(lleng)  {
		for (var i = 0; i < EditarLlengua.llengues.length; i++)  {
			var	camps_p = null;

			camps = $(".translation__" + EditarLlengua.llengues[i]);
			camps_p = camps.parent();

			if (lleng == EditarLlengua.llengues[i])  {
				for (var j = 0; j < camps.length; j++)  {
					var camp, camp_id, camp_width, camp_height;
					camp = camps.eq(j);

					camp_id = camp[0].id;
					camp_width = camp.eq(0).attr('data-width');
					camp_height = camp.eq(0).attr('data-height')

					if (camp_width)
						$('#'+camp_id+'_ifr').css('width', camp_width);
					if (camp_height)
						$('#'+camp_id+'_ifr').css('height', camp_height);
				}

				camps_p.show();
			}
			else  {
				camps_p.hide();
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
