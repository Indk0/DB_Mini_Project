function openForm() {
  // Clear the form fields (if any)
  document.getElementById("noteContent").value = "";

  // Open the modal
  document.getElementById("modal-container").style.display = "flex";
}

function closeForm() {
  document.getElementById("modal-container").style.display = "none";
}
