(function () {
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  var gate = document.querySelector("[data-age-gate]");
  if (!gate) return;
  var accepted = false;
  try { accepted = localStorage.getItem("museDonationAgeConfirmed") === "yes"; } catch (e) {}
  if (accepted) gate.hidden = true;

  var enter = gate.querySelector("[data-age-enter]");
  var leave = gate.querySelector("[data-age-leave]");
  if (enter) enter.addEventListener("click", function () {
    try { localStorage.setItem("museDonationAgeConfirmed", "yes"); } catch (e) {}
    gate.hidden = true;
  });
  if (leave) leave.addEventListener("click", function () {
    window.location.href = "index.html";
  });
})();
