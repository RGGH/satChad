

function myImageFunction(productSmallImg) {
    let productFullImg = document.getElementById("img-Box");
    productFullImg.src = productSmallImg.src;
}

function va() {
    document.getElementById("myForm").submit();
}

async function SubmitVars() {

    var qur = document.getElementById('qur').value;

    // http://0.0.0.0:8000/api/search?q=gold
    const url = `https://findthatbit.com/api/search?q=${qur}`;
    console.log(url)

    const res = await fetch(url, {

        method: "GET",
    });


    console.log(JSON.stringify({ "search": qur }))
    const responseText = await res.json();
    console.log(responseText)
    document.getElementById("rs").innerHTML = "Yay";

	

};
