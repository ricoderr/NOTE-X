const button = document.getElementById("addnote_button");
const box = document.getElementById("addnote_background");



button.addEventListener("click", () => {
  
    if (box.style.display === "flex") {
        box.style.display = "none";  // Hide the box if it's visible
      } else {
        box.style.display = "flex";  // Show the box if it's hidden
      }  
});

function toggleBox() { 
  const box = document.getElementById('viewnote_background');

  if (box.style.display === "flex") {
    box.style.display = "none";  // Hide the box if it's visible
  } else {
    box.style.display = "flex";  // Show the box if it's hidden
  }  

}