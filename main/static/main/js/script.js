function nextStep(step) {
  // Ukryj wszystkie tab-pane
  document.querySelectorAll(".tab-pane").forEach(function (pane) {
    pane.classList.remove("active", "show");
  });

  // Oznacz wszystkie kroki jako nieaktywne
  document.querySelectorAll(".progress-step").forEach(function (step) {
    step.classList.remove("active", "completed");
  });

  // Pokaż aktualny krok i oznacz poprzednie kroki jako ukończone
  for (let i = 1; i <= step; i++) {
    document.getElementById("step" + i).classList.add("completed");
  }
  document.getElementById("step" + step).classList.add("active");

  // Pokaż odpowiednią tab-pane
  document.getElementById(stepPaneId(step)).classList.add("active", "show");
}

function prevStep(step) {
  // Ukryj wszystkie tab-pane
  document.querySelectorAll(".tab-pane").forEach(function (pane) {
    pane.classList.remove("active", "show");
  });

  // Oznacz wszystkie kroki jako nieaktywne
  document.querySelectorAll(".progress-step").forEach(function (step) {
    step.classList.remove("active", "completed");
  });

  // Pokaż aktualny krok i oznacz poprzednie kroki jako ukończone
  for (let i = 1; i < step; i++) {
    document.getElementById("step" + i).classList.add("completed");
  }
  document.getElementById("step" + step).classList.add("active");

  // Pokaż odpowiednią tab-pane
  document.getElementById(stepPaneId(step)).classList.add("active", "show");
}

function stepPaneId(step) {
  if (step === 1) return "personalInformation";
  if (step === 2) return "education";
  if (step === 3) return "workExperience";
  if (step === 4) return "userPhoto";
}
