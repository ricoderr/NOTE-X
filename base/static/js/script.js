const button = document.getElementById("addnote_button");
const box = document.getElementById("addnote_background");
const editNote_button = document.getElementById("note_link");
const editNote_box = document.getElementById("editNote")


button.addEventListener("click", () => {
  
    if (box.style.display === "flex") {
        box.style.display = "none";  // Hide the box if it's visible
      } else {
        box.style.display = "flex";  // Show the box if it's hidden
      }  
});

button.addEventListener("click", () => {
  

});
