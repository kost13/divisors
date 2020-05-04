function show_number(id){
    var num = document.getElementById(id)
    // alert('ok');
    var opacity = 0    
    var animation_id = setInterval(frame, 10);
    function frame() {
      if (opacity == 1) {
        clearInterval(animation_id);
      } else {
        opacity+= 0.02
        num.style.opacity = opacity        
      }
    }
}
