var gulp = require('gulp');
var path = require('path');
var sass = require('gulp-sass')(require('sass'));
var autoprefixer = require('gulp-autoprefixer');
var sourcemaps = require('gulp-sourcemaps');
var open = require('gulp-open');

var Paths = {
  HERE: './',
  DIST: 'dist/',
  CSS: './css/',
  SCSS_TOOLKIT_SOURCES: './scss/soft-ui-dashboard.scss',
  DARK_MODE_SOURCE: './scss/dark-theme-core.scss',
  SCSS: './scss/**/**'
};

gulp.task('compile-scss', function() {
  return gulp.src([Paths.SCSS_TOOLKIT_SOURCES, Paths.DARK_MODE_SOURCE])
    .pipe(sourcemaps.init())
    .pipe(sass().on('error', sass.logError))
    .pipe(autoprefixer())
    .pipe(sourcemaps.write(Paths.HERE))
    .pipe(gulp.dest(Paths.CSS));
});

gulp.task('watch', function() {
  gulp.watch(Paths.SCSS, gulp.series('compile-scss'));
});

gulp.task('open', function() {
  gulp.src('pages/dashboard.html')
    .pipe(open());
});

gulp.task('open-app', gulp.parallel('open', 'watch'));