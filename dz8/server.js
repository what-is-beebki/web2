const http = require('http');
const WebSocket = require('ws');

const wsServer = new WebSocket.Server({port: 9000});

wsServer.on('connection', onConnect);

function onConnect(wsClient) 
{
	console.log("Сервер: Соединение установлено");
	wsClient.on('close', function() {console.log("Сервер: Соединение прервано");});
	wsClient.on('message', function(message) {console.log(`Сервер: получено сообщение "${message}"`);
	                                          wsClient.send('будь здоров');});
}
console.log("port 9000");