const message = "Mensagem para ser invertida.";

const reverseMessage = (message: string) => {
    let reversedMessage = "";

    for(let index=message.length-1; index>=0; index--){
        reversedMessage += message[index];
    }

    return reversedMessage;
}

console.log(reverseMessage(message))