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

	document.getElementById(dynamicId).innerHTML = '<a href="' + obj[i].url + '">' + obj[i].title + '</a>';
	document.getElementById(dynamicIdtx).innerHTML = "..." + obj[i].text + "...";
	document.getElementById(dynamicIdth).innerHTML = '<img src="' + obj[i].thumbnail +'" style="max-height: 150px; max-width: 150px;"/>';
	document.getElementById(dynamicIdth).innerHTML = '<a href="' + obj[i].url + '"><img src="' + obj[i].thumbnail +'" style="max-height: 150px; max-width: 150px;"/></a>';

	}


	};


document.getElementById('btnSwitch').addEventListener('click',()=>{
    if (document.documentElement.getAttribute('data-bs-theme') == 'dark') {
        document.documentElement.setAttribute('data-bs-theme','light')
    }
    else {
        document.documentElement.setAttribute('data-bs-theme','dark')
    }
});
