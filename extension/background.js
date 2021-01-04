chrome.runtime.onInstalled.addListener(()=>{
    chrome.storage.sync.set({dl_status:{}}, ()=>{
        // don't need to do anythign
    });

    chrome.declarativeContent.onPageChanged.removeRules(undefined, ()=>{
        chrome.declarativeContent.onPageChanged.addRules([{
            conditions: [new chrome.declarativeContent.PageStateMatcher({
                pageUrl: {urlContains: 'youtube.com/watch?v'},
            })],
            actions: [new chrome.declarativeContent.ShowPageAction()]
        }]);
    });
});