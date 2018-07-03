const path = require("path");
const webpack = require("webpack");
const BundleTracker = require("webpack-bundle-tracker");
const VueLoaderPlugin = require('vue-loader/lib/plugin');

module.exports = {

    entry: "./assets/js/main.js",
    output: {
        path: path.resolve("./assets/bundles/"),
        filename: "bundle.js",
    },

    module: {
        rules: [
            {
                test: /\.css$/,
                loader: 'style-loader!css-loader',
            },
            {
                test: /\.vue$/,
                loader: "vue-loader",
            },
        ],
    },

    devtool: "inline-source-map",

    plugins: [
        new BundleTracker({filename: "./webpack-stats.json"}),
        new VueLoaderPlugin(),
    ],

    resolve: {
        alias:{
            "vue": path.resolve('./node_modules/vue/dist/vue.js'),
        },
    },

    performance: {hints: false}

};