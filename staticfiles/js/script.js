const button = document.getElementById("addnote_button");
const box = document.getElementById("addnote_background"); 
const stickynote_button = document.getElementById("addSnote_button"); 
const stickynote_box = document.getElementById("addSnote_background")



button.addEventListener("click", () => {
  
    if (box.style.display === "flex") {
        box.style.display = "none";  // Hide the box if it's visible
      } else {
        box.style.display = "flex";  // Show the box if it's hidden
      }  
});

stickynote_button.addEventListener("click", () => {
  
    if (stickynote_box.style.display === "flex") {
        stickynote_box.style.display = "none";  // Hide the box if it's visible
      } else {
        stickynote_box.style.display = "flex";  // Show the box if it's hidden
      }  
});

