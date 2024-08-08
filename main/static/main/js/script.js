document.getElementById('backButton').addEventListener('click', function() {
    // Akcja dla przycisku "Powrót"
    $('#roboklockiModal').modal('show'); // Ukryj pierwszy modal
    $('#formularzeModal').modal('hide'); // Pokaż drugi modal
    // Możesz dodać tutaj kod, który przeniesie użytkownika do poprzedniego kroku
  });

  document.getElementById('nextButton').addEventListener('click', function() {
    $('#roboklockiModal').modal('hide'); // Ukryj pierwszy modal
    $('#formularzeModal').modal('show'); // Pokaż drugi modal
  });