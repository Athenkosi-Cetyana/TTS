$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				user1 : $('#user').val(),
				password1 : $('#pass').val()
			},
			type : 'POST',
			url : '/login'
		})
		.done(function(data) {

			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			}
			else {
				$('#successAlert').text(data.user1).show();
				$('#errorAlert').hide();
			}
		});
		event.preventDefault();
	});

});