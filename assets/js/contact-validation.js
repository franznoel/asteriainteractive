$("#contact").validate({
  errorLabelContainer: "#alert-messages",
  // wrapper: "li",
  rules: {
    fullname: { required: true, minlength : 2 },
    email: { required: true , email : true },
    phoneNumber: { phoneUS : true },
    website: { url : true },
    subject: { required: true },
    message: { required: true, minlength : 3 },
  },
  messages: {
    fullname: {
    	required: '<div style="font-style:italic;font-weight:normal;color:red;">Full name is a required information</div>',
    	minlength : '<div style="font-style:italic;font-weight:normal;color:red;">Minimum of 2 letters required</div>',
    },
    email: {
    	required: '<div style="font-style:italic;font-weight:normal;color:red;">Company name must be filled out.</div>',
    	email : '<div style="font-style:italic;font-weight:normal;color:red;">Email should be in the correct format</div>',
    },
    phoneNumber: { phoneUS: '<div style="font-style:italic;font-weight:normal;color:red;">Should be in phone US format.</div>' },
    website: { url: '<div style="font-style:italic;font-weight:normal;color:red;">Website should be in a url format.</div>' },
    subject: { 
      required: '<div style="font-style:italic;font-weight:normal;color:red;">Alternate email address must be filled out.<div>',
    },
    message: { 
    	required: '<div style="font-style:italic;font-weight:normal;color:red;">This is a required message.</div>',
    	minlength: '<div style="font-style:italic;font-weight:normal;color:red;">Please write a message.</div>',
    },
  },
  submitHandler: function(form) {
    var alertMessages = $('#alert-messages').html().length;

    if (alertMessages<=0) {
      $('#alert-messages').show();
    } else {
      $('#alert-messages').hide();
    }
    $(form).ajaxSubmit();
  }
});