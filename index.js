var gpio = require('rpi-gpio');
 
gpio.on('change', function(channel, value) {
	console.log('Channel ' + channel + ' value is now ' + value);
});

gpio.setup(23, gpio.DIR_IN, gpio.EDGE_BOTH);

setInterval(()=>{
  console.log('eyy');
}, 10000);
