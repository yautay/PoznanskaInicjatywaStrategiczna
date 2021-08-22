const {src, dest, series, parallel, watch} = require("gulp");
const kit = require("gulp-kit")
const replace = require('gulp-replace');
const clean = require('gulp-clean')


const paths = {
    kits: "src/templates/",
    public: "public"
    }

const gtm_token = {
    demo: "GTM-hidden",
    prod: "GTM-hidden"
}

function clean_index_html(done) {
    src(paths.public + "/index.html", {read: false, "allowEmpty": true}).pipe(clean());
    done();
}

function handleKits(done) {
    src(paths.kits + "index.kit")
        .pipe(kit())
        .pipe(dest(paths.public))
    done();
}

function gtm_app_prod(done) {
    src(paths.kits)
        .pipe(replace(/GTM-.{7}/g, function handleReplace(match) {
            if (match === gtm_token.prod){
                console.log("Found PRODUCTION token");
                console.log("Leaving PRODUCTION token");
                return match}
            else {
                console.log("Found DEMO token");
                console.log("Replacing with PRODUCTION token");
                return gtm_token.prod;}}))
        .pipe(dest(paths.kits));
    done();
}

function gtm_app_demo(done) {
    src(paths.kits)
        .pipe(replace(/GTM-.{7}/g, function handleReplace(match) {
            if (match === gtm_token.demo){
                console.log("Found DEMO token");
                console.log("Leaving DEMO token");
                return match}
            else {
                console.log("Found PRODUCTION token");
                console.log("Replacing with DEMO token");
                return gtm_token.demo;}}))
        .pipe(dest(paths.kits));
    done();
}

exports.default = series(clean_index_html, gtm_app_demo, handleKits);
exports.production = series(clean_index_html, gtm_app_prod, handleKits);
