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
    tackle = false,
    currentTurn = HOME_TEAM;

//these variables should not be changed
var hsqSize = sqSize/2,
    short_row = long_row-1;


var arr = [     ['E', 'E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E', 'E'],
                ['E', '0h', 'E', '1h', 'E'],
                ['E', 'E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'B', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E', 'E'],
                ['E', '1a', 'E', '0a', 'E'],
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
        pieces = new Image();
        pieces.src = '/static/battleball/images/pieces.png';
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

   
    
    // Check to see if block contains a piece
    if (selectedPiece === null) checkIfPieceClicked(clickedBlock);
    else if(tackle) processTackle(clickedBlock);
    // if there is a selected piece, move it
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
    var team = square_identifier.charAt(square_identifier.length-1);
    var ind = square_identifier.charAt(0);
    // Select color of space
    if (col === 0 && square_identifier === 'E') ctx.fillStyle = '#09D';
    else if (col == field_width && square_identifier === 'E') ctx.fillStyle = '#F55';
    else if (square_identifier === 'E') ctx.fillStyle = '#6C0';
    else if (square_identifier === 'B') ctx.fillStyle = 'yellow';
    else if (square_identifier === 'X') ctx.fillStyle = 'black';
    else if (team === 'h'){ 
        ctx.fillStyle = 'blue';
        //check if playerhas ball
        if(home[ind].has_ball){
            ctx.fillStyle = 'yellow';
            }
        }
    else if (team === 'a'){
         ctx.fillStyle = 'red';
         if(away[ind].has_ball){
            ctx.fillStyle = 'yellow';
            }
     }
    

    // get pieces coordinate and size
    var piece = coordinates(col, row);

    //place space on board
    ctx.fillRect(border + piece.x, border + piece.y, sqSize, piece.size);
    ctx.strokeRect(border + piece.x, border + piece.y, sqSize, piece.size);
    //place sprite
    if (team === 'h') 
        ctx.drawImage(pieces,0,2*66,66,66,border + piece.x, border + piece.y, sqSize, piece.size);
    else if (team === 'a')
        ctx.drawImage(pieces,1*66,1*66,66,66,border + piece.x, border + piece.y, sqSize, piece.size);
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
    if(tackle){
        var team = (currentTurn === HOME_TEAM ? away : home);
    }
    else{
        var team = (currentTurn === HOME_TEAM ? home : away);
    }

    return getPieceAtBlockForTeam(team, clickedBlock);
}

function getPieceAtBlockForTeam(teamOfPieces, clickedBlock) {
    // Returns the piece located at a space, otherwise returns null
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
    // Draw outline around selected piece
    ctx.strokeStyle = 'white';
    ctx.lineWidth = 4;

    var piece = coordinates(pieceAtBlock.position.xpos, pieceAtBlock.position.ypos);
    ctx.strokeRect(border + piece.x+2, border + piece.y+2, sqSize-4, piece.size-4);

    // selected piece is global
    selectedPiece = pieceAtBlock;
}

function removeSelection(selectedPiece) {

    fill_space(selectedPiece.position.xpos, selectedPiece.position.ypos,
        arr[selectedPiece.position.xpos][selectedPiece.position.ypos]);
    // add line to draw sprite
}

function processMove(clickedBlock) {
    /* When a piece is selected this function checks whether
       There is a piece at the location clicked
       if there is it removes the current selection and selects the next piece
       Otherwise if the move is allowed, the piece is moved
    */
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
    var occupied = surroundingSpaces(selectedPiece);
    var occounter, nextMove=[], bNextRowEmpty;
    
    nextMove.col = selectedPiece.position.xpos;
    nextMove.row = selectedPiece.position.ypos;

    for(occounter=0; occounter<occupied.length; occounter++) {
        if (occupied[occounter].row == clickedBlock.row &&
            occupied[occounter].col == clickedBlock.col &&
            occupied[occounter].col>=0 && occupied[occounter].col<=field_width) {
            nextMove = occupied[occounter];
        }
    }
    // Ensure next space is empty or has a ball on it 
    if(arr[nextMove.col][nextMove.row]=='E' || arr[nextMove.col][nextMove.row] == 'B')
        bNextRowEmpty = true;
    else bNextRowEmpty = false;
    return bNextRowEmpty;
}

