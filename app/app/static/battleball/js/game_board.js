window.onload = function(){
    //var request = new XMLHttpRequest();
    //request.open('GET', 'http://localhost:8000/battleball/board/1/game/', false);  // `false` makes the request synchronous
    //request.send(null);

    //if (request.status === 200) {
    //    json = JSON.parse(request.responseText);
    //}
    //arr = json.game.board;
    draw();
}

//These variables can be changed to create a bigger/smaller field
var field_width = 12,
    sqSize = 100,
    border = 25,
    long_row = 5,
    pieces = 3,
    selectedPiece = null,
    ctx = null,
    HOME_TEAM = 0,
    AWAY_TEAM = 1,
    currentTurn = HOME_TEAM;

//these variables should not be changed
var hsqSize = sqSize/2,
    short_row = long_row-1;


var arr = [     ['E', 'E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E', 'E'],
                ['E', '8h', 'E', '2h', 'E'],
                ['E', 'E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'B', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E', 'E'],
                ['E', '2a', 'E', '8a', 'E'],
                ['E', 'E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E', 'E']      ];

var home = [
                {"injured": 0,
                 "name": "running back",
                 "psize": 1,
                 "has_ball": false,
                 "roll_size": 20,
                 "position": {"xpos": 2, "ypos": 1}},
                {"injured": 0,
                 "name": "lineman",
                 "psize": 1,
                 "has_ball": false,
                 "roll_size": 8,
                 "position": {"xpos": 2, "ypos": 3}}
            ];
var away =  [
                {"injured": 0,
                 "name": "running back",
                 "psize": 1,
                 "has_ball": false,
                 "roll_size": 20,
                 "position": {"xpos": 10, "ypos": 3}},
                {"injured": 0,
                 "name": "lineman",
                 "psize": 1,
                 "has_ball": false,
                 "roll_size": 8,
                 "position": {"xpos": 10, "ypos": 1}}
            ];


document.addEventListener("DOMContentLoaded", draw, false);

//This is the main function and will paint in the football field
function draw() {
    var canvas = document.getElementById('canvas');
    if (canvas.getContext) {
        ctx = canvas.getContext('2d');

        gameboard();
        canvas.addEventListener("click", getPosition, false);
    }
    else alert("Canvas not supported!");
}

//Returns the coordinates of the mouse
function getPosition(event) {
    var rect = canvas.getBoundingClientRect();
    console.log(rect.top);
    var x = event.pageX,
        y = event.pageY - rect.top;
    if (x === undefined) {
        x = event.clientX + document.body.scrollLeft;// + document.documentElement.scrollLeft;
        y = event.clientY + document.body.scrollTop;//    + document.documentElement.scrollTop;
    }
    
    //select block that has been clicked
    var clickedBlock = position(x, y);

    console.log(x + ' , ' + y);
    console.log(clickedBlock.row +' , ' + clickedBlock.col);

    if (selectedPiece === null) checkIfPieceClicked(clickedBlock);
    else processMove(clickedBlock);
}


function roll(roll_size) {
    /*
    This function creates a random number from 1- roll size
   */
    proll = Math.floor((Math.random() * roll_size) + 1);
    return proll;
}

//This function will create a board
function gameboard() {
    // fill in long rows
    for (var i = 1; i <= (field_width-1); i+=2)
        for (var j = 0; j <= long_row; j++) fill_space(i, j, arr[i][j]);
    // fill in short rows
    for (i = 2; i <= (field_width-1); i+=2)
        for (j = 0; j <= short_row; j++) fill_space(i, j, arr[i][j]);
    // fill in endzones
    for (i = 0; i <= field_width; i+=field_width)
        for (j = 0; j <= long_row; j++) fill_space(i, j, arr[i][j]);
}


function fill_space(col, row, square_identifier) {
    /* 
   This function will take in the desired spot and piece indicator 
   and create a space

   Input: col = column that the square will will occupy
          row = row that the square will occupy
          square_identifier = E, X, B, #a, identifies what type of square
                               is created

    */
    ctx.strokeStyle = 'white';
    ctx.lineWidth = 1;
    var team = square_identifier.charAt(square_identifier.length-1)
    // Select color of space
    if (col === 0 && square_identifier === 'E') ctx.fillStyle = '#09D';
    else if (col == field_width && square_identifier === 'E') ctx.fillStyle = '#F55';
    else if (square_identifier === 'E') ctx.fillStyle = '#6C0';
    else if (square_identifier === 'B') ctx.fillStyle = 'yellow';
    else if (square_identifier === 'X') ctx.fillStyle = 'black';
    else if (team === 'h') ctx.fillStyle = 'blue';
    else if (team === 'a') ctx.fillStyle = 'red';
    
    // get pieces coordinate and size
    var piece = coordinates(col, row);

    //place space on board
    ctx.fillRect(border + piece.x, border + piece.y, sqSize, piece.size);
    ctx.strokeRect(border + piece.x, border + piece.y, sqSize, piece.size);
}

//This function will take in a row and column.
//The columns start from the left and the rows start from the bottom.
//The output is the x, y coordinates of the upper left pixel of the square and the size of the square
function coordinates(col, row) {
    var o = new Object({});
    o.x= sqSize*col;
    // If enzone or long row
    if(col%2 !== 0 || col === 0 || col === field_width || row < 0) {
        // if top space
        if(row==long_row) {
            o.y = 0;
            o.size = hsqSize;
        }
        else {
            o.y = -(row-short_row)*sqSize + hsqSize;
            if(row === 0) o.size = hsqSize;
            else o.size = sqSize;
        }
    }
    // If short row
    else {
        o.y = -(row-short_row)*sqSize;
        o.size = sqSize;
    }

    return o;
}

