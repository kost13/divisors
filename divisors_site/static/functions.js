
const hovered_number_color_pair = 'wheat'
const hovered_number_color_single = '#b6dc9a'
const normal_number_color  = 'white'

function initialize_divisors(divisors, number){
  
  show_animated('list')    
  add_hover_events(divisors, number)
}

function show_animated(id){
    var num = document.getElementById(id)    
    var opacity = 0    
    var animation_id = setInterval(frame, 10);
    function frame() {
      if (opacity >= 1) {
        clearInterval(animation_id);
      } else {
        opacity+= 0.02
        num.style.opacity = opacity        
      }
    }
}

function add_hover_events(divisors, number){    

  var divisors_pairs = get_divisors_pairs(divisors, number)
  
  for( pair of divisors_pairs){        
    if(pair.length === 1){
      add_hover_event_for_single(pair[0])  
    } else {
      add_hover_event_for_pair(pair)
    }       
  }
}

function add_hover_event_for_single(num){
  var id = "divisor" + (num + 1).toString()    
  const num_obj = document.getElementById(id);

  num_obj.addEventListener('mouseenter', e => {
    num_obj.style.color = hovered_number_color_single;
  });

  num_obj.addEventListener('mouseleave', e => {
    num_obj.style.color = normal_number_color
  });
}

function add_hover_event_for_pair(pair){
  var id1 = "divisor" + (pair[0] + 1).toString()    
  const num_obj1 = document.getElementById(id1);

  var id2 = "divisor" + (pair[1] + 1).toString()    
  const num_obj2 = document.getElementById(id2);

  for(obj of [num_obj1, num_obj2]){
    obj.addEventListener('mouseenter', e => {
      num_obj1.style.color = hovered_number_color_pair
      num_obj2.style.color = hovered_number_color_pair
    });
  
    obj.addEventListener('mouseleave', e => {
      num_obj1.style.color = normal_number_color
      num_obj2.style.color = normal_number_color
    });
  }  
}

function get_divisors_pairs(divisors, number){  
  if(divisors.length === 1){
    return [[divisors[0]]]
  }

  var divisors_pairs = []
  for( var i=0; i<divisors.length - 1; i++){
    if(divisors[i] * divisors[i+1] === number){
      divisors_pairs.push([i, i+1])
      i++
    } else {
      divisors_pairs.push([i])
    }    
  }
  return divisors_pairs
}