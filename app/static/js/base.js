function chatBox(){
	var colMax = 45;

	var textarea = document.getElementById('input');
	var chars = parseInt(textarea.value['length']);
	var rows = parseInt(textarea.getAttribute('rows'));

  	var divLastcharsMax = document.getElementById('divLastcharsMax');
  	var lastCharsMax = parseInt(divLastcharsMax.getAttribute('value'));
	
	if(chars%colMax == 0 && lastCharsMax < chars){
		var lastCharsMax = chars;
		divLastcharsMax.setAttribute('value', lastCharsMax);
		textarea.setAttribute('rows', rows + 1);
	}else if(chars%colMax == 0 && lastCharsMax >= chars){
		var lastCharsMax = chars;
		divLastcharsMax.setAttribute('value', lastCharsMax);
		textarea.setAttribute('rows', rows - 1 );
	};


	console.log('chars : ' + chars);
	console.log('rows : ' + rows)
	console.log('lastCharsMax : ' + lastCharsMax);

}

chatBox()