const host = "http://man.com:5000"

const download = document.querySelector("#download");
const notify = document.querySelector("#notify");

download.addEventListener("click",()=>{
    chrome.tabs.query({active:true, currentWindow:true}, function(tabs){
        url = tabs[0].url;

        download.setAttribute("disabled", true);
        
        axios.get(`${host}/download?url=${url}`).then(()=>{
            notify.innerText = "Downloading!";
        }).catch((error)=>{
            notify.innerText = "Error downloading: " + error;
            //console.warn(error);
        });
    });
});

