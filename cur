#! /bin/bash

# Currency converter

NAME=${0##*/}
VERSION="1.0"

clean_up(){
return
}

error_exit(){
echo -e "$NAME: ${$1:- "Unknown Error"}" >&2
clean_up
exit 1
}

graceful_exit(){
clean_up
exit
}

signal_exit(){
  case $1 in
    INT)
       error_exit "Program interrupted by the user" ;;
    TERM)
       echo "$NAME: Program terminated" >&2
       graceful_exit ;;
    *)
       error_exit "$NAME: Unknown error.. Terminating...." ;;
  esac
}

usage(){
echo -e "Usage: $NAME [-h| --help] | [[*currency_from*] [*currency_to*] [*amount]]"
}

help_message(){
cat <<- _EOF_
$NAME Version $VERSION
Currency converter

$(usage)
_EOF_
return
}

trap "signal_exit TERM" TERM HUP
trap "signal_exit INT" INT

# MAIN

if [[ ! $# -eq 0 ]]; then
echo "$(curl -s "https://www.xe.com/currencyconverter/convert/?Amount=${3^^}&From=${1^^}&To=${2^^}" | pup 'p.dPdXSB text{}' | awk 'NR==1{print $1}') ${2^^}"


else
  echo 'Currency Converter'
  read -p 'Please enter the currency you would like to convert from: ' from
  read -p 'Please enter the currency you would like to convert to: ' to
  read -p 'Please enter the amount: ' amount
  echo "$(curl -s "https://www.xe.com/currencyconverter/convert/?Amount=${amount^^}&From=${from^^}&To=${to^^}" | pup '.dPdXSB text{}' | awk 'NR==1{print $1}') ${to^^}"
fi

graceful_exit









