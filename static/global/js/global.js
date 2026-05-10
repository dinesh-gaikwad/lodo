console.log("Global JS Loaded");

function showMessage(message){
    alert(message);
}

function toggleElement(id){
    const element = document.getElementById(id);

    if(element.style.display === "none"){
        element.style.display = "block";
    }else{
        element.style.display = "none";
    }
}

function loader(status){
    if(status){
        console.log("Loading...");
    }else{
        console.log("Loaded");
    }
}
