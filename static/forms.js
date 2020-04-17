$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				user1 : $('#user').val(),
				password1 : $('#pass').val()
			},
			type : 'GET',
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

/**
 * 
  CODE FOR LOGIN AUTHENTICATION ON THE ROUTE MODULE:
	if request.form == 'GET':
        print("Reached?")
    user1 = request.form.get('user')
    password1 = request.form.get('pass')
    
    if user1 and password1:
        newUser = user1[::-1]
        return jsonify({'user1' : newUser})

    return jsonify({'error' : 'Incorrect username or password'})

 * 
 */