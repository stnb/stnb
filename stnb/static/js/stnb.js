var EditarLlengua = {
	llengues: ["ca", "es", "en"],
	init: function()  {

	},

	canviar_lengua: function(lleng)  {
		console.log("lleng:", lleng);
		for (var i = 0; i < EditarLlengua.llengues.length; i++)  {
			var	camps_p = null;

			camp = $(".translation__" + EditarLlengua.llengues[i]);
			camps_p = camp.parent();

			if (lleng == EditarLlengua.llengues[i])  {
				camps_p.show();
				var camp_id, camp_width, camp_height;
				camp_id = camp[0].id;
				camp_width = camp.eq(0).attr('data-width');
				camp_height = camp.eq(0).attr('data-height')
				console.log(camp_width);

				console.log($('#'+camp_id+'_ifr'));
				if (camp_width)
					$('#'+camp_id+'_ifr').css('width', camp_width);
				if (camp_height)
					$('#'+camp_id+'_ifr').css('height', camp_height);
			}
			else  {
				camps_p.hide();
			}
		}

	},

	elegir_llengua_base: function()  {
		var	llengua_base, llengues;

		llengues = $(".llengua");
		for (var j = 0; j < llengues.length; j++)  {
			if ($(llengues[j]).hasClass('current'))  {
				console.log(llengues);
				for (var i = 0; i < EditarLlengua.llengues.length; i++)  {
					if ($(llengues[j]).hasClass(EditarLlengua.llengues[i]))  {
						llengua_base = EditarLlengua.llengues[i];
					}
				}
			}
		}
		
		console.log(llengua_base);
		EditarLlengua.canviar_lengua(llengua_base);
	}

};
	
$(document).ready(function() {
	EditarLlengua.elegir_llengua_base();
});
