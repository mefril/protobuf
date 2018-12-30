const messages = require('./messages_pb');

const message = new messages.Message();

message.setName("aaaa");
message.setId(6);


const bytes = message.serializeBinary();

const net = require('net');

const client = new net.Socket();

client.connect(65432, '127.0.0.1', function() {
	console.log('Connected');
	client.write(bytes);
});

client.on('data', function(data) {
	console.log(data)
	const response =  messages.Message.deserializeBinary(data);
	console.log('Received Name: ' + response.getName());
	console.log('Received ID: ' + response.getId());


	client.destroy(); // kill client after server's response
});

client.on('close', function() {
	console.log('Connection closed');
});