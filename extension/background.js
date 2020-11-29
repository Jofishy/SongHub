chrome.runtime.onInstalled.addListener(()=>{
    chrome.storage.sync.set({color:'red'}, ()=>{
        console.log("the color is green");
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