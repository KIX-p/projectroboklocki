document.getElementById('nextButton').addEventListener('click', function() {
  $('#firstpage').modal('hide'); 
  $('#secondpage').modal('show');
});

document.getElementById('nextButton1').addEventListener('click', function() {
  $('#secondpage').modal('hide'); 
  $('#thirdpage').modal('show');
});

document.getElementById('nextButton2').addEventListener('click', function() {
  $('#thirdpage').modal('hide'); 
  $('#fourthpage').modal('show');
});

document.getElementById('backButton1').addEventListener('click', function() {
  $('#secondpage').modal('hide'); 
  $('#firstpage').modal('show'); 
});

document.getElementById('backButton2').addEventListener('click', function() {
  $('#thirdpage').modal('hide'); 
  $('#secondpage').modal('show');
});

document.getElementById('backButton3').addEventListener('click', function() {
  $('#fourthpage').modal('hide'); 
  $('#thirdpage').modal('show');
});

document.querySelector('.custom-upload-button').addEventListener('click', function() {
  document.querySelector('.upload-box input[type="file"]').click();
});


