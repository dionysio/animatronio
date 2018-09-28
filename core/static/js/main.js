$( document ).ready(function() {
    var $container = $('#gallery');
    $container.imagesLoaded(function () {
        $container.masonry({
                columnWidth: 275,
                fitWidth: true,
                gutter: 9,
        });
        $container.css('opacity', 1);
    });
    var label = {};
    label.replace = function(t1, t2) {
        return $('.grid-item:nth-child('+t2+') a').attr('data-caption');
    }
    lightbox.option({
         'albumLabel': label,
         'wrapAround': true,
         'alwaysShowNavOnTouchDevices': true
    })
});
