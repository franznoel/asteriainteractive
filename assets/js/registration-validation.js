$('#registration').validate({
  //errorLabelContainer: "#alert-messages",
  //wrapper: "li",
  rules: {
    contactName: { required: true },
    organizationName: { required: true },
    customerDomain: { required: true },
    phoneNumber: { required: true },
    alternateEmail: { required: true, email: true },
    addressLine1: { required: true },
    region: { required: true },
    locality: { required: true },
    postalCode: { required: true, minlength: 5 }, 
  },
  messages: {
    contactName: { required: '<div style="font-style:italic;font-weight:normal;color:red;">Full name must be filled out.</div>', },
    organizationName: { required: '<div style="font-style:italic;font-weight:normal;color:red;">Company name must be filled out.</div>' },
    customerDomain: { required: '<div style="font-style:italic;font-weight:normal;color:red;">Customer domain must be filled out.</div>'},
    phoneNumber: { required: '<div style="font-style:italic;font-weight:normal;color:red;">Phone number must be filled out.</div>' },
    alternateEmail: { 
      required: '<div style="font-style:italic;font-weight:normal;color:red;">Alternate email address must be filled out.</div>',
      email: '<div style="font-style:italic;font-weight:normal;color:red;">The email should be in the correct format.</div>',
    },
    addressLine1: { required: '<div style="font-style:italic;font-weight:normal;color:red;">Address line 1 must be filled out.</div>'},
    region: { required: '<div style="font-style:italic;font-weight:normal;color:red;">State must be filled out.</div>'},
    locality: { required: '<div style="font-style:italic;font-weight:normal;color:red;">City must be filled out.</div>'},
    postalCode: {
      minlength: '<div style="font-style:italic;font-weight:normal;color:red;">Postal code should have a minimum of 5 numbers.</div>',
      required: '<div style="font-style:italic;font-weight:normal;color:red;">The postal code should be filled out.</div>', 
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