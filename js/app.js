function va() {
    document.getElementById("myForm").submit();
}

async function SubmitVars() {

    var qur = document.getElementById('qur').value;

    // http://0.0.0.0:8000/api/search?q=gold
    const url = `https://findthatbit.com/api/search?q=${qur}`;
    console.log(url)
    console.log(JSON.stringify({ "search": qur }))



const res = await fetch(url,{method:"GET"});
            const responseText = await res.json();
            restx = (JSON.stringify(responseText.result));
        const obj = JSON.parse(restx);
        for (i =0; i < obj.length;i++){
                console.log(obj[i]);
                url0 = obj[0].url;
                url1 = obj[1].url;
                url2 = obj[2].url;
                url3 = obj[3].url;
                url4 = obj[4].url;
                document.getElementById('rs0').innerHTML = obj[0].text;
                document.getElementById('ru0').innerHTML ="<a href=" +  url0 + ">click here</a>";
                document.getElementById('rs1').innerHTML = obj[1].text;
                document.getElementById('ru1').innerHTML ="<a href=" +  url1 + ">click here</a>";
                document.getElementById('rs2').innerHTML = obj[2].text;
                document.getElementById('ru2').innerHTML ="<a href=" +  url2 + ">click here</a>";
                document.getElementById('rs3').innerHTML = obj[3].text;
                document.getElementById('ru3').innerHTML ="<a href=" +  url3 + ">click here</a>";
                document.getElementById('rs4').innerHTML = obj[4].text;
                document.getElementById('ru4').innerHTML ="<a href=" +  url4 + ">click here</a>";
        }};