function position(posx, posy) {
    /*
    This function returns the coordinate of the space selected
    */
    var o = new Object({});

    // Gets y coordinate
    o.col = Math.floor((posx-border)/sqSize);

    var board_bottom = long_row*sqSize+border;
    var yfix = -(posy - border - long_row*sqSize);
    var edge_right = (field_width+1)*sqSize+border;
    if(posy <= board_bottom && posy >= border) {
        if(o.col%2 !== 0 || o.col === 0 || o.col === field_width) {
            if(yfix < hsqSize) o.row = 0;
            else o.row = Math.floor((yfix+hsqSize)/sqSize);
        }
        else o.row = Math.floor(yfix/sqSize);
    }
    else o.row = -1;
    return o;
}


function checkIfPieceClicked(clickedBlock) {
    var pieceAtBlock = getPieceAtBlock(clickedBlock);
    if (pieceAtBlock !== null)
        selectPiece(pieceAtBlock);
}

function getPieceAtBlock(clickedBlock) {
    var team = (currentTurn === HOME_TEAM ? home : away);

    return getPieceAtBlockForTeam(team, clickedBlock);
}

function getPieceAtBlockForTeam(teamOfPieces, clickedBlock) {

    var curPiece = null,
        iPieceCounter = 0,
        pieceAtBlock = null;

    for (iPieceCounter = 0; iPieceCounter < teamOfPieces.length; iPieceCounter++) {

        curPiece = teamOfPieces[iPieceCounter];

        if (curPiece.injured === 0 && curPiece.position.xpos === clickedBlock.col &&
            curPiece.position.ypos === clickedBlock.row) {
                curPiece.itr = iPieceCounter;
                pieceAtBlock = curPiece;
                iPieceCounter = teamOfPieces.length;
        }
    }

    return pieceAtBlock;
}

function selectPiece(pieceAtBlock) {
    // Draw outline
    ctx.strokeStyle = 'white';
    ctx.lineWidth = 4;

    var piece = coordinates(pieceAtBlock.position.xpos, pieceAtBlock.position.ypos);
    ctx.strokeRect(border + piece.x+2, border + piece.y+2, sqSize-4, piece.size-4);

    selectedPiece = pieceAtBlock;
}

function removeSelection(selectedPiece) {

    fill_space(selectedPiece.position.xpos, selectedPiece.position.ypos,
        arr[selectedPiece.position.xpos][selectedPiece.position.ypos]);
    // add line to draw sprite
}

function processMove(clickedBlock) {
    var pieceAtBlock = getPieceAtBlock(clickedBlock);
    if (pieceAtBlock !== null) {
        removeSelection(selectedPiece);
        checkIfPieceClicked(clickedBlock);
    }

    else if (canSelectedMoveToBlock(selectedPiece, clickedBlock) === true)
        //move(clickedBlock.col, clickedBlock.row, arr[clickedBlock.col][clickedBlock.row]);
        movePiece(clickedBlock);
}

//This function would check that the tile is not occupied by ally or X and that it's only 1 move away.
function canSelectedMoveToBlock(selectedPiece, clickedBlock)
{
    var col = selectedPiece.position.xpos,
        row = selectedPiece.position.ypos,
        occounter, nextMove=[], bNextRowEmpty,
        u={}, d={}, ul={}, dl={}, ur={}, dr={}, l={}, r={},
        occupied=[];
    d.col = u.col = col;
    ul.col = dl.col = l.col = col-1;
    ur.col = dr.col = r.col = col+1;
    d.row = row-1;
    u.row = row+1;
    if(col === 0) {
        ul.row = row+1;
        l.row = ur.row = row;
        dl.row = dr.row = row-1;
    }
    else if(col === 0) {
        ur.row = row;
        ul.row = r.row = row;
        dl.row = dr.row = row-1;
    }
    else if(col%2 !== 0) {
        dr.row = dl.row = row-1;
        ur.row = ul.row = row;
    }
    else {
        dr.row = dl.row = row;
        ur.row = ul.row = row+1;
    }
    occupied.push(u, d, ul, dl, ur, dr, l, r);
    nextMove.col = selectedPiece.position.xpos;
    nextMove.row = selectedPiece.position.ypos;

    for(occounter=0; occounter<occupied.length; occounter++) {
        if (occupied[occounter].row == clickedBlock.row &&
            occupied[occounter].col == clickedBlock.col &&
            occupied[occounter].col>=0 && occupied[occounter].col<=field_width) {
            nextMove = occupied[occounter];
        }
    }
    //alert(arr[nextMove.col][nextMove.row]);
    if(arr[nextMove.col][nextMove.row]=='E')
        bNextRowEmpty = true;
    else bNextRowEmpty = false;
    return bNextRowEmpty;
}

//A better draw function thatn the one currently used
function movePiece(clickedBlock) {
    // Clear the block in the original position
    var ind = arr[selectedPiece.position.xpos][selectedPiece.position.ypos];

    fill_space(selectedPiece.position.xpos, selectedPiece.position.ypos, 'E');

    fill_space(clickedBlock.col, clickedBlock.row, ind);

    arr[clickedBlock.col][clickedBlock.row] = ind;

    arr[selectedPiece.position.xpos][selectedPiece.position.ypos] = 'E';

    var team = (currentTurn === AWAY_TEAM ? away : home),
        opposite = (currentTurn !== AWAY_TEAM ? away : home);

    team[selectedPiece.itr].position.xpos = clickedBlock.col;
    team[selectedPiece.itr].position.ypos = clickedBlock.row;

    // Draw the piece in the new position
    // drawPiece(selectedPiece, (currentTurn === HOME_TEAM));

    selectedPiece = null;

    currentTurn = (currentTurn === AWAY_TEAM ? HOME_TEAM : AWAY_TEAM);
}