//A better draw function thatn the one currently used
function movePiece(clickedBlock) {
    
    var ind = arr[selectedPiece.position.xpos][selectedPiece.position.ypos],
        cur_team = ind.charAt(ind.length-1);
        console.log(cur_team);
    if(arr[clickedBlock.col][clickedBlock.row] === 'B'){
        pickupBall(selectedPiece);
    }
    // Clear the block in the original position
    fill_space(selectedPiece.position.xpos, selectedPiece.position.ypos, 'E');
    // fill next space
    fill_space(clickedBlock.col, clickedBlock.row, ind);
    
    
    //update game board
    arr[clickedBlock.col][clickedBlock.row] = ind;
    arr[selectedPiece.position.xpos][selectedPiece.position.ypos] = 'E';
    
    // TODO: Tackle function    

    // update piece object to match board status, possibly it's own function later
    var team = (currentTurn === AWAY_TEAM ? away : home),
        opposite = (currentTurn !== AWAY_TEAM ? away : home);

    team[selectedPiece.itr].position.xpos = clickedBlock.col;
    team[selectedPiece.itr].position.ypos = clickedBlock.row;

    
    var occupied = surroundingSpaces(selectedPiece);
    for(var i = 0; i < occupied.length - 2; i++){
        var space = occupied[i];
        console.log(space);        
        var adj_ind = arr[space.col][space.row];
        console.log(adj_ind);
        if(adj_ind !== 'E' && adj_ind !== 'B'){
            var team = adj_ind.charAt(adj_ind.length-1);
            console.log(team); 
            if(team !== cur_team){
                tackle = true;
            }
        }
    }

    
    // change turn if not in tackle position
    if(tackle === false){
        selectedPiece = null;    
        currentTurn = (currentTurn === AWAY_TEAM ? HOME_TEAM : AWAY_TEAM);
    }
}

function surroundingSpaces(selectedPiece){
    /* 
    This function returns a list of the surrounding spaces
    relative to the selected piece
    */
    var col = selectedPiece.position.xpos,
        row = selectedPiece.position.ypos,
        u={}, d={}, ul={}, dl={}, ur={}, dr={}, l={}, r={},
        occupied=[];
    d.col = u.col = col;
    ul.col = dl.col = l.col = col-1;
    ur.col = dr.col = r.col = col+1;
    d.row = row-1;
    u.row = row+1;
    //endzone 1
    if(col === 0) {
        ul.row = row+1;
        l.row = ur.row = row;
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
    return occupied
}

function pickupBall(piece){
    // This function allows a piece to pick up
    // the game ball
    piece['has_ball'] = true;
}

function processTackle(clickedBlock){
    //This function checks whether the clicked block has an enemy piece
    // Then resolves the tackle
    // updates field
    var enemy_piece = getPieceAtBlock(clickedBlock);
    if(enemy_piece !== null){
        tackle_roll = roll(selectedPiece.roll_size);
        defend_roll = roll(selectedPiece.roll_size);
        alert('your piece rolled a ' + tackle_roll + ' the opposing team rolled a ' + defend_roll);
        //if tackling piece wins
        if(tackle_roll < defend_roll){
            if(tackle_roll === 1){
                enemy_piece.injured = 2;
            }

            enemy_piece.injured = 1;
            fill_space(enemy_piece.position.xpos,enemy_piece.position.ypos, 'X');
        }

         //if defending piece wins
        else if(tackle_roll > defend_roll){
            if(defend_roll === 1){
                selectedPiece.injured = 2;
            }
            selectedPiece.injured = 1;
            fill_space(selectedPiece.position.xpos,selectedPiece.position.ypos, 'X');
        }
        
        else {
            if(defend_roll === 1){
                selectedPiece.injured = 2;
                enemy_piece.injured = 2;
            }
            else{
                selectedPiece.injured = 1;
                enemy_piece.injured = 1;
                }
            fill_space(selectedPiece.position.xpos,selectedPiece.position.ypos, 'X');
            fill_space(enemy_piece.position.xpos,enemy_piece.position.ypos, 'X')
        }
        tackle = false;
        selectedPiece = null;    
        currentTurn = (currentTurn === AWAY_TEAM ? HOME_TEAM : AWAY_TEAM);
    }
}

