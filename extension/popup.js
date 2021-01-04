(async ()=>{
    const host = "http://localhost:5000"

    const status_ui = document.querySelector("#status-ui");
    const status_text = document.querySelector("#status-text");

    const download_ui = document.querySelector("#download-ui");
    const download_botton = document.querySelector("#download-button");
    const notify = document.querySelector("#notify");

    const url = await getUrl();
    const status = await getDlStatus(url);

    notify.innerText = status;

    if (status){
        // already downloading/downloaded

        // query status
        download_ui.setAttribute("hidden", true);
        status_text.innerText = status;
        
    } else {
        // not downloaded, give download option
        status_ui.setAttribute("hidden", true);
    }

    download_botton.addEventListener("click", async ()=>{
        download_botton.setAttribute("disabled", true);
        
        axios.get(`${host}/download?url=${url}`).then(async ()=>{
            // set download link for this page
            notify.innerText = "Downloading";

            await setDlStatus(url, "downloading")
            
        }).catch((error)=>{
            notify.innerText = "Error downloading: " + error;
            //console.warn(error);
        });
    });

    function getUrl(){
        return new Promise((resolve, reject)=>{
            chrome.tabs.query({active:true, currentWindow:true}, function(tabs){
                const url = tabs[0].url;
                resolve(url);
            });
        });
    }

    function getAllStatuses(){
        return new Promise((resolve,reject)=>{
            chrome.storage.sync.get(["dl_status"], (result)=>{
                resolve(result.dl_status);
            });
        });
    }

    async function getDlStatus(url){
        const status = await getAllStatuses();

        return status[url];
    }

    function setDlStatus(url, status){
        return new Promise((resolve, reject)=>{
            const status = getAllStatuses();
            status[url] = status;
            chrome.storage.sync.set({"dl_status":status}, (result)=>{
                resolve();
            });
        })
        
    }
})();
