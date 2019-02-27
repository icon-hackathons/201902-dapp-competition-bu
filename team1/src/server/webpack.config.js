var path = require('path');
var cheerio = require('cheerio');

module.exports = {
	devtool: "cheap-eval-source-map",
	entry: ['babel-polyfill', './public/src/js/main.js'],	// modify path
	output: {
		filename: 'bundleMain.js',	// modify path
		// path: "/Users/SG/istar/server/public/src/js/bundle"// modify path
		path: "/Users/SG/icon_project/icon_nft_game/server/public/src/js/bundle"
	},
	module: {
		rules: [
			//	Css loader loads the css into JS and the style loader injects it into the html file
			{
				test: /\.css$/,
				use: ['style-loader', 'css-loader']
			},
			// Babel ES7+
			{
				test: /\.js$/,
				exclude: /(node_modules)/,
				loader: 'babel-loader',
				query: {
					presets: ['env'],
					plugins: ["transform-regenerator"]
				}
			}
		]
	},
	plugins: [],
	/*	Instead of loading the raw-loader plugin and importing the html in javascript I set the devserver watch option on the html file 
		I created a new folder just for the html because, the devserver watches for changes only in a specific folder(not in a single file)
		,and if I did put the html file near the bundle.js file, the devServer would have watched for changes on the bundle.js file as well, thus 
		preventing hot reloading, and doing a full reload everytime I modify JS code 
	*/
	devServer: {
		contentBase: './public',
		watchContentBase: true
	}
};