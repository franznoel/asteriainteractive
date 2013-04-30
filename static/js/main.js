var init = function() {
  setLogIn();
}

var changeModal = function(modal_type) {
  var html='';
  if (modal_type=="signup") {
    html+=addControlGroup('fullname','text','Full Name','');
    html+=addControlGroup('username','text','Username','');
    html+=addControlGroup('email','email','Email','');
    html+=addControlGroup('password','password','Password','');
    setModal('Sign Up',html,'account/','Save');
  } else if (modal_type=="login") {
    html+=addControlGroup('username','text','Username','');
    html+=addControlGroup('password','password','Password','');
    html+=addControlGroup(null,'checkbox','Remember me','');
    setModal('Sign In',html,"login/",'Login','');
  } else if(modal_type=="update_account") {
    html+=addControlGroup('fullname','text','Full Name','');
    html+=addControlGroup('username','text','Username','');
    html+=addControlGroup('email','email','Email','');
    html+=addControlGroup('password','password','Password','');
    setModal('Update Account',html,'accounts/','Update Accounts','');
  } else if(modal_type=="create_job") {
    var expiration = getExpirationDate();
    html+=addControlGroup('title','text','Position Title','');
    html+=addControlGroup('description','textarea','Description','')
    html+=addControlGroup('skills','textarea','Skills (comma separated)','')
    html+=addControlGroup('address','textarea','Postal Address','')
    html+=addControlGroup('phone','phone','Phone Number','');
    html+=addControlGroup('link','url','Link','');
    html+=addControlGroup('expiration','date','Expiration',expiration);
    html+=addControlGroup('isPublic','hidden','','');
    setModal('Create Job',html,'job/','Create Job');
  } else if(modal_type=="create_resume") {
    html+=addControlGroup('title','text','Position Title','');
    html+=addControlGroup('description','textarea','Description','');
    html+=addControlGroup('address','textarea','Address','');
    html+=addControlGroup('skills','textarea','Skills (comma separated)','');
    html+=addControlGroup('link','url','Link','');
    html+=addControlGroup('isPublic','hidden','Is Public','public');
    setModal('Create Resume',html,'resume/','Create Resume');
  }
}

var setModal = function(title,html,action,submit) {
  $('#modal_label').html(title);
  $('#modal-content').html(html);
  $('#modal_form').attr("action",action);
  $('#modal_submit').html(submit);
}

var list = function(list_type) {
  $('#list').toggle();
}

$('#opportunity_list a').click(function (e) {
  //alert("Hello");
  //alert($(this).html());
  e.preventDefault();
  $(this).tab('show');
})


$(document).ready(function() {
  $('#user_tooltip').tooltip()
  $('#jobs_tooltip').tooltip()
  $('#resume_tooltip').tooltip()
})

var getExpirationDate = function() {
  var today = new Date();
  var year = today.getFullYear();
  var month = today.getMonth()+2;
  var day = today.getDate();
  if (month < 10) month = '0' + month;
  if (day < 10) day = '0' + day;
  return year + "-" + month + "-"+ day;
}

var addControlGroup = function(name,type,title,value) {
  var html='';
  if (type=='text' || type=='email' || type=='date' || type=='phone' || type=='password' || type=='url') {
    html+='<div class="control-group">';
    html+='<label class="control-label" for="'+name+'">'+title+'</label>';
    html+='<div class="controls"><input type="'+type+'" name="'+name+'" value="'+value+'" placeholder="'+title+'" /></div>';
    html+='</div>';
  } else if (type=="checkbox") {
    html+='<div class="control-group">';
    html+='<div class="controls">';
    html+='<label class="checkbox">';
    html+='<input type="'+type+'"> '+title;
    html+='</label>';
    html+='</div>';
    html+='</div>';
  } else if (type=="textarea") {
    html+='<div class="control-group">';
    html+='<label class="control-label">'+title+'</label>';
    html+='<div class="controls"><textarea name="'+name+'" rows="2" placeholder="'+title+'"></textarea></div>';
    html+='</div>';
  } else if (type=="hidden") {
    html+='<input type="'+type+'" name="'+name+'" value="'+value+'">'
  }
  return html;
}

var setLogIn = function() {
  username = getCookie('username');
  message = getCookie('message');
  var html='';
  // Assign username
  if (username==null) {
    html+='<a href="#modal_sign" onclick="changeModal(\'signup\')" role="button" data-toggle="modal" class="btn btn-default" style="margin:0px;">Sign Up</a>';
    html+='<a href="#modal_sign" onclick="changeModal(\'login\')" role="button" data-toggle="modal" class="btn btn-default" style="margin:0px;">Sign In</a>';
    $('#loggedin').html(html);
  } else {
    html+='<a href="#logout" onclick="deleteCookie(\'username\')"><code style="margin:10px 0 0 0;">Hello, '+username+'</code></a>';
    $('#loggedin').html(html);
  }
  // Alert message
  // If message is not empty, don't pop up
  if (message!=null && message!='') {
    alert(message);
    setCookie('message','',360);
  } 
}
 
function deleteCookie(c_name){
  document.cookie = 'username=; Max-Age=0';
  document.location.reload(true);
}

function getCookie(c_name) {
  var c_value = document.cookie;
  var c_start = c_value.indexOf(" " + c_name + "=");
  if (c_start == -1) {
    c_start = c_value.indexOf(c_name + "=");
  }
  if (c_start == -1) {
    c_value = null;
  } else {
    c_start = c_value.indexOf("=", c_start) + 1;
    var c_end = c_value.indexOf(";", c_start);
    if (c_end == -1) {
      c_end = c_value.length;
    }
    c_value = unescape(c_value.substring(c_start,c_end));
  }
  return c_value;
}

function setCookie(c_name,value,exdays) {
  var exdate=new Date();
  exdate.setDate(exdate.getDate() + exdays);
  var c_value=escape(value) + ((exdays==null) ? "" : "; expires="+exdate.toUTCString());
  document.cookie=c_name + "=" + c_value;
}
