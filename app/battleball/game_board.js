function draw() {
  var canvas = document.getElementById('canvas');
  if (canvas.getContext) {
    var ctx = canvas.getContext('2d');


    var field_width = 12;
    var sqSize = 100;
    var hsqSize = sqSize/2;
    var border = 25;
    ctx.fillStyle = '#6C0';
    ctx.strokeStyle = 'white';

    for (var i = 1; i <= (field_width-1); i++) {
    	var field_itr = border
    	if(i%2 != 0) {
    		ctx.fillRect(i*sqSize+border, border, sqSize, hsqSize);
    		ctx.strokeRect(i*sqSize+border, border, sqSize, hsqSize);
    		field_itr+=hsqSize
    	}
    	for(var j = 5; j>1; j--) {
    		ctx.fillRect(i*sqSize+border, field_itr, sqSize, sqSize);
    		ctx.strokeRect(i*sqSize+border, field_itr, sqSize, sqSize);
    		field_itr+=sqSize
    	}
    	if(i%2 != 0) {
    		ctx.fillRect(i*sqSize+border, field_itr, sqSize, hsqSize);
    		ctx.strokeRect(i*sqSize+border, field_itr, sqSize, hsqSize);
    	}
    	else {
    		ctx.fillRect(i*sqSize+border, field_itr, sqSize, sqSize);
    		ctx.strokeRect(i*sqSize+border, field_itr, sqSize, sqSize);
    	}
	}

	for (i = 0; i<= field_width; i+=(field_width)) {
		if(i==0) ctx.fillStyle = '#09F';
		else if (i==field_width) ctx.fillStyle = '#F30';
		var field_itr = border
		ctx.fillRect(i*sqSize+border, border, sqSize, hsqSize);
		ctx.strokeRect(i*sqSize+border, border, sqSize, hsqSize);
		field_itr+=hsqSize
	    	for(var j = 5; j>1; j--) {
    		ctx.fillRect(i*sqSize+border, field_itr, sqSize, sqSize);
    		ctx.strokeRect(i*sqSize+border, field_itr, sqSize, sqSize);
    		field_itr+=sqSize
    	}
		ctx.fillRect(i*sqSize+border, field_itr, sqSize, hsqSize);
		ctx.strokeRect(i*sqSize+border, field_itr, sqSize, hsqSize);
	}
  }
}