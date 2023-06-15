function ClearResults() {
    document.getElementById('qur').innerHTML = "";
}

function myImageFunction(productSmallImg) {
    let productFullImg = document.getElementById("img-Box");
    productFullImg.src = productSmallImg.src;
}

function va() {
    document.getElementById("myForm").submit();
}

async function SubmitVars() {
    var qur = document.getElementById('qur').value;
    clearFeatures();
    // query FastAPI
    const url = `https://findthatbit.com/api/search?q=${qur}&limit=5`;
    console.log(url)
    console.log(JSON.stringify({ "search": qur }))



const res = await fetch(url,{method:"GET"});
	    const responseText = await res.json();
	    restx = (JSON.stringify(responseText.result));
	const obj = JSON.parse(restx);
	
	for (let i = 0; i < 5; i++) {
	 let dynamicId = 'ru' + i;
	 let dynamicIdtx = 'rs' + i;
	 let dynamicIdth = 'th' + i;


	document.getElementById("satoshi").innerHTML = '';
	document.getElementById(dynamicId).innerHTML = '<a href="' + obj[i].url + '">' + obj[i].title + '</a>';
	document.getElementById(dynamicIdtx).innerHTML = "..." + obj[i].text + "...";
	document.getElementById(dynamicIdth).innerHTML = '<img src="' + obj[i].thumbnail +'" style="max-height: 150px; max-width: 150px;"/>';
	document.getElementById(dynamicIdth).innerHTML = '<a href="' + obj[i].url + '"><img src="' + obj[i].thumbnail +'" style="max-height: 150px; max-width: 150px;"/></a>';

	}


	};



function features(){
    clearHtmlContentById('aboot');
    clearResults();	
    document.getElementById("featuresId").innerHTML = "<br>Type any sentence, phrase, or selection of words, submit, and you'll get related content from the most relevant videos, the sentences have been embedded using 'all-MiniLM-L6-v2' sentence-transformer - the videos have been carefully chosen to offer the best content for anyone interested in Bitcon (NOT Crypto) - If you would like to suggest a video to add to the site then let me know.  This is intended as a tool for anyone seriously interested in Bitcoin and/or any developers interested in 'Semantic Search and Vector Databases";};

function clearFeatures(){
	clearHtmlContentById('aboot');
	clearHtmlContentById('findthatbit');
	document.getElementById("featuresId").innerHTML = "";
}

function clearResults(){
	for (let i = 0; i < 5; i++) {
		         let dynamicId = 'ru' + i;
		         let dynamicIdtx = 'rs' + i;
		         let dynamicIdth = 'th' + i;

		        document.getElementById(dynamicId).innerHTML = "";
		        document.getElementById(dynamicIdtx).innerHTML ="";
		        document.getElementById(dynamicIdth).innerHTML ="";

	clearHtmlContentById('findthatbit');
}};

function clearAll(){
	document.getElementById("satoshi").innerHTML = '<img src="images/satoshi_lightning_address.jpg" style="max-height: 150px; max-width: 150px;"/>';
	clearResults();
	clearFeatures();
	clearHtmlContentById('aboot');
};

function setHtmlContentById(id, htmlContent) {
	 clearAll();
	  var element = document.getElementById(id);
	  if (element) {
		      element.innerHTML = htmlContent;
		    }
}

function clearHtmlContentById(id) {
	  var element = document.getElementById(id);
	  if (element) {
		      element.innerHTML = "";
		    }
}
