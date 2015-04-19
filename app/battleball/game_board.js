//These variables can be changed to create a bigger/smaller field
var field_width = 12;
var sqSize = 100;
var border = 25;
var long_row = 5;

//these variables should not be changed
var hsqSize = sqSize/2;
var short_row = long_row-1;

//This is the main function and will paint in the football field
function draw() {
  var canvas = document.getElementById('canvas');
  if (canvas.getContext) {
    var ctx = canvas.getContext('2d');

    ctx.fillStyle = '#6C0';
    ctx.strokeStyle = 'white';

    for (var i = 1; i <= (field_width-1); i++) {
    	var field_itr = border
    	if(i%2 != 0) {
    		ctx.fillRect(i*sqSize+border, border, sqSize, hsqSize);
    		ctx.strokeRect(i*sqSize+border, border, sqSize, hsqSize);
    		field_itr+=hsqSize
    	}
    	for(var j = long_row; j>1; j--) {
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
	    	for(var j = long_row; j>1; j--) {
    		ctx.fillRect(i*sqSize+border, field_itr, sqSize, sqSize);
    		ctx.strokeRect(i*sqSize+border, field_itr, sqSize, sqSize);
    		field_itr+=sqSize
    	}
		ctx.fillRect(i*sqSize+border, field_itr, sqSize, hsqSize);
		ctx.strokeRect(i*sqSize+border, field_itr, sqSize, hsqSize);
	}
    ball = coordinates(6, 2)
    ctx.fillStyle = 'yellow'
    ctx.fillRect(border + ball.x, border + ball.y, sqSize, ball.size);
    ctx.strokeRect(border + ball.x, border + ball.y, sqSize, ball.size);

    red = coordinates(10, 0)
    ctx.fillStyle = 'red'
    ctx.fillRect(border + red.x, border + red.y, sqSize, red.size);
    ctx.strokeRect(border + red.x, border + red.y, sqSize, red.size);

    blue = coordinates(3, 5)
    ctx.fillStyle = 'blue'
    ctx.fillRect(border + blue.x, border + blue.y, sqSize, blue.size);
    ctx.strokeRect(border + blue.x, border + blue.y, sqSize, blue.size);
  }
}

//This function will take in a row and column.
//The columns start from the left and the rows start from the bottom.
//The output is the x, y coordinates of the upper left pixel of the square and the size of the square
function coordinates(col, row) {
    var o = new Object();
    o.x= sqSize*col;
    if(col%2 != 0 || col == 0 || col ==field_width) {
        if(row==long_row) {
            o.y = 0;
            o.size = hsqSize;
        }
        else {
            o.y = -(row-short_row)*sqSize + hsqSize;
            if(row==0) o.size = hsqSize;
            else o.size = sqSize;
        }
    }
    else {
        o.y = -(row-short_row)*sqSize;
        o.size = sqSize;
    }

    return o;
}