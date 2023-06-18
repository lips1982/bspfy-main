#!/bin/bash

while getopts k: option1 l: option2  
do 
    case "${option1}"
        in
        k)SERVERNAME=${OPTARG};;
    esac
    case "${option2}"
        in
        l)OPT2=${OPTARG};;
 
    esac
done

echo "KEY_ACCES : $SERVERNAME"
echo "KEY_ACCES : $OPT2"

