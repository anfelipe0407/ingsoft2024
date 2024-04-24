
function showStep(step) {
  document.querySelectorAll('.step-content').forEach(content => {
    content.classList.remove('active');
  });
  document.getElementById('step' + step).classList.add('active');

  document.querySelectorAll('.step').forEach(stepElement => {
    stepElement.classList.remove('active');
  });
  document.querySelector('.step:nth-child(' + step + ')').classList.add('active');
}

