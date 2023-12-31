const Kafka = require('no-kafka');

const consumer = new Kafka.SimpleConsumer({ connectionString: '127.0.0.1:9092' }); 

var data = function (messageSet) {
    messageSet.forEach(function (m) {
        var value = m.message.value.toString('utf8');
        console.log(value);
    });
};

return consumer.init().then(function () {
    return consumer.subscribe('kafka-python-topic', data);
});