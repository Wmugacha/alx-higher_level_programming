#!/usr/bin/node

const request = require('request');

const id = process.argv[2];

const options = {
	method: 'GET',
	url: 'https://swapi-api.alx-tools.com/api/films/:${id}'
};

request(options, function (error, response, body) {
	if (error) {
		console.error(error);
	} else if {
		(Films.episode_id === id)
		{
			console.log();

	}
});
