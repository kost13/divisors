function show_number(id){
    var num = document.getElementById(id)
    var opacity = 0    
    var id = setInterval(frame, 10);
    function frame() {
      if (opacity == 1) {
        clearInterval(id);
      } else {
        opacity+= 0.01; 
        num.style.opacity = opacity        
        // num.style.width = opacity + "px"; 
      }
    }
}
