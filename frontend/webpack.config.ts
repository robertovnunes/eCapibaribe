import NodePolyfillPlugin = require("node-polyfill-webpack-plugin");

require('webpack');

module.exports = {
  plugins: [
    new NodePolyfillPlugin(),
  ],
  target: 'node18.17',
  resolve: {
    fallback: {
      url: require.resolve('url/'),
      path: require.resolve('path-browserify'),
      util: require.resolve('util/'),
      crypto: require.resolve('crypto-browserify'),
    },
  },
};
