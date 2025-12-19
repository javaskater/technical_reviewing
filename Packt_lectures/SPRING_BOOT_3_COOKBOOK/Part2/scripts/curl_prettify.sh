#!/usr/bin/env bash

function main(){
    url=$1
    curl ${url} > output.json
    ret=$?
    if [ $ret -eq 0 ]; then
        echo "le curl d'est bien passé on passe au formatage"
        node -e "console.log(JSON.stringify(JSON.parse(require('fs').readFileSync(process.argv[1])), null, 4));" output.json | tee outputFmt.json
    else
        echo "le curl a eu un problème code retour ${ret}"
    fi
}

main $1