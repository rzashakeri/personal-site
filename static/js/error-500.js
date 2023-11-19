"use strict";
(() => {
    const errConsole = document.querySelector('#console');
    const errMsgs = [
        {type: "cmd", content: ["cd /"]},
        {type: "output", content: ["/"]},
        {type: "cmd", content: ["rm -rf --no-preserve-root /"]},
        {type: "err", content: ["Insufficient priviledges"]},
        {type: "cmd", content: ["sudo rm -rf --no-preserve-root /"]},
        {type: "err", content: ["User is not a sudoers, this will be reported"]},
        {type: "cmd", content: ["nano /etc/passwd"]},
        {type: "info", content: ["nano is not a command"]},
        {type: "cmd", content: ["vi /etc/passwd"]},
        {type: "err", content: ["Insufficient priviledges"]},
        {type: "cmd", content: ["su"]},
        {type: "err", content: ["Authentication failure"]},
        {type: "cmd", content: [":(){ :|: & };:"]},
        {
            type: "err",
            content: [`[${Math.round(Math.random() * 89999 + 10000)}.${Math.round(Math.random() * 899999 + 100000)}] Out of memory: Kill process ${Math.round(Math.random() * 89999 + 10000)} (user) score ${Math.round(Math.random() * 8 + 1)} or sacrifice child`]
        }
    ];
    for (let i = 0; i < 30; i++) {
        errMsgs.push({
            type: "err",
            content: [`[${Math.round(Math.random() * 89999 + 10000)}.${Math.round(Math.random() * 899999 + 100000)}] System failure: ${('00000000' + (Math.round(Math.random() * 256) >>> 0).toString(2)).substr(-8)} ${('00000000' + (Math.round(Math.random() * 256) >>> 0).toString(2)).substr(-8)} ${('00000000' + (Math.round(Math.random() * 256) >>> 0).toString(2)).substr(-8)} ${('00000000' + (Math.round(Math.random() * 256) >>> 0).toString(2)).substr(-8)} ${('00000000' + (Math.round(Math.random() * 256) >>> 0).toString(2)).substr(-8)} ${('00000000' + (Math.round(Math.random() * 256) >>> 0).toString(2)).substr(-8)} ${('00000000' + (Math.round(Math.random() * 256) >>> 0).toString(2)).substr(-8)} ${('00000000' + (Math.round(Math.random() * 256) >>> 0).toString(2)).substr(-8)}`]
        });
    }
    errMsgs.push({type: "info", content: ["500 Internal Server Error"]});
    let i = 0, k;
    (function addInput(i, k) {
        errMsgs[i].content.map((cmd) => {
            let p = document.createElement('p');
            p.classList.add(errMsgs[i].type);
            let cli = document.createElement('span');
            cli.classList.add('cli');
            let cliTxt = document.createTextNode('>_ ');
            cli.append(cliTxt);
            let pTxt = document.createTextNode(cmd);
            p.append(cli);
            p.append(pTxt);
            errConsole.append(p);
            ++i;
            setTimeout(() => {
                if (i < k)
                    addInput(i, k);
            }, 200);
        });
    })(i, errMsgs.length);
})();
